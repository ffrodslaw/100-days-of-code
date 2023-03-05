import smtplib
import datetime as dt
import random

# # change these variables to your email info and the recipient's
my_email = "myemail@gmail.com"
email_pw = "password"
email_to = "recipient@gmail.com"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=email_pw)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=email_to,
#         msg="Subject:Hello\n\nThis is the body of my email.")


now = dt.datetime.now()
day = now.weekday()

if day == 6:
    with open("quotes.txt", "r") as quotes:
        data = quotes.read().replace("\n",  " .").split(" .")
        qotd = random.choice(data)
        print(qotd)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_to,
            msg=f"Subject:Monday Motivation\n\n{qotd}")