
import requests
import random
import json
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
Home = tk.Frame(root)
quiz = tk.Frame(root)
Home.pack(fill="both", expand=True)
root.title("RICK AND MORTY  CHARACTERS")
root.geometry("1280x600")

def search_CHARACTER():
      name= search.get()
      CHARACTER=getrickymort(name)
      outcome_label.config(text=str(CHARACTER))
      print(CHARACTER)
def randomfact():
    facts=json.load(open("facts.json"))["facts"]
    y=(random.choice(facts))
    outcomefact.config(text=str(y))

Label=tk.Label(Home,text="USE THE SEARCH BAR TO SEARCH FOR RICK AND MORTY CHARACTERS")
Label.pack(pady=10)
search =tk.Entry(Home,width=50)
search.pack(pady=10)

tk.Button(Home,text="SEARCH",command=search_CHARACTER ).pack(pady=10)
outcome_label= tk.Label(Home,font=("Georgia",12),text="",)# outcome of the search                                                                                                                                                                                                                                                                                                                                 
outcome_label.pack(pady=50)

tk.Button(Home,text="RANDOM FACT",command=randomfact).pack(pady=30)
outcomefact=tk.Label(Home,font=("Georgia",12),text="",)
outcomefact.pack(pady=40)

def show_quiz():
    Home.pack_forget()
    quiz.pack(fill="both", expand=True)
tk.Button(Home,text="game",command=show_quiz).pack(pady=50)
tk.Label(quiz,text="game screen",font=("Georgia",24)).pack(pady=20)
root.mainloop()
