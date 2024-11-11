import turtle as tt
from turtle import *
import time 
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk,ImageDraw,ImageFont
import numpy as np

l = []

wn = tk.Tk() 
wn.geometry('1200x800+150+0')
wn.configure(bg="black") 

c_all = tk.Canvas(wn,height=800,width=1200)
skk = tt.RawTurtle(c_all)
c_all.configure(bg = "black",highlightbackground='black')
c_all.pack()

tries1=0
tries2=0
tries3=0
tries4=0
tries5=0
tries6=0

name_1_var = StringVar()
name_2_var = StringVar()
rounds_no = IntVar()
rounds_no.set(1)
word = StringVar()
space_label = StringVar(value='')
gues = StringVar()



tie_breaker_random = 0

hangman = np.array(["H","A","N","G","M","A","N"])
tries=0

player_1 = Image.open("player 1.png")
player_1_copy = player_1.copy()
player_2 = Image.open("player 2.png")
player_2_copy = player_2.copy()

round_options = ["1","2","3"]

def intro(): 
	skk.hideturtle()
	skk.color("white")
	skk.pensize(6)
	skk.speed(1)
	skk.pu()
	skk.goto(-10,120)
	skk.pd()

	skk.write("GIGGA NIGGA GAMES \n\n ", False, align="center",font=("veradana",25,"bold"))
	time.sleep(1)
	skk.write("PRESENTS",  False, align="center",font=("veradana",15,"bold"))
	time.sleep(2)
	skk.clear()

	skk.speed(8)
	skk.write("  HANGMAN",False,align="center",font=("veradana",25,"normal"))
	skk.shape("turtle") 
	skk.pu()
	skk.goto(-150,-150)
	skk.pd()
	skk.fillcolor("black")
	skk.begin_fill()
	for i in range (2):
		skk.fd(300)
		skk.right(90)
		skk.fd(30)
		skk.right(90)

	skk.pu()
	skk.fd(75)
	skk.pd()
	skk.left(90)
	skk.fd(250)
	skk.right(90)
	skk.fd(150)
	skk.right(90)
	skk.fd(70)
	skk.right(90)
	skk.fd(30)
	skk.right(90)
	skk.fd(40)
	skk.left(90)
	skk.fd(90)
	skk.left(90)
	skk.fd(220)

	skk.end_fill()

	skk.pu()
	skk.left(180)
	skk.fd(220)
	skk.right(90)
	skk.fd(90)
	skk.right(90)
	skk.fd(40)
	skk.left(90)
	skk.fd(15)
	skk.right(90)
	skk.pd()
	skk.fd(20)
	skk.pu()
	skk.fd(30)
	skk.left(90)
	skk.pd()
	skk. circle(15)
	skk.right(90)
	skk.fd(40)
	skk.right(180)
	skk.fd(25)
	countdown = 2
	for i in range (4):
		time.sleep(0.5)
		countdown+=0.5
		if countdown == 2.5:
			skk.left(120)
			skk.fd(20)
			skk.bk(20)
		if countdown == 3:
			skk.left(120)
			skk.fd(20)
			skk.bk(20)
			skk.right(60)
			skk.fd(25)
		if countdown == 3.5:
			skk.left(60)
			skk.fd(30)
			skk.bk(30)
			skk.right(120)
		if countdown == 4:
			skk.fd(30)
	time.sleep(1)
	skk.clear()

