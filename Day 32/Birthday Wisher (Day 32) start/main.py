# #achutapython@gmail.com, #Abhipandu12
# #Yahoo is logged in through google
# #app password = "vfjs icwh ttoe vmdx"
import smtplib
import random

my_email = "achutapython@gmail.com"
password = "vfjsicwhttoevmdx"

with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs='goodlucknitin@gmail.com', msg = "Subject:Hello\n\nI'm sending this email through python")
print("done")


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year= 2005, month= 2, day= 26)

with open('quotes.txt') as file:
    quotes = file.readlines()
    quote_list = [quote.strip() for quote in quotes]
    
if day_of_week == 2:
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='aachuta@gmail.com', msg = f"Subject:Inspirational Quote\n\n{random.choice(quote_list)}")
        print('done')

