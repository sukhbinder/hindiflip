import eel
import numpy as np
import io
import json
from fill_in.deck_cards import Deck
from pathlib import Path
import os
import argparse
import sys
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser("HINDI Writing Practice")
    parser.add_argument("word_file", type=str, help="Word file")

    args = parser.parse_args()

    fname = Path(args.word_file).resolve()

    eel.init("web")

    def say(msg):
        os.system("say -v Lekha '{}'".format(msg))


    deckapp = Deck(fname)

    def selectwords(data):
        rdata = []
        for d in data:
            rdata.append([d.question, d.answer, d.num, d.active])
        random.shuffle(rdata)
        return rdata

    @eel.expose
    def handle_exit(ar1,ar2):
        sys.exit(0)

    @eel.expose
    def say_words(currcard):
        if currcard:
            msg = "The question is {0}".format(currcard["question"])
            say(msg)

    @eel.expose
    def get_words():
        ddata = deckapp.get_due_cards()
        if len(ddata) > 30:
            nnum = np.random.randint(23,30)
            ddata = ddata[:nnum]
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
                if a["question"] == d.question:
                    d.num = a["num"]
        deckapp.save_words(deckapp.ddata)
        return 1

    try:
        eel.start('different.html', size=(620,520) ,close_callback=handle_exit)
    except (SystemExit, MemoryError, KeyboardInterrupt):
        # We can do something here if needed
        # But if we don't catch these safely, the script will crash
        pass 

    print ('This is printed when the window is closed!')
