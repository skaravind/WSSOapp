# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
def send_email(receiver, subject, text):# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("wssotesttest@gmail.com","wssotest123")
	try:
		message = 'Subject: {}\n\n{}'.format(subject,text)
	 	# sending the mail
		s.sendmail("wssotesttest@gmail.com" ,receiver, message)
	 	# terminating the session
		print("Email Sent")
	except:
		print("Email failed to send.")

	s.quit()

