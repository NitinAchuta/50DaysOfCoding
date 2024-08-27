import smtplib
import datetime as dt
import pandas as pd
import random

email = "Your email here"
password =  "Your password here"

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

birthday_matches = False
data = pd.read_csv('Birthday_Wisher_Final/birthdays.csv')
all_months = data.month.to_list()
if month in all_months:
    birthday_matches = True
    todays_birthday = data[data.day == day]
    name = todays_birthday.name.to_string(index=False)

if birthday_matches:
    with open(f"Birthday_Wisher_Final/letter_templates/letter_{random.randint(1,3)}.txt", 'r') as file:
        letter = file.read()
        letter = letter.replace("[NAME]", f"{name}")

# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
    connection.starttls()
    connection.login(user = email, password=password)
    connection.sendmail(from_addr=email, to_addrs="TO ADDRESS HERE", msg=f"Subject:Happy Birthday {name}!\n\n{letter}")
print("done")



