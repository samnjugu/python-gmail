from Tools import *
import datetime

EMAIL_ACCOUNT = "somuser@gmail.com"
EMAIL_PASS = 'somepass'

imap = ImapGmail(EMAIL_ACCOUNT,EMAIL_PASS)
imap.folder_select('INBOX')#select a folder to search use list_mailboxes() to see what is available
date = (datetime.date.today() - datetime.timedelta(0)).strftime("%d-%b-%Y")
querys = ['(FROM "daycare" SUBJECT "Morning Report" SENTSINCE "'+date+'")', '(FROM "daycare" SUBJECT "Afternoons Report" SENTSINCE "'+date+'")',
                '(FROM "daycare" SUBJECT "Activity Report" SENTSINCE "'+date+'")']
imap.folder_search(querys)
imap.imap_close()
imap.fwd_emails(EMAIL_ACCOUNT, EMAIL_PASS, ["anotheruser@gmail.com","some@yahoo.com","stillkicking@aol.com"])
