import random
import string
import tkinter as tk
from tkinter import *

def password_generate(length, _digit = True, _whitespaces = True, _pontuation = True):
    letters = string.ascii_letters
    digit = string.digits
    pontuantion = string.punctuation
    whitespaces = string.whitespace

    password = ""

    character = letters
    if _digit:
        character += digit
    if _whitespaces:
        character += whitespaces
    if _pontuation:
        character += pontuantion


    while len(password) < length:
        random_char = random.choice(character)
        password += random_char

    return password



# length = int(input("Put the size of te password "))
# _digit = input("The Password must have Digits? ").strip().lower() == 'y'
# _whitespaces = input("The Password must have whitespaces? ").strip().lower() == 'y'
# _pontuation = input("The Password must have pontuantion? ").strip().lower() == 'y'
#
# print(password_generate(length, _digit, _whitespaces, _pontuation))


def password_generation():
    try:
        length = int(entry_length.get())
    except ValueError:
        res.config(text="Enter a Valid number")
        return

    use_digits = __digit.get()
    use_ponctuation = __ponctuation.get()
    use_whitespaces = __whitespaces.get()


    password = password_generate(length, use_digits, use_whitespaces, use_ponctuation)
    res.config(text=password)




m = tk.Tk()
m.title("Password Generator")


__digit = BooleanVar(value=True)
__ponctuation =  BooleanVar(value=True)
__whitespaces = BooleanVar(value=True)


Label(m, text="Password Generator").grid(row=0, column=0, columnspan=2, pady=10)


Label(m, text='Put the size of te password').grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_length = Entry(m)
entry_length.grid(row = 1, column = 1, pady=5)



Checkbutton(m, text='The Password must have Digits?').grid(row=3, column=0, padx=10, pady=5, sticky='e')
Checkbutton(m, text='The Password must have whitespaces?').grid(row=5, column=0, padx=10, pady=5, sticky='e')
Checkbutton(m, text='The Password must have pontuantion?').grid(row=8, column=0, padx=10, pady=5, sticky='e')

tk.Button(m, text="Generate", width=25, command=password_generation).grid(row=10,columnspan=2, pady=15)

res = Label(m, text="", fg="blue", wraplength=3000)
res.grid(row = 6, column = 0, columnspan=2 ,pady=5)


m.mainloop()

