from tkinter import *
import time
import math
purple = "#8F87F1"
green = "#3F7D58"
red ="#7D0A0A"
count = 5
reps = 5
work_min = 25
short_brake_min = 5
long_brake_min = 20
timer = 0

def restart_timer():
    win.after_cancel(timer)
    canvas.itemconfig(timer_setting, text="00:00")
    title_lab.config(text="Timer")
    chake_mark.config(text="")
    global reps
    reps = 0
def start_timer():
    global reps
    reps += 1

    work_sec = work_min * 60
    short_brake_sec = short_brake_min * 60
    long_brake_sec = long_brake_min * 60

    if reps % 8 == 0:
        count_down(long_brake_sec)
        title_lab.config(text="Break", fg=red)
    elif reps % 2 == 0:
        count_down(short_brake_sec)
        title_lab.config(text="Break", fg=red)
    else:
        count_down(work_sec)
        title_lab.config(text="Break", fg=green)
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_setting, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = win.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        work_stations = math.floor(reps/2)
        for _ in range(work_stations):
            marks += "✔"
        chake_mark.config(text=marks)
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
restart_button = Button(text="Restart", highlightthickness=0, command=restart_timer)
restart_button.grid(column=2, row=2)
chake_mark = Label(text="✔", bg=purple, fg=green)
chake_mark.grid(column=1, row=3)


win.mainloop()