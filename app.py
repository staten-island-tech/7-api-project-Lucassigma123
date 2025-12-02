import requests

def getrickymort(name):
  response = requests.get(f"https://rickandmortyapi.com/api/character/?name={name.lower()}")
  if response.status_code != 200:
        print("Error fetching data!")
        return None
    
  data = response.json()
  return {
        "name": data["name"],
        "status": data["status"],
        "species": data["species"],
        "type": data["type"],
        "gender": data["gender"],
        "origin": data["origin"]
        
      }
CHARACTER=getrickymort("Morty")
print(CHARACTER)