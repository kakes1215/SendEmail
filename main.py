import os
import smtplib
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

def main():
    sender = 'kaylynnpds'
    password = ''
    recipients = [
      'test'
    ]
    
    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'EMAIL SUBJECT'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # List of attachments
    attachments = ['text.txt']
    for x in range(10):
      # Add the attachments to the message
      for file in attachments:
          try:
              with open(file, 'rb') as fp:
                  msg = MIMEBase('application', "octet-stream")
                  msg.set_payload(fp.read())
              encoders.encode_base64(msg)
              msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
              outer.attach(msg)
          except:
              print("Unable to open one of the attachments.")

      composed = outer.as_string()

      # Send the email
      try:
          with smtplib.SMTP('smtp.office365.com', 587) as s:
              s.ehlo()
              s.starttls()
              s.ehlo()
              s.login(sender, password)
              s.sendmail(sender, recipients, composed)
              s.close()
          print(f'Email #{x} sent!')
          time.sleep(5)
      except:
          print("Unable to send the email. Error: ")
    

if __name__ == '__main__':
    main()