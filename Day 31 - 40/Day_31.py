############### languge traling
from tkinter import *
import random
import pandas

background = "#b1ddc6"
learn= pandas.read_csv("files/french_words.csv")
to_lern = learn.to_dict(orient="records")
words = {}
def next_card():
    global words , timer
    win.after_cancel(timer)
    words =  random.choice(to_lern)
    canvas.itemconfig(title,text="French", fill="black")
    canvas.itemconfig(list, text=words["French"], fill="green")
    canvas.itemconfig(card_bg, image=image_file_bg)
    timer = win.after(3000, flip_card)
def is_known():
    to_lern.remove(words)
    data = pandas.DataFrame(to_lern)
    data.to_csv("files/new_french_words.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(list, text=words["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_bg_im)
win = Tk()
win.title("Sample")
win.config(padx=50, pady=50,bg=background)
timer = win.after(3000, flip_card)
canvas = Canvas(width=800, height=526)

image_file_bg = PhotoImage(file="files/card_front.png")
card_bg_im = PhotoImage(file="files/card_back.png")
card_bg = canvas.create_image(400, 263,image=image_file_bg)
canvas.grid(row=0, column=0,columnspan=2)
canvas.config(bg=background, highlightthickness=0)
title = canvas.create_text(400, 100,text="Title", font=("times new roman", 40 , "bold"))
list = canvas.create_text(400,200, text="Word", font=("arial", 50, "bold"))

cross_image = PhotoImage(file="files/wrong.png")
un_button = Button(image=cross_image, highlightthickness=0, command=next_card)
un_button.grid(row=1, column=0)

chake_image = PhotoImage(file="files/right.png")
chake_button = Button(image=chake_image, highlightthickness=0, command=is_known)
chake_button.grid(row=1, column=1)

next_card()
win.mainloop()