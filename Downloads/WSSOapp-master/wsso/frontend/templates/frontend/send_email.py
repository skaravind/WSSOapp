import smtplib 

import config

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login("utkarsh97s@gmail.com", "17091997")
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail('aravindraghavi@gmail.com', 'vyombani@gmail.com',message= 'al')
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")

subject = "Test subject"
msg = "Hello there, how are you today?"

send_email(subject, msg)

