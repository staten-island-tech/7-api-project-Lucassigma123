import requests

def getvalo(valo):
 response = requests.get(f"https://valorant-api.com{valo.lower()}")
 if response.status_code != 200:
     print("Error fetching data!")
     return None
 data = response.json()
 return {
        "name": data["name"],
        