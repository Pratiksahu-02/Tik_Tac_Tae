from tkinter import *
import random

def next_turn(row,column):
    global player
    if buttons[row][column]["text"]=="" and check_winner() is False:
        if player==players[0]:
            buttons[row][column]["text"]=player

            if check_winner() is False:
                player=players[1]
                Label.config(text=(players[1]+"turn"))

            elif check_winner() is TRUE:
                Label.config(text=(players[0]+"wins"))
            
            elif check_winner()=="Tie":
                Label.config(text="Tie!")
    else:
        buttons[row][column]["text"]=player

        if check_winner() is False:
            player=players[0]
            Label.config(text=(players[1]+"turn"))

        elif check_winner() is TRUE:
            Label.config(text=(players[1]+"wins"))
            
        elif check_winner()=="Tie":
            Label.config(text="Tie!")


def check_winner():
    
    for row in range(3):
        if buttons[row][0]["text"]==buttons[row][1]["text"]==buttons[row][2]["text"]!="":
            buttons[row][0].config(bg="red")
            buttons[row][1].config(bg="red")
            buttons[row][2].config(bg="red")
            return True
    
    for column in range(3):
        if buttons[column][0]["text"]==buttons[column][1]["text"]==buttons[column][2]["text"]!="":
            buttons[0][column].config(bg="blue")
            buttons[1][column].config(bg="blue")
            buttons[2][column].config(bg="blue")
            return True
    
    if buttons[0][0]["text"]==buttons[1][1]["text"]==buttons[1][1]["text"]!="":
        buttons[0][0].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][2].config(bg="blue")
        return True
    
    elif buttons[0][2]["text"]==buttons[1][1]["text"]==buttons[2][0]["text"]!="":
        buttons[0][2].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][0].config(bg="blue")
        return True
    
    elif empty_spaces() is False:
        return "Tie!"
    
    else :
        return False


def empty_spaces():
    spaces=9
    for i in range (3):
        for j in range(3):
           if buttons[i][j]["text"]!="":
            spaces -=1
    if spaces==0:
        return False
    else:
        return True

def new_game():
    global player
    player=random.choice(players)
    Label.config(text=player+"turn")

    for i in range (3):
        for j in range(3):
            buttons[i][j].config(text="",bg="lightblue")

window=Tk()
window.title("T-t-t")
players=["x","o"]
player=random.choice(players)
buttons=[[0,0,0],
        [0,0,0],
        [0,0,0]]
Label=Label(text=player + " turn",font=("consoles",40))
Label.pack(side="top")

reset_button=Button(text="restart",font=("consoles",20),command=new_game)
reset_button.pack(side="top")

frame=Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame,text="",font=("consoles",40),width=5,height=2,
                                    command=lambda row=row,column=column:next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
    

window.mainloop()