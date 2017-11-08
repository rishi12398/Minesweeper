from Tkinter import *
import tkMessageBox
import random


#This is the main class
class Minesweeper:
	def __init__(self,master):
		self.p=0
		self.q=0
		self.l=[]
                    #Takes image files from the folder
		self.tile_plain=PhotoImage(file="tile_plain.gif")
		self.tile_clicked=PhotoImage(file="tile_clicked.gif")
		self.tile_mine=PhotoImage(file="tile_mine.gif")
		self.tile_flag=PhotoImage(file="tile_flag.gif")
		self.tile_wrong=PhotoImage(file="tile_wrong.gif")
		self.tile_no=[]
		for i in range(10):
			a=random.randint(0,63)
			if a not in self.l:
				self.l.append(a)
			else:
				i=i-1
		


		for x in range(1,9):
			self.tile_no.append(PhotoImage(file="tile_"+str(x)+".gif"))
                #creates a frame
		self.frame=Frame(master)
		self.frame.grid()

		self.label1=Label(self.frame,text="Minesweeper")
		self.label1.grid(row=0,column=0,columnspan=8)

		self.flags=0
		self.correct_flags=0
		self.clicked=0

		self.buttons={}
		self.mines=0
		x_cord=1
		y_cord=0

		for x in range(64):
			mine=0
			image_p=self.tile_plain
			if x in self.l: 
				mine=1
				self.mines=self.mines+1
				self.q=self.q+1
			#0:button
			#1:wether mine present(1:present,0:not present)
			#2:state(0:unclicked,1:clicked;2:flagged)
			#3:button number
			#4:coordinates
			#5:nearby mines
			self.buttons[x]=[Button(self.frame,image=image_p,width=30,height=30,bg="black"),mine,0,x,[x_cord,y_cord],0]
			self.buttons[x][0].bind("<Button-1>",self.lclick1(x))
			self.buttons[x][0].bind("<Button-3>",self.rclick1(x))

			y_cord=y_cord+1;
			if(y_cord==8):
				y_cord=0
				x_cord=x_cord+1

		for keys in self.buttons:
			self.buttons[keys][0].grid(row=self.buttons[keys][4][0],column=self.buttons[keys][4][1])
                #checks no.of mines near a tile
		for keys in self.buttons:
			x_crd=self.buttons[keys][4][0]
			y_crd=self.buttons[keys][4][1]
			self.near_mines=0    #Different for boundary tiles as no.of tiles surrounding it are different.
			if(keys==0):
				if (self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+8)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+9)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(keys==7):
				if (self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+8)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+7)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(keys==56):
				if (self.check_mines(keys-8)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys-7)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(keys==63):
				if (self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys-8)):
					self.near_mines=self.near_mines+1
				if (self.check_mines(keys-9)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(x_crd==1):
				if(self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+9)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+8)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+7)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(y_crd==0):
				if(self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-8)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-7)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+8)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+9)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(x_crd==8):
				if(self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-9)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-8)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-7)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			elif(y_crd==7):
				if(self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+8)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+7)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-8)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-9)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
			else:
				if(self.check_mines(keys-1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+1)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+7)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+8)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys+9)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-9)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-8)):
					self.near_mines=self.near_mines+1
				if(self.check_mines(keys-7)):
					self.near_mines=self.near_mines+1
				self.buttons[keys][5]=self.near_mines
                #creates two labels which shows the the no.of mines in the game and no.of flags you can still plant.
		self.label2=Label(self.frame,text="Mines: "+str(self.mines))
		self.label2.grid(row=9,column=0,columnspan=4)
		self.label3=Label(self.frame,text="Flags: "+str(self.flags))
		self.label3.grid(row=9,column=4,columnspan=4)
         
        #after completion of one game, we use this function to forget the previous game and show the new game. 
	def forgetframe(self):
               self.frame.grid_forget()
       
	def check_mines(self,keys):	
		try:
			if (self.buttons[keys][1]==1):
				return True
			else:
				return False
		except KeyError:
			pass

	def lclick1(self,keys):
		return lambda Button: self.l_click1(self.buttons[keys])

	def rclick1(self,keys):
		return lambda Button: self.r_click1(self.buttons[keys])
        
        #open the tile if we left click on it.
	def l_click1(self,button):
			if(button[1]==1):
				for keys in self.buttons:
					if (self.buttons[keys][1]!=1 and self.buttons[keys][2]==2):
						self.buttons[keys][0].configure(image=self.tile_wrong)
					if (self.buttons[keys][1]==1 and self.buttons[keys][2]!=2):
						self.buttons[keys][0].configure(image=self.tile_mine)
				self.end()
			else:
				if (button[5]==0):
					button[0].configure(image=self.tile_clicked)
					self.cln_emp_tile1(button[3])
				else:
					button[0].configure(image=self.tile_no[button[5]-1])
				if (button[2]!=1):
					button[2]=1
				self.clicked=self.clicked+1
				

        #plants flag if once right clicked and removes it if clicked once again.
	def r_click1(self,button):
		if (button[2]==0):
			button[0].configure(image=self.tile_flag)
			button[2]=2
			button[0].unbind("<Button-1>")
			self.flags=self.flags+1
			self.update_flag()
			if(button[1]==1):
				self.p=self.p+1
			if(self.p==self.q and self.p==self.flags):
				self.win()
			
		elif (button[2]==2):
			button[0].configure(image=self.tile_plain)
			button[2]=0
			button[0].bind("<Button-1>",self.lclick1(button[3]))
			self.flags=self.flags-1
			self.update_flag()
			if(button[1]==1):
				self.p=self.p-1
	
        #This function opens all the empty tiles near a tile.
	def cln_emp_tile1(self,button_num):
			button_list=[button_num]
			while (len(button_list)!=0):
				keys=button_list.pop()
				x_crd=self.buttons[keys][4][0]
				y_crd=self.buttons[keys][4][1]			
				if (keys==0):
					self.check(keys+1,button_list)
					self.check(keys+8,button_list)
					self.check(keys+9,button_list)				
				elif(keys==7):
					self.check(keys-1,button_list)
					self.check(keys+8,button_list)
					self.check(keys+7,button_list)
				elif(keys==56):
					self.check(keys-8,button_list)
					self.check(keys-7,button_list)
					self.check(keys+1,button_list)
				elif(keys==63):
					self.check(keys-9,button_list)
					self.check(keys-8,button_list)
					self.check(keys-1,button_list)
				elif(x_crd==1):
					self.check(keys-1,button_list)
					self.check(keys+1,button_list)
					self.check(keys+9,button_list)
					self.check(keys+8,button_list)
					self.check(keys+7,button_list)
				elif(y_crd==0):
					self.check(keys-8,button_list)
					self.check(keys-7,button_list)
					self.check(keys+1,button_list)
					self.check(keys+8,button_list)
					self.check(keys+9,button_list)
				elif(x_crd==8):
					self.check(keys-9,button_list)
					self.check(keys-8,button_list)
					self.check(keys-7,button_list)
					self.check(keys-1,button_list)
					self.check(keys+1,button_list)
				elif(y_crd==7):
					self.check(keys-9,button_list)
					self.check(keys-8,button_list)
					self.check(keys-1,button_list)
					self.check(keys+7,button_list)
					self.check(keys+8,button_list)
				else:
					self.check(keys-7,button_list)
					self.check(keys-8,button_list)
					self.check(keys-9,button_list)
					self.check(keys-1,button_list)
					self.check(keys+1,button_list)
					self.check(keys+9,button_list)
					self.check(keys+8,button_list)
					self.check(keys+7,button_list)

	def check(self,keys,button_list):
		try:
			if(self.buttons[keys][2]==0):
				if(self.buttons[keys][5]==0):
					self.buttons[keys][0].configure(image=self.tile_clicked)
					button_list.append(keys)
				else:
					self.buttons[keys][0].configure(image=self.tile_no[self.buttons[keys][5]-1])
				self.buttons[keys][2]=1
				self.clicked=self.clicked+1
		except KeyError:
			pass
	

