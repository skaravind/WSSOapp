# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
def send_email(message):# creates SMTP session
	try:
		s = smtplib.SMTP('smtp.gmail.com', 587)
 
		# start TLS for security
		s.starttls()
	 
		# Authentication
		s.login("utkarsh97s@gmail.com", "")
	 
		# sending the mail
		s.sendmail("utkarsh97s@gmail.com", "vyombani@gmail.com", message)
		s.sendmail("utkarsh97s@gmail.com", "aravindraghavi@gmail.com", message)
	 
		# terminating the session
		s.quit()

		print("Email Sent")


	except:
		print("Email failed to send.")