def ask_names():
	global player_1
	global player_2
	global lbl_1
	global btn
	global player_1_e
	global player_2_e
	global drop_menu


	player_1 = player_1.resize((250,250))
	player_1 = ImageTk.PhotoImage(player_1)

	player_2 = player_2.resize((250,250))
	player_2 = ImageTk.PhotoImage(player_2)

	c_all.create_image(-30,30,image=player_1,anchor=SE)
	c_all.create_image(30,30,image=player_2,anchor=SW)

	btn = Button(c_all,text="PLAY",command=set_word,width=7,height=1)
	btn.configure(bg="blue",fg="yellow",font=("veradana",20,"bold"))
	c_all.create_window(0,300,window=btn,anchor=CENTER)

	player_1_e = Entry(c_all,text=name_1_var,bd=3,bg="blue",fg="yellow",font=("veradana",15,"bold"),width=20)
	c_all.create_window(-80,86,anchor=E,window=player_1_e)

	player_2_e = Entry(c_all,text=name_2_var,bd=3,bg="blue",fg="yellow",font=("veradana",15,"bold"),width=20)
	c_all.create_window(80,86,anchor=W,window=player_2_e)

	lbl_1 = Label(c_all,text = "ENTER THE NAME OF THE PLAYERS ...",font=("veradana",20,"bold"),fg="yellow",bg="black")
	c_all.create_window(0,-250,anchor=CENTER,window=lbl_1)

	lbl_2 = Label(c_all,text="SELECT NO OF ROUNDS TO BE PLAYED :",font=("veradana",15,"bold"),fg="yellow",bg="black")
	c_all.create_window(100,200,anchor=E,window=lbl_2)

	drop_menu = OptionMenu(c_all,rounds_no,*round_options)
	drop_menu.configure(bg="blue",fg="yellow",font=("veradana",10,"bold"),activebackground="blue",activeforeground="yellow",bd=0)
	c_all.create_window(105,200,anchor=W,window=drop_menu)

def set_word():

	global setter
	global finder
	global player_1
	global word_e
	global rounds

	name_1_var = player_1_e.get()
	name_2_var = player_2_e.get()
	rounds = rounds_no.get()
	c_all.delete("all")

	rounds*=2
	print(rounds)#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

	if tie_breaker_random == 0:
		if rounds%2==0:
			setter=name_1_var
			setter_img = player_1_copy
			finder=name_2_var
			finder_img = player_2_copy
		else:
			setter=name_2_var
			setter_img = player_2_copy
			finder=name_1_var
			finder_img = player_1_copy

	elif tie_breaker_random == 1:
		setter=name_1_var
		setter_img = player_1_copy
		finder=name_2_var
		finder_img = player_2_copy
		
	elif tie_breaker_random == 2:
		setter=name_2_var
		setter_img = player_2_copy
		finder=name_1_var 
		finder_img = player_1_copy
	
	if tie_breaker_random!=0:
		setter_declare_str=f"\n\n{setter} IS THE SETTER \n AND \n {finder} IS THE FINDER."
	
	image_set_word =setter_img.resize((200,200))
	pimage_set_word = ImageTk.PhotoImage(image_set_word)
	hehe = c_all.create_image(-350,-155,image=pimage_set_word,anchor=CENTER)
	l.append(pimage_set_word)

	dia_box = Image.open('dialog box.png')
	dia_box_copy = dia_box.copy()
	
	set_dia_box = dia_box_copy
	writer_set = ImageDraw.Draw(set_dia_box)
	font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",50)
	writer_set.text((200,200),'huhu',fill='red',font=font)
	set_dia_box = set_dia_box.resize((300,200))
	#set_dia_box.show()
	set_dia_box = ImageTk.PhotoImage(set_dia_box)
	sett_dia_box = c_all.create_image(-280,-180,image = set_dia_box,anchor=SW)
	l.append(set_dia_box)
	
	word_e = Entry(c_all,text = word,bd=3,bg="blue",fg="yellow",font=("veradana",20,"bold"),width=20)
	c_all.create_window(150,-96,anchor=W,window=word_e)

	image_find_word = finder_img.resize((200,200))
	pimage_set_word = ImageTk.PhotoImage(image_find_word)
	sui = c_all.create_image(-200,220,image = pimage_set_word,anchor = CENTER)
	l.append(pimage_set_word)

	find_dia_box = dia_box_copy
	find_dia_box = find_dia_box.resize((300,200))
	writer_find = ImageDraw.Draw(find_dia_box)
	writer_find.text((200,200),'huhu',font=font)
	find_dia_box = ImageTk.PhotoImage(find_dia_box)
	l.append(find_dia_box)
	c_all.create_image(8,0,image = find_dia_box,anchor = N)

	word_set_label = Label(c_all,text = f'{setter}:ENTER THE WORD YOU WANT {finder} TO GUESS ...',bg = "black", fg="yellow",font=('verdana',10,'bold'))
	word_set_label.config(text=word_set_label.cget("text").upper())
	c_all.create_window(50,-146,window=word_set_label,anchor = W)

	word_confirm_btn = Button(c_all,text = "SET WORD", height = 1 ,width = 8, bg="blue",fg="yellow",font=("veradana",15,"bold"),padx=10,bd = 3,command=stro)
	c_all.create_window(500,0,window=word_confirm_btn,anchor=E)

