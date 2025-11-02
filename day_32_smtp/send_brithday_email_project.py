import smtplib
import pandas as pd
import datetime as dt
import random

######setiing cridentials
my_email = "csprogrammer311@gmail.com"
password = "bardhgrmxldndmkd"

## setting receiver perameteres
check_birth_date = pd.read_csv("birthdays.csv")
birth_name = check_birth_date.name[0]
birth_month = check_birth_date.month[0]
send_email = check_birth_date.email[0]
birth_date = check_birth_date.day[0]
#########checking today date and year and moth
now = dt.datetime.now()
month = now.month
day = now.day
####modifying latters
with open(f"letter_{random.randint(1,3)}.txt","r") as latter:
    check_later = latter.read()
    replace_name = check_later.replace("[NAME]",birth_name)


##checking perametres and sending email if match
######
if  birth_date ==day and birth_month:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=send_email, msg=f"Subject:Happy Birthday\n\n {replace_name}")



