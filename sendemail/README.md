
1.	Install the Python 3.6 or latest version (what I use)
https://www.python.org/

2.	In windows command line, run
py  --version
make sure it display the python version

3.	For Gmail Email sender you want to test, need turn on less secure option:
http://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
In a nutshell, google is not allowing you to log in via smtplib because it has flagged this sort of login as "less secure", so what you have to do is go to this link while you're logged in to your google account, and allow the access:
https://www.google.com/settings/security/lesssecureapps

4.	Run Test
There is a working example in /src/simpleEmail.py
Change the
gmail_sender = 'youremail'
gmail_passwd = 'youremailpassword'
To your email and password, then run “test email.bat”, it will send a test email to you

5.	For more example, can check
https://docs.python.org/3.6/library/email-examples.html


