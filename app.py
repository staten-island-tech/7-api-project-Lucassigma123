import requests

def getrickymort(rickymort):
 response = requests.get(f"https://rickandmortyapi.com{rickymort()}")
 if response.status_code != 200:
     print("Error fetching data!")
     return None
 data = response.json()
 return {
        "name": data["name"],
 