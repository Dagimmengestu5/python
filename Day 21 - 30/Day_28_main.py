from tkinter import *
import time
import math
purple = "#8F87F1"
green = "#3F7D58"
count = 5

# while True:
#
#     time.sleep(1)
#     count -= 1
def start_timer():
    count_down(5*60)
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_setting, text=f"{count_min}:{count_sec}")
    if count > 0:
        win.after(1000, count_down, count -1)
win = Tk()
win.title("Timer")
win.config(padx=100, pady=50, bg=purple)
title_lab = Label(text="Timer", fg=green, bg=purple, font=("times new roman",40 ))
title_lab.grid(column=1, row=0)
canvas = Canvas(width=200, height=224 , bg=purple, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_setting = canvas.create_text(103,130,text="00:00",fill="white",font=("times new roman", 30 , "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
restart_button = Button(text="Restart", highlightthickness=0)
restart_button.grid(column=2, row=2)
chake_mark = Label(text="✔", bg=purple, fg=green)
chake_mark.grid(column=1, row=3)


win.mainloop()