import argparse
from fill_in.deck_cards import Deck
import numpy as np
import datetime
import os


parser = argparse.ArgumentParser(description="Take test")
parser.add_argument("fname", type=str)
parser.add_argument("-n", "--nwords", type=int, default=10)

args = parser.parse_args()
deck = Deck(args.fname)
cards = deck.cards
words = np.random.choice(cards, size=args.nwords, replace=False)

fname = "Hindi_test_{}.txt".format(datetime.datetime.strftime(datetime.datetime.now(), '%d_%m_%y_%H_%M'))
with open(fname, "w") as fout:
     fout.write("Answer the following questions\n")

     for i, aword in enumerate(words, 1):
          fout.write("{0}. {1}\n".format(i, aword.question))

     
     fout.write(" \n"*20) 
     fout.write("Answers\n")

     for i, aword in enumerate(words, 1):
	     fout.write("{0}. {1}\n".format(i, aword.answer))


os.system("open {}".format(fname))

