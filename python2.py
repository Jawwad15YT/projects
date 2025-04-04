import tkinter as tk
import random


choices = ["Rock", "Paper", "Scissors"]


def play(user_choice):
    computer_choice = random.choice(choices)
    result = ""
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    
    label_result.config(text=f"Computer chose: {computer_choice}\n{result}")


root = tk.Tk()
root.title("Rock Paper Scissors")

tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack()


for choice in choices:
    tk.Button(root, text=choice, command=lambda c=choice: play(c)).pack()


label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()