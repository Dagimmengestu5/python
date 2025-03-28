import smtplib
import requests
from datetime import datetime
import time


my_email = "daveman191919@gmail.com"
my_password = "eajnrvqbekykqdvy"
my_lat = 8.980603
my_long = 38.757759

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if my_lat - 5 <= iss_latitude <= my_lat + 5 and my_long - 5 <= iss_longitude <= my_long + 5:
        return True
def is_night():
    parameters = {
        "lat":my_lat,
        "lng":my_long,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com")as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="dagimmengestu5@gmail.com",
                                msg="subject:It's the day of the week☝️☝️☝️☝️☝️☝️\n\niss is above you")


# go to up on the sky ok

# import requests
# import time
#
# url = "http://api.open-notify.org/iss-now.json"
#
# for attempt in range(3):  # Try 3 times
#     try:
#         response = requests.get(url, timeout=10)  # Timeout after 10 sec
#         response.raise_for_status()  # Raise error if response is bad
#         data = response.json()
#         print(data)
#         break  # Exit loop if request is successful
#     except requests.exceptions.RequestException as e:
#         print(f"Attempt {attempt + 1} failed: {e}")
#         time.sleep(5)  # Wait 5 seconds before retrying
