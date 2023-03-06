# Day 33: APIs

import requests
from datetime import datetime
import smtplib


MY_LAT = 43.156578
MY_LONG = -77.608849
MY_POSITION = (MY_LAT, MY_LONG)

# change these variables and the content of birthdays.csv
my_email = ""
my_smtp = "smtp.gmail.com"
my_password = ""
recipient_email = ""



# +- 5 degrees
def position_close(my_position):

    # get iss position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # raise exception if error occurred
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    iss_position = (longitude, latitude)

    if abs(my_position[0] - iss_position[0]) <= 5 and abs(my_position[1] - iss_position[1]) <= 5:
        return True


# is it dark
def dark(my_position):
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # current time
    time_now = datetime.utcnow()
    current_hour = time_now.hour
    current_minute = time_now.minute

    if current_hour >= sunset or current_hour <= sunrise:
        return True


if position_close(MY_POSITION) and dark(MY_POSITION):
    with smtplib.SMTP(my_smtp) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:Look up! ⬆\n\nThe ISS is above you!")
