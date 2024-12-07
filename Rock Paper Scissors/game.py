import tkinter as tk
import random

# Function to handle the user's choice
def user_choice(user_move):
    program_move = random.choice(["Rock", "Paper", "Scissors"])
    result.set(f"User: {user_move} | Program: {program_move}")
    
    if user_move == program_move:
        winner.set("It's a Tie!")
    elif (user_move == "Rock" and program_move == "Scissors") or \
         (user_move == "Paper" and program_move == "Rock") or \
         (user_move == "Scissors" and program_move == "Paper"):
        winner.set("You Win!")
    else:
        winner.set("You Lose!")

# Function to reset the game
def reset_game():
    result.set("")
    winner.set("")

# Creating the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Variables to store the results
result = tk.StringVar()
winner = tk.StringVar()

# Creating buttons for Rock, Paper, Scissors
rock_button = tk.Button(root, text="Rock", command=lambda: user_choice("Rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: user_choice("Paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: user_choice("Scissors"))

# Creating labels to display the choices and winner
result_label = tk.Label(root, textvariable=result)
winner_label = tk.Label(root, textvariable=winner)

# Creating a reset button
reset_button = tk.Button(root, text="Reset Game", command=reset_game)

# Placing the buttons and labels on the window
rock_button.pack()
paper_button.pack()
scissors_button.pack()
result_label.pack()
winner_label.pack()
reset_button.pack()

# Running the main loop
root.mainloop()
