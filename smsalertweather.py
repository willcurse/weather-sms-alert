import requests
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "fee269a2cc885b8bc812130c8855b80a"

# Twilio credentials
account_sid = 'AC175b190390ce444cbb005689139326a8'
auth_token = '4b01dcee3a20fbbbaefd10d48d90b1fc'

weather_params = {
    "lat": 31.2304,
    "lon": 121.4737,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    main = hour_data["weather"][0]["id"]
    if int(main) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="hey! its rainig bring your umbrella ☔",
                     from_='+12176152565',
                     to='+917895099154'
                 )
    print(message.status)
else:
    print("No rain expected in Shanghai.")
