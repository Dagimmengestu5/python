import requests
response = requests.get(url="http://api.open-notify.org/iss-new.json")
print(response.status_code)
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
