import tkinter as tk
from tkinter import messagebox
import random


a = random.randint(1, 10)
def game():
    guess = input.get()
    if int(guess) == int(a):
        result.config(text="Всё правильно! Ты угадал!", fg="green")
    else:
        result.config(text="Ты НЕ угадал! Попробуй ещё раз", fg="red")

def new_game():
    global a
    a = random.randint(1, 10)
    result.config(text=" ", fg="black")




app = tk.Tk()


app.title("Угадай число :3")
app.geometry("800x600")

label = tk.Label(app, text="Привееет! Угадай число от 1 до 10!", font=("Arial", 25))
label.pack(pady=10)

input = tk.Entry(app)
input.pack()

button = tk.Button(app, text="Проверить", font=("Arial", 20), command=game)
button.pack(pady=5)

result = tk.Label(app, text="(⁄⁄•⁄ω⁄•⁄⁄)", font=("Arial", 23))
result.pack()

new_game_btn = tk.Button(app, text="Новая игра!", font=("Arial", 23), command=new_game)
new_game_btn.pack()

label = tk.Label(app, text=":D", font=("Arial", 200))
label.pack(pady=10)

app.mainloop()