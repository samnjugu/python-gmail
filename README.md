# python-gmail
Search retrieve and send emails with gmail using python.

I mainly wrote this code to automate forwding emails to kids grandparents sent by daycare on a daily bases
You can have gmail fwd your emails but the recepients have to acknowledege approval which is a hassle when 
dealing with non tech people.
You can also have your favourite email client do this, but I barely use mine everyday so with this solution and cron am covered.

Most of the work is done by Tools.py which handles importing imap and smtp library then wrapping the  main features I need in single API. This reduces code duplication since for all the classes where you need to email functionality you only have to import Tools.py.
