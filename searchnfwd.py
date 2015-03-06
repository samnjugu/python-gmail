from Tools import *
import datetime

#This class searches todays emails that mmet the search criteria and fwds to the list of emails

EMAIL_ACCOUNT = "somuser@gmail.com"
EMAIL_PASS = 'somepass'

imap = ImapGmail(EMAIL_ACCOUNT,EMAIL_PASS)
imap.folder_select('INBOX')#select a folder to search use list_mailboxes() to see what is available
#adjust timedelta(0) to suit ur needs 0 = today, 1 = yesterday etc
date = (datetime.date.today() - datetime.timedelta(0)).strftime("%d-%b-%Y")
querys = ['(FROM "daycare" SUBJECT "Morning Report" SENTSINCE "'+date+'")', '(FROM "daycare" SUBJECT "Afternoons Report" SENTSINCE "'+date+'")',
                '(FROM "daycare" SUBJECT "Activity Report" SENTSINCE "'+date+'")']
imap.folder_search(querys)
imap.imap_close()
imap.fwd_emails(EMAIL_ACCOUNT, EMAIL_PASS, ["anotheruser@gmail.com","some@yahoo.com","stillkicking@aol.com"])
