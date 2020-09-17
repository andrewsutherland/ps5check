import requests
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# product web page to monitor
url = 'https://www.amazon.com/exec/obidos/ASIN/B08F3PZ13Z/'

# sender gmail credentials and setup
sender_address = 'changethis@gmail.com'  # < YOUR GMAIL ADDRESS HERE >
sender_pass = 'changethis'

# recipient...
# lookup your mobile carriers format for email to text
recipient_address = '8888888888@tmomail.net'  # < EMAIL ADDRESS TO SEND TO >

# create email contents
mail_content = "email body"  # < ENTER EMAIL BODY TEXT HERE >
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = recipient_address
message['Subject'] = "PS5 Available on Amazon"
message.attach(MIMEText(mail_content, 'plain'))

# email scraping loop
while True:
    
    # download the webpage and save read the contents
    r = requests.get(url, allow_redirects=True)
    response = r.text
    
    # check to see if the web server responded or timed out
    # status code 200 indicates a good response
    if r.status_code == 200:
            
        # try to send the email indicating the alert email
        # the TRY statement keeps the script from crashing if the email...
        # fails to send for some reason
        # if an email is sent the script stops
        try:
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(sender_address, sender_pass)
            text = message.as_string()
            session.sendmail(sender_address, recipient_address, text)
            print('mail sent')
            break
        except:
            print("Error: unable to send email")
        
        session.quit()
    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"Not yet :( [{current_time}]")
        
    # if the page is still down or did not respond the script tries again after a delay
    time.sleep(30)  # < SET DELAY TIME IN SECONDS HERE >
