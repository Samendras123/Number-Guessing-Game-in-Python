import tkinter as tk 
import random


secret_num = random.randint(1, 100)
font = ("Times New Roman", 17, "bold")
bg_color = "#0b2447"

window = tk.Tk()
window.title("Number Guessing Game")
window.config(bg=bg_color)
window.geometry("400x400")

number_guess = 10

def check_number():

    global number_guess
    guess = int(entry.get())
    
    if guess == secret_num:
        result.config(text="You win the Game..", fg="#47a992")
        entry.config(state=tk.DISABLED)
        button.config(state=tk.DISABLED)
        print("You win")

    elif guess < secret_num:
        result.config(text="Too low", fg="#f00")
        print("Too low")

    else:
        result.config(text="Too high", fg="#f00")
        print("Too high")

    number_guess -= 1
    chance.config(text=f"left Chances : {number_guess}")    
       
    if number_guess == 0:
        result.config(text="You Loose the Game", fg="#f00")
        entry.config(state=tk.DISABLED)
        button.config(state=tk.DISABLED)
        



label = tk.Label(window, text="Enter a number between 1 to 100", font=font, bg=bg_color, fg="#fff")
label.pack(pady=20)

entry = tk.Entry(window, font=font)
entry.pack(pady=15)

button = tk.Button(window, text="Submit", font=font, command=check_number, activebackground=bg_color)
button.pack(padx=15)

result = tk.Label(window, text="", font = ("Times New Roman", 20, "bold"), bg=bg_color)
result.pack(pady=20)

chance = tk.Label(window, text="left Chances : 10", font=font, bg=bg_color, fg="#dde6ed")
chance.pack(pady=10)


window.mainloop()