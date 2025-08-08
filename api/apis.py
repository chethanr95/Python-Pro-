import requests

MY_LAT = 12.971599
MY_LNG = 77.594566

my_latlong = {
    "lat" : MY_LAT,
    "lng" : MY_LNG
}

response = requests.get(url = "https://api.sunrise-sunset.org/json", params = my_latlong)
response.raise_for_status()

#print(response.status_code)

data = response.json()
print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(f"Today's Sunrise is at = {sunrise}")
print(f"Today's sunset is at = {sunset}")

