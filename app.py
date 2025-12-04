import requests

def getrickymort(name):
  response = requests.get(f"https://rickandmortyapi.com/api/character/?name={name.lower()}")
  if response.status_code != 200:
        print("Error fetching data!")
        return None
    
  data = response.json()
  character=data["results"][0]
  return {
        "name": character["name"],
        "status": character["status"],
        "species": character["species"],
        "type": character["type"],
        "gender": character["gender"],
        "origin": character["origin"]
        
      }
import tkinter as tk
root = tk.Tk()
root.title("RICK AND MORTY  CHARACTERS")
root.geometry("1000x600")
Label=tk.Label(root,text="USE THE SEARCH BAR TO SEARCH FOR RICK AND MORTY CHARACTERS")
Label.pack(pady=20)
search =tk.Entry(root,width=50)
search.pack(pady=10)
outcome_label= tk.Label(root,text="")
outcome_label.pack(pady=20)


def search_CHARACTER():
      name= search.get()
      CHARACTER=getrickymort(name)
      outcome_label.config(text=str(CHARACTER))
      print(CHARACTER)

tk.Button(root,text="search",command=search_CHARACTER ).pack(pady=10)



root.mainloop()

