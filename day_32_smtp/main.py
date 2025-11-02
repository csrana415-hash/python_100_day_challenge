################day_32

###smtp --> pre-boundle with python help us to send emain
###daytime -->is to check date

##video 245
###smtp lib help us to set send these mains

### SMTP FOR GMAIL---> smtp.gmail.com
##hotmail ----> smtp.live.com
##yahoo ---> smtp.mail.yahoo.com
# import smtplib
#
# ##for generating password go to gmail and enable twor factor authentication --> generate passowrd --> other --> put app name any thing then copy the pass and pes
# password="bardhg"
# my_email = "cabddd@gmail.com" ### sender email address
# with smtplib.SMTP("smtp.gmail.com")  as connection:#### address of smtp server
#     connection.starttls() ### this to secure our email connection over internet
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="csdgs@gmail.com",
#                         msg="Subject:Hello\n\nhola kaise ho aap")  ### thses \n\n for wring msg


#######video 246
### datetime --> its prebuild --> datetime module having same datetime class
#
# import datetime as dt
# import random
# import smtplib
#
# now = dt.datetime.now()  ### this will print all date and time its a datetime module
# year = now.year  ### this will give only year , its a int class
# month = now.month
# day = now.day
# week_day = now.weekday()  ### its satrt counting from 0 so on sunday oit will give 6
# print(year,month,day, week_day)
#
# bith_day = dt.datetime(year=1995, month=10, day=15, hour=6) ##specifiying the particula date anda time , hour
# print(bith_day)
#
# ###checking
#
# if dt.datetime.now() == dt.datetime.now():
#     with open("quotes.txt", "r") as lines:
#         one_quote = random.choice(lines.readlines())
#         # print(one_quote)
#     with smtplib.SMTP("smtp.gmail.com") as connect:
#         connect.starttls()
#         connect.login(user="csgsgs@gmail.com", password="barsgsgfsd")
#         connect.sendmail(from_addr="cfsagsd@gmail.com", to_addrs="gbsdhsdh@gmail.com", msg=f"Subject:verify current date time\n\n ahh.. its {dt.datetime.now()} \n {one_quote}")
#

####### video 248
### sending email