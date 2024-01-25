"""
Program to read and clean information from files
"""

import os, re
from tkinter import *
from random import randint

cwd = os.getcwd()

files = [f[:-4] for f in os.listdir(cwd) if os.path.isdir(cwd) and f.endswith(".txt")]
print(files)
#filename that stores all the french words

root = Tk()
root.title("Basic French Language Flashcard")
#canvas1 = Canvas(root,width = 300, height = 100)
#canvas1.pack()
root.geometry("600x500")





#canvas1.create_window(0,20, window=drop_down)


#opening,reading and storing the words and phrases
words_phrases = []
with open(files[0]+".txt", mode="r", encoding="utf-8") as f:
	for txt in f.readlines():
		txt1 = txt.strip("\n").split(":")
		#removing empty lines from the list
		txt1[:] = [x for x in txt1 if x]
		#adding new row entry into list and converting to tuple
		words_phrases.append(tuple(txt1))


###for error checking
#[print(w) for w in words_phrases]

count = len(words_phrases)
##for error checking
#print(count)



def next():
	
	#Clear screen
	answer_label.config(text="")
	user_entry.delete(0,END)
	hint_label.config(text="")
	##Reset hint stuff
	global hinter, hint_count
	hinter = ""
	hint_count = 0
	#create random selection
	global rand_word
	rand_word = randint(0, count-1)
	f_word.config(text=words_phrases[rand_word][0])


def answer():
	if (user_entry.get().strip().capitalize() == words_phrases[rand_word][1].strip().capitalize()) and (len(user_entry.get()) > 0):
		answer_label.config(text=f"Correct! {words_phrases[rand_word][0]} is {user_entry.get().strip().capitalize()}")
	else:
		answer_label.config(text=f"Incorrect! {words_phrases[rand_word][0]} is not {user_entry.get().strip().capitalize()}")


#keep track of hints
hinter = ""
hint_count = 0

def hint():
	global hint_count
	global hinter

	if hint_count < len(words_phrases[rand_word][1]):
		hinter = hinter + words_phrases[rand_word][1].strip()[hint_count]
		hint_label.config(text=hinter)
		hint_count += 1
	else:
		hint_count = 0


#Labels
f_word = Label(root, text="", font=("Helvetica",36))
f_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

user_entry = Entry(root, font=("Helvetica",18))
user_entry.pack(pady=20)

#create hint label
hint_label = Label(root, text="")
hint_label.pack(pady=20)

#Buttons
button_frame = Frame(root)
button_frame.pack(side= BOTTOM,pady=20)

answer_button = Button(button_frame, text="Answer", command = answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next",command = next)
next_button.grid(row=0, column=1)

hint_button = Button(button_frame, text="Hint", command = hint)
hint_button.grid(row=0, column=2, padx=20)



next()

root.mainloop()
