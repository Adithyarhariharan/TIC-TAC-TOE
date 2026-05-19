from tkinter import *

# window
root = Tk()
root.title("Tic Tac Toe")
root.geometry("320x400")
root.config(bg="lightblue")

# data structures
board = [""] * 9          # List
buttons = {}              # Dictionary
wins = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]                         # Tuple list

player = "X"

# check winner
def check_win(p):
    for a,b,c in wins:
        if board[a] == board[b] == board[c] == p:
            return True
    return False

# button click
def play(i):
    global player

    if board[i] == "":

        board[i] = player
        buttons[i]["text"] = player

        if check_win(player):
            status.config(text=f"🎉 Player {player} Wins!")
            return

        elif "" not in board:
            status.config(text="😄 Draw!")
            return

        player = "O" if player == "X" else "X"
        status.config(text=f"Player {player}'s Turn")

# restart game
def restart():
    global player
    player = "X"

    for i in range(9):
        board[i] = ""
        buttons[i]["text"] = " "

    status.config(text="Player X's Turn")

# title
Label(root,
      text="Tic Tac Toe",
      font=("Arial",20,"bold"),
      bg="lightblue").pack(pady=10)

# game frame
frame = Frame(root, bg="lightblue")
frame.pack()

# buttons using loop
for i in range(9):

    btn = Button(
        frame,
        text=" ",
        width=6,
        height=3,
        font=("Arial",20,"bold"),
        bg="white",
        command=lambda i=i: play(i)
    )

    btn.grid(row=i//3, column=i%3, padx=5, pady=5)

    buttons[i] = btn

# status label
status = Label(root,
               text="Player X's Turn",
               font=("Arial",14),
               bg="lightblue")

status.pack(pady=10)

# restart button
Button(root,
       text="Restart",
       font=("Arial",12,"bold"),
       bg="white",
       command=restart).pack()

root.mainloop()