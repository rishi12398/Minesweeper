from level1 import Minesweeper
from level2 import Minesweeper2
from Tkinter import *
import tkMessageBox
import random
import time

#This function shows the rules of the game.
def instruction():
    tkMessageBox.showinfo("Instructions","The rules in Minesweeper are simple: Uncover a mine, and the game ends.Uncover an empty square, and you keep playing. Uncover a number, and it tells you how many mines lay hidden in the eight surrounding squares-information you use to deduce which nearby squares are safe to click.")

class minesweeper(Minesweeper2,Minesweeper):  #This class shows the player the levels he can choose to play.
    def __init__(self,master):
        self.apple=0
        self.frame=Frame(root)
        self.frame.grid()
        self.buttons={}
        self.tile_plain=PhotoImage(file="tile_plain.gif")
        self.tile_clicked=PhotoImage(file="tile_clicked.gif")
        self.tile_mine=PhotoImage(file="tile_mine.gif")
        self.tile_flag=PhotoImage(file="tile_flag.gif")
        self.tile_wrong=PhotoImage(file="tile_wrong.gif")
        self.tile_no=[]
        self.pic=PhotoImage(file="start.gif")
        self.label_photo=Label(self.frame,image=self.pic)
        self.label_photo.grid(row=1,column=0,columnspan=30)

        for x in range(1,9):
            self.tile_no.append(PhotoImage(file="tile_"+str(x)+".gif"))

            
        self.label_minesweeper=Label(self.frame,text="Minesweeper")    #Displays Title of the game.
        self.label_minesweeper.grid(row=0,column=10,columnspan=10)


        self.story_button=Button(self.frame,text="Story Mode",bg="red",fg="white")      #Displays Story Mode button.
        self.story_button.grid(row=2,column=20,columnspan=10)
        self.story_button.bind("<Button-1>",lambda Button:self.lll2())


        self.normal_button=Button(self.frame,text="Normal Mode",bg="green",fg="white")      #Displays Normal Mode button.
        self.normal_button.grid(row=2,column=10,columnspan=10)
        self.normal_button.bind("<Button-1>",lambda Button:self.lll())
           
        self.Inst_button=Button(self.frame,text="Instruction",command = instruction,bg="blue",fg="white")   #Displays Instructions button.
        self.Inst_button.grid(row=2,column=0,columnspan=10)

    def lll(self):
        self.frame.grid_forget()
        self.label_minesweeper.grid_forget()
        self.story_button.grid_forget()
        self.normal_button.grid_forget()
        self.frame=Frame(root)
        self.frame.grid()
        self.pic=PhotoImage(file="normal.gif")
        self.label_photo=Label(self.frame,image=self.pic)
        self.label_photo.grid(row=0,column=0,columnspan=30)
        self.level1_button=Button(self.frame,text="Level 1",bg="orange",fg="white")      #Displays level1 button.
        self.level1_button.grid(row=1,column=0,columnspan=15)
        self.level1_button.bind("<Button-1>",lambda Button:self.level1())

        self.level2_button=Button(self.frame,text="Level 2",bg="orange",fg="white")       #Displays level2 button.
        self.level2_button.grid(row=1,column=15,columnspan=15)
        self.level2_button.bind("<Button-1>",lambda Button:self.level2())
           
        
        
    def level1(self): #Forgets everything and opens 8 by 8 game 
        self.frame.grid_forget()
        self.label_minesweeper.grid_forget()
        self.level1_button.grid_forget()
        self.level2_button.grid_forget()
        self.Inst_button.grid_forget()
        global root
        Minesweeper.__init__(self,root)
            
    def level2(self):         #Forgets everything and opens 16 by 16 game 

        self.frame.grid_forget()
        self.label_minesweeper.grid_forget()
        self.level1_button.grid_forget()
        self.level2_button.grid_forget()
        self.Inst_button.grid_forget()
        global root
        Minesweeper2.__init__(self,root)
            
    def lll2(self): #forgets everything and starts story mode
        self.frame.grid_forget()
        self.label_minesweeper.grid_forget()
        self.story_button.grid_forget()
        self.normal_button.grid_forget()
        self.frame=Frame(root,height=400,width=400)
        self.frame.grid()
        self.pic=PhotoImage(file="story.gif")
        self.label_photo=Label(self.frame,image=self.pic)
        self.label_photo.grid(row=0,column=0,columnspan=30)
        tkMessageBox.showinfo("Top Secret","RAW needs to infiltrate the mine infested camp and obtain the required documents.Think you are up to it?")
        self.level1_button=Button(self.frame,text="Start Infiltration",bg="black",fg="white")     #Displays Start button.
        self.level1_button.grid(row=1,column=0,columnspan=30)
        self.level1_button.bind("<Button-1>",lambda Button:self.level12())

   
    def level12(self): #Forgets everything and opens 8 by 8 game 
        self.frame.grid_forget()
        self.label_minesweeper.grid_forget()
        self.level1_button.grid_forget()
        self.Inst_button.grid_forget()
        global root
        Minesweeper.__init__(self,root)
        self.apple=1
    def end(self):
        if(self.apple==0):
            playagain=tkMessageBox.askquestion("Game over!", "You Lose! Do you want to play again?")
            global root
            if(playagain == 'yes'): #if player wants to play again then it returns to the main window or else it destroys the window.
                self.forgetframe()
                self.__init__(self)
            else:
                sure = tkMessageBox.askquestion("Game over!","Are you sure you want to exit?")
                if(sure == 'yes'): 
                    tkMessageBox.showinfo("Made By:","1.Rishikesh Chaumal\n2.Sagar Kumar\n3.Sarat Chandra")         
                    root.destroy()
                else:
                    self.forgetframe()
                    self.__init__(self)
        else:
            playagain=tkMessageBox.askquestion("Mission Failed","You just got wasted.Try again.")
            global root
            if(playagain == 'yes'): #if player wants to play again then it returns to the main window or else it destroys the window.
                self.forgetframe()
                self.__init__(self)
            else:
                sure = tkMessageBox.askquestion("Game Over!!","Are you sure you want to exit?")
                if(sure == 'yes'): 
                    tkMessageBox.showinfo("Made By:","1.Rishikesh Chaumal\n2.Sagar Kumar\n3.Sarat Chandra")         
                    root.destroy()
                else:
                    self.forgetframe()
                    self.__init__(self)


        
    def win(self):
        if(self.apple==0):
            playagain = tkMessageBox.askquestion("Game over!","You Won! Do you want to play again?")
            global root
            if(playagain == 'yes'):    #if player wants to play again then it returns to the main window or else it destroys the window.
                self.forgetframe()
                self.__init__(self)
            else:
                sure = tkMessageBox.askquestion("Game over!","Are you sure you want to exit?")
            if(sure =='yes'): 
                tkMessageBox.showinfo("Made By:","1.Rishikesh Chaumal\n2.Sagar Kumar\n3.Sarat Chandra")        
                root.destroy()
            else:
                self.forgetframe()
                self.__init__(self)
        else:
            playagain = tkMessageBox.askquestion("Game over!","Congratulations!! You just secured some of the most important documents for RAW!!")
            global root
            if(playagain == 'yes'):    #if player wants to play again then it returns to the main window or else it destroys the window.
                self.forgetframe()
                self.__init__(self)
            else:
                sure = tkMessageBox.askquestion("Game over!","Are you sure you want to exit!?")
            if(sure =='yes'): 
                tkMessageBox.showinfo("Made By:","1.Rishikesh Chaumal\n2.Sagar Kumar\n3.Sarat Chandra")        
                root.destroy()
            else:
                self.forgetframe()
                self.__init__(self)

            
    def update_flag(self):   # This function updates the flags count.
        self.label3.configure(text="Flags: "+str(self.flags))
     
if __name__=="__main__":
    global root
    root=Tk()
    root.title("Minesweeper")
    #root.iconbitmap('unnamed.ico')			#works only on windows
    mine=minesweeper(root)
    root.mainloop()

