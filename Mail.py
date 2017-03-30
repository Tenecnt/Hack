import smtplib
from email.mime.text import MIMEText
def sendsth(sth):
	user='dolabdream@qq.com'
	to='dolabdream@qq.com'
	msg=MIMEText(sth)
	msg['Subject']='Coming'
	msg['From']=user
	msg['To']=to

	try:
		s=smtplib.SMTP_SSL('smtp.qq.com','465')
		s.login(user,pwd)
		s.sendmail(user,to,msg.as_string())
		s.quit()
		print 'Success!'
	except smtplib.SMTPException,e:
		print "Failed,%s"%e