def movefront_hangman():
	pos = c_all.coords(c_drew)
	if pos[0]<390:
		c_all.move(c_drew,10,0)
		c_all.after(10,movefront_hangman)

def moveback_hangman():
	pos = c_all.coords(c_drew)
	if pos[0]>0:
		c_all.move(c_drew,-10,0)
		c_all.after(10,moveback_hangman)
	if pos[0]==0:
		if pos[1]>-150:
			c_all.move(c_drew,0,-10)
			c_all.after(10,moveback_hangman)
	
def stro():
	global c_drew,guess_e,c_draw
	global ggg,warning_label
	global space_label,spaces_label,spaces_array
	global spaces,letters
	global n,tpos
	global spp,skk
	global wordstr
	
	wordstr = word_e.get()
	#wordstr='sumesh'
	word = wordstr.upper()
	n = len(word)

	letters = np.empty(2*n,dtype=str)
	for i in range(n):
		letters[2*i+1] = word[i]
	print(letters)#3333333333333333333333333333333333333333333333333333333333333333333333333333

	dashes = np.repeat('_',n)
	spaces = ''
	for i in range (n):
		spaces = spaces + f' {dashes[i-1]}'

	c_all.delete('all')
	c_all.config(bg = 'black')
	
	space_label.set(spaces)
	space_label.set(space_label.get())

	c_draw = Canvas(c_all,width=600,height=400,highlightbackground='black')
	c_drew = c_all.create_window(0,0,window=c_draw,anchor=CENTER)
	skk = RawTurtle(c_draw)
	c_draw.config(bg='black')
	skk.pensize(4)
	skk.hideturtle()
	skk.color('blue')
	skk.speed(9)
	skk.pu()
	skk.goto(-150,-150)
	skk.pd()
	skk.fillcolor("blue")
	skk.begin_fill()
	for i in range (2):
		skk.fd(300)
		skk.right(90)
		skk.fd(30)
		skk.right(90)

	skk.pu()
	skk.fd(75)
	skk.pd()
	skk.left(90)
	skk.fd(250)
	skk.right(90)
	skk.fd(150)
	skk.right(90)
	skk.fd(70)
	skk.right(90)
	skk.fd(30)
	skk.right(90)
	skk.fd(40)
	skk.left(90)
	skk.fd(90)
	skk.left(90)
	skk.fd(220)

	skk.end_fill()

	skk.pu()
	skk.left(180)
	skk.fd(220)
	skk.right(90)
	skk.fd(90)
	skk.right(90)
	skk.fd(40)
	skk.left(90)
	skk.fd(15)
	skk.right(90)
	skk.pd()
	skk.fd(20)
	skk.pu()
	skk.speed(1)
	movefront_hangman()
	skk.bk(50)
	skk.fd(80)
	skk.left(90)
	skk.pd()
	tpos = skk.pos()
	print(tpos)#33333333333333333333333333333333333333333333333333333

	spaces_label = Label(c_all,font=('verdana',20,'bold'),text=space_label.get(),bg='black',fg = 'yellow',)
	c_all.create_window(0,-200,window=spaces_label,anchor=CENTER,tags='spaces_label')

	guess_e = Entry(c_all,text=gues,bg='blue',fg='yellow',width=3,font=('verdana',25,'bold'))
	c_all.create_window(0,-70,anchor=CENTER,window=guess_e,tags='guess_e')

	checker = Button(c_all,text='CHECK',bg='blue',fg='yellow',padx=5,font=('verdana',20,'bold'),command=guess_check)
	c_all.create_window(0,0,anchor=CENTER,window=checker,tags='checker')
#buggableeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
	print('entering buggable ......')
	# spp = RawTurtle(c_draw)
	# skk.fd(10)
	skk.hideturtle()
	skk.color('red')
	skk.pensize(4)
	skk.speed(9)
	skk.up()
	print(tpos)#333333333333333333333333333333333333333333333333333333333333333
	skk.goto(tpos)
	skk.down()

