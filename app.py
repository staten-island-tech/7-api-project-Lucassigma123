import requests
import random
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
        "origin": character["origin"],
      }
import tkinter as tk
root = tk.Tk()
root.title("RICK AND MORTY  CHARACTERS")
root.geometry("1280x600")

def search_CHARACTER():
      name= search.get()
      CHARACTER=getrickymort(name)
      outcome_label.config(text=str(CHARACTER))
      print(CHARACTER)
def randomfact():
    facts=["Rick Is Afraid Of Pirates",
           "Rick And Birdperson Share A Kiss In The Comics",
           "Mr. Poopybutthole Was The Parasite Catalyst"
    ]
    print(random.choice(facts))
   
Label=tk.Label(root,text="USE THE SEARCH BAR TO SEARCH FOR RICK AND MORTY CHARACTERS")
Label.pack(pady=10)
search =tk.Entry(root,width=50)
search.pack(pady=10)
tk.Button(root,text="search",command=search_CHARACTER ).pack(pady=10)
outcome_label= tk.Label(root,font=("Georgia",12),text="",)# outcome of the search 
outcome_label.pack(pady=50)
tk.Button(root,text="random fact",command=randomfact).pack(pady=200)
root.mainloop()

