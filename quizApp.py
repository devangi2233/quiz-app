from tkinter import *
from tkinter import messagebox as mb
import json


class Quiz:
	def __init__(self):
		
		self.q_no=0
		self.display_title()
		self.display_question()
		self.opt_selected=IntVar()
		self.opts=self.radio_buttons()
		self.display_options()
		self.buttons()
		self.data_size=len(question)
		self.correct=0


	def display_result(self):
		
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")



	def check_ans(self, q_no):
		
		if self.opt_selected.get() == answer[q_no]:
			return True

	def next_btn(self):
		
		if self.check_ans(self.q_no):
			self.correct += 1
		
		self.q_no += 1
		
		
		if self.q_no==self.data_size:
			self.display_result()
			gui.destroy()
		else:
			self.display_question()
			self.display_options()


	def buttons(self):
		next_button = Button(gui, text="Next",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		next_button.place(x=350,y=380)
		
		quit_button = Button(gui, text="Quit", command=call,
		width=5,bg="black", fg="white",font=("ariel",16," bold"),justify=RIGHT)
		quit_button.place(x=1000,y=50)

    
	def display_options(self):
		val=0
		self.opt_selected.set(0)
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1

	def display_question(self):
		q_no = Label(gui, text=question[self.q_no], width=60,
		font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		q_no.place(x=70, y=100)

	def display_title(self):
		title = Label(gui, text="DBMS QUIZ",
		width=90, bg="pink",fg="black", font=("ariel", 20, "bold"))
		title.pack(side=TOP)
    
    
	def radio_buttons(self):
		q_list = []
		y_pos = 150
		
		while len(q_list) < 4:
			radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("ariel",14))
			q_list.append(radio_btn)
			radio_btn.place(x = 100, y = y_pos)
			y_pos += 40
		return q_list

def call():
        res=mb.askquestion('Exit Application', 'Do you really want to Quit')
        if res == 'yes' :
            gui.destroy()
        else :
            mb.showinfo('Return', 'Returning to main application')

gui = Tk()
gui.geometry("1200x600")
gui.title("DBMS Quiz")

with open('data.json') as f:
	data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])


quiz = Quiz()
gui.mainloop()

