import eel
import numpy as np
import io
import json
from fill_in.deck_cards import Deck, Card
import random

eel.init("web")

# class Deck():
#     def __init__(self, fname="words.csv"):
#         self.fname=fname
#         self.data = None
#         self.selected_words = None 
    
#     def load_data(self):
#         data = np.genfromtxt(self.fname, delimiter=",", skip_header=1, dtype=None, encoding=None)
#         self.data = data

#     def select_words(self):
#         if self.data is None:
#             self.load_data()
#         self.selected_words=[]
#         for i, d in enumerate(self.data):
#             if d[3]:
#                 self.selected_words.append(i)
#         np.random.shuffle(self.selected_words)
#         return self.data[self.selected_words]

#     def save_words(self, jdeck):
#         words = []
#         for a in jdeck:
#             words.append([a["sound"], a["picture"], str(a["num"]), str(a["active"])]) 
#         for word in words:
#             for d in self.data:
#                 if word[0] == d[0]:
#                     d[2] = int(word[2])
#         header="question,answer,num,active"
#         np.savetxt(self.fname, self.data, fmt="%s,%s,%i,%s",header=header, comments="")

deckapp = Deck("words.csv")

def selectwords(data):
    rdata = []
    for d in data:
        rdata.append([d.question, d.answer, d.num, d.active])
    random.shuffle(rdata)
    return rdata

@eel.expose
def handle_exit(ar1,ar2):
   import sys
   sys.exit(0)


@eel.expose
def get_words():
    ddata = deckapp.get_due_cards()
    print("{} words selected".format(len(ddata)))
    deckapp.ddata = ddata
    data = selectwords(ddata)
    a = io.StringIO()
    json.dump(data, a, separators=(',',':'))
    return a.getvalue()
    
@eel.expose
def save_words(deck):
    for a in deck:
        for d in deckapp.ddata:
            if a["sound"] == d.question:
                d.num = a["num"]
    deckapp.save_words(deckapp.ddata)
    return 1

try:
    eel.start('flipbook.html', size=(350,500) ,close_callback=handle_exit)
except (SystemExit, MemoryError, KeyboardInterrupt):
    # We can do something here if needed
    # But if we don't catch these safely, the script will crash
    pass 

print ('This is printed when the window is closed!')
