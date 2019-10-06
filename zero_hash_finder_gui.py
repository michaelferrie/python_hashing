from tkinter import *
import hashlib
import random
input_String = ''
def click():
    entered_text=text_entry.get()
    output_data.delete(0.0, END)
    resulting_input = entered_text
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?-+=@#&*"
    random_char = random.choice(chars)
    input_string = entered_text
    new_guess = input_string + random.choice(chars)
    #to find more zeros change this number
    first_four = new_guess[:2]
    while first_four[:2] != ("00"):
        #and this string
        new_guess += random.choice(chars)
        result = hashlib.md5(new_guess.encode())
        output_hash = (result.hexdigest())
        #and this number
        first_four = (output_hash)[:2]
        print (new_guess)
        print (output_hash)
    output_data.insert(END, "Padding random data to:    ")
    output_data.insert(END, input_string)
    output_data.insert(END, "-    ")
    output_data.insert(END, new_guess)
    output_data.insert(END, "   The first hash starting with zeros found : ")
    output_data.insert(END, output_hash)
app = Tk()
app.title("Hashlib Zero Finder")
Label (app, text="Enter the input value for hashing, HINT! try Hello World: ").grid(row=1,column=1)
text_entry = Entry(app, width=20)
text_entry.grid(row=2,column=1)
Button(app, text="GO",width=3,command=click).grid(row=3,column=1)
output_data = Text(app, width=75, height=6, wrap=WORD)
output_data.grid(row=4,column=1)
app.mainloop()
