#!/usr/bin/python
import smtplib, imaplib, email, email.header
# Utility class to handle IMAP and SMTP 
# IMAP is used to fetch emails while SMTP is used to send emails


class Gmail(object):
    def __init__(self, email, password):
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(email, password)
        self.session = session    
	
	#This method composes an email before sending
    def send_onetime_email(self,subject,body):
	sender = self.email
	receiver = 'user' #shows up in the To field not used 4 sending
	receivers = ['someuser@gmail.com'] #used 4 sending	
	msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" %(sender, receiver, subject, body))	 
	self.session.sendmail(sender, receivers, msg)
	self.session.close()
	
	#This method takes a msg which is an email already composed and doesn't close session
    def send_email_to(self,receivers,msg):
	self.session.sendmail(self.email, receivers, msg)
	

    def gmail_close(self):
        self.session.close()

class ImapGmail(object):
    def __init__(self, email, password):
	self.server = 'imap.gmail.com'
	self.session = imaplib.IMAP4_SSL(self.server)
	self.session.login(email, password)
	self.email_data_li = []

    def folder_select(self, folder):
	self.session.select(folder)
	
    def folder_search(self,querys):
	if querys:#only proceed if we have querys
	    for query in querys:#loop through all the querys
                rv, data = self.session.search(None, query)
                if rv != 'OK':
                    print "No messages found!"
                    return
                
                for num in data[0].split():
                    rv, data = self.session.fetch(num, '(RFC822)')#get the whole email
                    if rv != 'OK':
                        print "ERROR getting message", num
                        return
                    self.email_data_li.append(data)

    def imap_close(self):
        try:
            self.session.close()
        except imaplib.IMAP4.error:
            print 'Close called without calling select'
        finally:
            self.session.logout()
	     
    def messages_print_header(self):
	if self.email_data_li:
	    for data in self.email_data_li:
	        msg = email.message_from_string(data[0][1]) 
	        decode = email.header.decode_header(msg['Subject'])[0]
	        subject = unicode(decode[0])
	        print 'Message Subject: %s' % (subject)
	        print 'Date:', msg['Date']

    def list_mailboxes(self):
	rv, mailboxes = self.session.list()
	if rv == 'OK':
	    print "Mailboxes:"
	    print mailboxes #prints list of all mailboxes	

    def fwd_emails(self, user, passw, to_addr):
        if self.email_data_li:
            gm = Gmail(user, passw)
            for data in self.email_data_li:
	              # create a Message instance from the email data
	              message = email.message_from_string(data[0][1])
	              # replace headers 
	              message.replace_header("From", user)
	              message.replace_header("To", ', '.join(to_addr))#convert list to string
	              gm.send_email_to(to_addr, message.as_string())
            print "Done Sending Emails"
            gm.gmail_close()

