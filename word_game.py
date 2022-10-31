import pandas as pd
import numpy as np

from random import *

def count(guess,word):
	c = 0
	for i in guess:
		if i in word:
			c = c+1
	return c
	

df = pd.read_csv('words.csv')
arr = np.asarray(df)
n = randint(0,400)
word = arr[n][0].lower()
#print(word)

guess = input("Vola.. it's a five letter word...mmm.. Can you guess?!!..: ")
count =20
while(word != guess and count>0):
	print("oops no!! But you have %d letters in common..."%count(guess,word))
	count = count -1
	if count ==10:
		choice = input("Wanna Quit? Y/n")
		if choice == 'y' or choice =='Y":
			break
	guess = input("Guess again....")
	if len(guess) != 5:
		print("Say a five letter word")
		guess = input("Guess again....")
	
if word == guess:
	print("Correct ... You got it right")
	
else:
	print("You Lost :( \n\t The Word is '%s'"%word)

