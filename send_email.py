# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
def send_email(receiver, subject, text):# creates SMTP session
	try:
		s = smtplib.SMTP('smtp.gmail.com', 587)
 		# start TLS for security
		s.starttls()
	 	# Authentication
		s.login("wssotesttest@gmail.com","wssotest123")

		message = 'Subject: {}\n\n{}'.format(subject,text)
	 	# sending the mail
		s.sendmail("wssotesttest@gmail.com" ,receiver, message)
	 	# terminating the session
		s.quit()
		print("Email Sent")
	except:
		print("Email failed to send.")

