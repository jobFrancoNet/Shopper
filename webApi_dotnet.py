import requests

indirizzo_webapi="http://localhost:57058/api/Values/1"

richiesta=requests.get(indirizzo_webapi)

jsondata=richiesta.json()

print(jsondata)