def guess_check():
	global warning
	global spaces,skk
	global tries
	global tries1,tries2,tries3,tries4,tries5,tries6
	global rounds

	guess = guess_e.get()
	guess = guess.upper()

	print(guess)#3333333333333333333333333333333333333333333333333333333333333333333333333333	

	if len(guess) != 1:
		warning = 'PLEASE ENTER A VALID INPUT'
		warning_label = Label(c_all,font=('verdana',20,'bold'),text=warning,bg='black',fg = 'red')
		ggg = c_all.create_window(0,-300,window=warning_label,anchor=CENTER,tags='unni')
		skk.pu()
		skk.fd(30)
		skk.bk(30)
		c_all.after(500,c_all.delete('unni'))	
		gues.set('')


	else :
		gues.set('')
		i=0
		j=0
		print(spaces)#33333333333333333333333333333333333333333333333333333333333333333333
		spaces_array = []
		for z in range (len(spaces)):
			spaces_array.append(spaces[z])

		spaces_array = np.array(spaces_array)
		print(spaces_array)#333333333333333333333333333333333333333333333333333333333

		for x in letters:
			if x==guess:
				index = np.argwhere(letters==guess)
				for w in index:
					spaces_array[w]=guess
					print(f'spaces array in loop {i}- {spaces_array}')
					i+=1
		
		print(spaces_array)#33333333333333333333333333333333333333333333333333333333

		if i==0:
			tries+=1

		for x in range (2*n):
			if letters[x]==spaces_array[x]:
				j+=1

		print('\n\n\n\n\n\n',j)#3333333333333333333333333333333333333333333333333333333
		spaces = ''
		for x in spaces_array:
			spaces = spaces + x

	print(tries)#333333333333333333333333333333333333333333333333333333333333333333
	print(spaces)#33333333333333333333333333333333333333333333333333333333333333
	space_label.set(spaces)
	spaces_label.config(text=space_label.get())

	print(f'tries = {tries}')
	print(f'tries1 = {tries1}')
	print(f'tries2 = {tries2}')
	print(f'tries3 = {tries3}')
	print(f'tries4 = {tries4}')
	print(f'tries5 = {tries5}')
	print(f'tries6 = {tries6}')

	if tries==1 and tries1 ==0:
		skk.circle(15)
		skk.right(90)
		tries1 = 1
	if tries==2 and tries2 ==0:
		skk.fd(40)
		skk.bk(25)
		tries2 = 1
	if tries==3 and tries3 ==0:
		skk.left(60)
		skk.fd(20)
		skk.bk(20)
		tries3 = 1
	if tries==4 and tries4 ==0:
		skk.right(120)
		skk.fd(20)
		skk.bk(20)
		skk.left(60)
		skk.fd(25)
		tries4 = 1
	if tries==5 and tries5 ==0:
		skk.left(60)
		skk.fd(30)
		skk.bk(30)
		skk.right(120)
		tries5 = 1
	if tries==6 and tries6 ==0:
		skk.fd(30)
		tries6 = 1
		c_all.delete('spaces_label','guess_e','checker')
		moveback_hangman()
		skk.up()
		skk.speed(1)
		skk.fd(300)
		game_over = Label(c_all,text=f'The word was {wordstr}.\n setter wins.',bg='black',fg='yellow',font=('veradana',25,'bold'))
		c_all.create_window(0,200,window=game_over,anchor=CENTER)
		word.set('')
		rounds-=1
		tries = tries1 = tries2 = tries3 = tries4 = tries5 = tries6 = 0
		set_word()

	if j==n:
		c_all.delete('all')
		finder_wins = Label(c_all,text='FINDER WINS',bg='black',fg='yellow',font=('veradana',25,'bold'))
		c_all.create_window(0,0,window=finder_wins,anchor=CENTER)
		word.set('')
		tries = tries1 = tries2 = tries3 = tries4 = tries5 = tries6 = 0
		rounds-=1
		set_word()

	
intro()
ask_names()
# stro()

wn.mainloop()
