

import datetime as dt
import pandas
import smtplib
import random

# change these variables and the content of birthdays.csv
my_email = ""
my_smtp = "smtp.gmail.com"
my_password = ""
my_name = ""


# today's date
today = dt.datetime.now()
day = today.day
month = today.month
print(day)
print(month)

# get saved dates
data = pandas.read_csv("birthdays.csv")
data = data.to_dict(orient="records")


for row in data:
    print(row)
    if row["month"] == month and row["day"] == day:
        name = row["name"]
        email = row["email"]
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            email_text = letter.read()
            email_text = email_text.replace("[NAME]", name)
            email_text = email_text.replace("Angela", my_name)

            print(email_text)

            with smtplib.SMTP(my_smtp) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:Happy birthday\n\n{email_text}")



