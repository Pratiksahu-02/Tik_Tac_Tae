from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        buttons[row][column]["text"] = player

        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            Label.config(text=(player + " turn"))
        elif check_winner() is True:
            Label.config(text=(player + " wins!"))
        elif check_winner() == "Tie":
            Label.config(text="Tie!")

def check_winner():
    # Check rows
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="red")
            buttons[row][1].config(bg="red")
            buttons[row][2].config(bg="red")
            return True

    # Check columns
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="blue")
            buttons[1][column].config(bg="blue")
            buttons[2][column].config(bg="blue")
            return True

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][2].config(bg="blue")
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][0].config(bg="blue")
        return True

    # Check for tie
    if not empty_spaces():
        return "Tie!"

    return False

def empty_spaces():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                return True
    return False

def new_game():
    global player
    player = random.choice(players)
    Label.config(text=player + " turn")

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="lightblue")

# Create the main window
window = Tk()
window.title("Tic Tac Toe")
players = ["X", "O"]
player = random.choice(players)

# Create a label to display the current player's turn
Label = Label(text=player + " turn", font=("Consolas", 40))
Label.pack(side="top")

# Create a reset button
reset_button = Button(text="Restart", font=("Consolas", 20), command=new_game)
reset_button.pack(side="top")

# Create a frame for the buttons
frame = Frame(window)
frame.pack()

# Create the buttons for the Tic Tac Toe grid
buttons = [[Button(frame, text="", font=("Consolas", 40), width=5, height=2,
                   command=lambda row=row, column=column: next_turn(row, column))
            for column in range(3)] for row in range(3)]

for row in range(3):
    for column in range(3):
        buttons[row][column].grid(row=row, column=column)

# Start the main loop
new_game()  # Initialize the game
window.mainloop()