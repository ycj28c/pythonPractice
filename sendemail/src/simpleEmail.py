import smtplib

# Gmail Sign In
gmail_sender = 'youremail'
gmail_passwd = 'youremailpassword'

TO = 'ryang@equilar.com'
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()