# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("wssotesttest@gmail.com","wssotest123")
 
def send_email(receiver, subject, text):# creates SMTP session
	try:
		message = 'Subject: {}\n\n{}'.format(subject,text)
	 	# sending the mail
		s.sendmail("wssotesttest@gmail.com" ,receiver, message)
	 	# terminating the session
		print("Email Sent")
	except:
		print("Email failed to send.")

while(1):
	send_email("utkarsh97s@gmail.com", "madarchod", "betichod")

s.quit()

