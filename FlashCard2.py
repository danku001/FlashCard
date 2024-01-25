import os
import tkinter as tk
from random import randint, seed
from datetime import datetime
import pyttsx3 as pyt

seed(datetime.now().timestamp())


class FlashCardGame:
	def __init__(self,master):
		self.master = master
		master.title("Basic French Language Flashcard Game")
		master.geometry("700x500")

		#Getting the vocabulary text file names.
		self.cwd = os.getcwd()
		self.file_names = [f[:-4] for f in os.listdir(self.cwd) if os.path.isdir(self.cwd) and f.endswith(".txt")]

		#MenuButton 
		self.menu_button = tk.Menubutton(master,text="Vocabulary Lists", 
			relief = tk.RAISED)
		self.menu = tk.Menu(self.menu_button, tearoff = 0)

		self.vocab_file = tk.StringVar()
		for f in self.file_names:
			self.menu.add_radiobutton(label=f,command = lambda f=f :self.click(f))
		#Associate inside menu with menubuttom
		self.menu_button["menu"] = self.menu 
		self.menu_button.pack(pady=5)


		#labels
		self.f_word = tk.Label(master, text="", font=("Helvetica",36))
		self.f_word.pack(pady=50)

		self.answer_label = tk.Label(master, text="")
		self.answer_label.pack(pady=20)

		self.user_entry = tk.Entry(master, font=("Helvetica",18))
		self.user_entry.pack(pady=20)

		self.hint_label = tk.Label(master, text="")
		self.hint_label.pack(pady=20)

		#buttons
		self.button_frame = tk.Frame(master)
		self.button_frame.pack(side=tk.BOTTOM, pady=20)

		self.answer_button = tk.Button(self.button_frame, text= "Answer", command = self.answer)
		self.answer_button.grid(row=0, column=0, padx=20)

		self.next_button = tk.Button(self.button_frame, text = "Next", command = self.next)
		self.next_button.grid(row = 0, column=1)

		self.hint_button = tk.Button(self.button_frame, text = "Hint", command = self.hint)
		self.hint_button.grid(row=0, column=2, padx=20)

		self.audio_button = tk.Button(self.button_frame, text= "Audio", command = self.speak)
		self.audio_button.grid(row=1, column=1, pady = 10)



	def click(self,file):
		"""
		Program to load new word document
		inputs:
			self: so the class can refer to itself and the attributes
			      in this method
			file: File name
		Operation:
			load the selected word document into memory
		"""
		self.cwd = os.getcwd()
		self.words_phrases = []
		with open(file+".txt", mode="r", encoding="utf-8") as f:
			for txt in f.readlines():
				txt1 = txt.strip("\n").split(":")
				#removing empty lines from the list
				txt1[:] = [x.strip() for x in txt1 if x]
				#adding new row entry into list and converting to tuple
				self.words_phrases.append(tuple(txt1))

		self.count = len(self.words_phrases)


	def next(self):
		#Clear Screan
		self.answer_label.config(text="")
		self.user_entry.delete(0,tk.END)
		self.hint_label.config(text="")
		##Reset hint stuff
		self.hinter = ""
		self.hint_count = 0
		self.rand_word = randint(0,self.count-1)
		self.f_word.config(text=self.words_phrases[self.rand_word][0])



	def answer(self):
		if (self.user_entry.get().strip().capitalize() == self.words_phrases[self.rand_word][1].strip().capitalize()) and (len(self.user_entry.get()) > 0):
			self.answer_label.config(text=f"Correct! {self.words_phrases[self.rand_word][0]} is {self.user_entry.get().strip().capitalize()}")
		else:
			self.answer_label.config(text=f"Incorrect! {self.words_phrases[self.rand_word][0]} is not {self.user_entry.get().strip().capitalize()}")


	def hint(self):

		if self.hint_count < len(self.words_phrases[self.rand_word][1]):
			self.hinter = self.hinter + self.words_phrases[self.rand_word][1].strip()[self.hint_count]
			self.hint_label.config(text=self.hinter)
			self.hint_count = self.hint_count + 1

		else:
			pass


	def speak(self):
		#object creation
		engine = pyt.init()
		engine.setProperty('voice',"french")
		engine.setProperty('rate',120)
		engine.say(self.words_phrases[self.rand_word][0])
		engine.runAndWait()



root = tk.Tk()
my_ui = FlashCardGame(root)
root.mainloop()