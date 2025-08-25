import requests
import json

city= input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=eb11a50ca2b54b98b8080400231208&q={city}"


r  = requests.get(url)
# print(r.text)

wdic = json.loads(r.text)
temp = wdic["current"]["temp_c"]
print(f"current temperature of {city} is {temp} degrees")