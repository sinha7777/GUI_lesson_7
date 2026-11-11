from tkinter import *
import random
import tkinter.font as font

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("600x500")

player_score = 0
computer_score = 0

options = [("rock",0),("paper",1),("scissors",2)]

def computer_wins():
    global player_score
    global computer_score
    computer_score +=1
    label_2.config(text="Computer Won!")
    label_8.config(text="Computer Score:-"+ str(computer_score))
    label_7.config(text="Your Score:-"+str(player_score))

def player_wins():
    global player_score
    global computer_score
    player_score +=1
    label_2.config(text = "You Won!")
    label_7.config(text="Your Score:-"+str(player_score))
    label_8.config(text="Computer Score:-"+str(computer_score))

def tie():
    global player_score
    global computer_score
    label_2.config(text = "Tie!")
    label_8.config(text="Computer Score:-"+str(computer_score))
    label_7.config(text="Your Score:-"+str(player_score))

def get_computer_choice():
    return random.choice(options)
    

label_1 = Label(root,text="Rock Paper Scissors",font= font.Font(size = 20),fg = "Grey")
label_1.pack(pady=10)

label_2 = Label(root,text="Let's Start the Game....",fg="Green",font=font.Font(size=15))
label_2.pack(pady=10)

frame = Frame(root)
frame.pack()

label_3 = Label(frame,text="Your Options:",fg="grey",font=font.Font(size = 15))
label_3.grid(row=0,column=0,pady=10)

btn_1 = Button(frame,text="Rock",bg="light pink")
btn_1.grid(row=1,column=1,padx=8,pady=5)

btn_2 = Button(frame,text = "Paper", bg = "grey")
btn_2.grid(row=1,column=2,padx=8,pady=5)

btn_3 = Button(frame,text="Scissors",bg="light blue")
btn_3.grid(row=1,column=3,padx=8,pady=5)

label_4 = Label(frame,text="Score:",fg = "grey",font=font.Font(size = 15))
label_4.grid(row=2,column=0,pady=10)

label_5 = Label(frame,text="You selected:-",font=font.Font(size = 12))
label_5.grid(row=3,column=1,pady=10,padx=10)

label_6 = Label(frame,text="Computer Selected:-",font = font.Font(size = 12))
label_6.grid(row=3,column=2,pady=10,padx=10)

label_7 = Label(frame,text="Your score:-",font = font.Font(size = 12))
label_7.grid(row=4,column=1,pady=10,padx=10)

label_8 = Label(frame,text="Computer Score:-",font=font.Font(size = 12))
label_8.grid(row=4,column=2,pady=10,padx=10)


root.mainloop()