import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rate=data[0]['rates']

print(rate)


