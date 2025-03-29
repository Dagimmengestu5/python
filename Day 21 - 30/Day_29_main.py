############## password saving form


from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

def password_generater():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = [
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
        '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '"', ',', '<', '>', '.',
        '/', '?', '`', '~'
    ]

    pass_latter = [choice(letters) for _ in range(randint(8,10))]
    pass_num = [choice(number) for _ in range(randint(2,4))]
    pass_simbol = [choice(symbols) for _ in range(randint(2,4))]

    pass_list = pass_latter + pass_simbol + pass_num
    shuffle(pass_list)
    password = "".join(pass_list)
    Password_entry.insert(0, password)


def save():

    website = web_entry.get()
    email  = email_entry.get()
    password = Password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="pleas insert the box is empty")
    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"Detail enterd: \n "
                                        f"Email: {email} \n"
                                        f" Password: {password}\n is it ok to save ")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, END)
                Password_entry.delete(0, END)


win = Tk()
win.title("Password Manager")
win.config(pady=50, padx=50)
canvas = Canvas(height=200 , width=200)
log_img = PhotoImage(file="files/logo.png")
canvas.create_image(100,100,image=log_img)
canvas.grid( row=0, column=1)

# Labels
web_lable = Label(text="Website:")
web_lable.grid(column=0,row=1)
email_label = Label(text="Email/User name:")
email_label.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

# Entry
web_entry = Entry(width=35)
web_entry.grid(column=1,row=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0, "Dagimmengestu5@gmail.com")

Password_entry = Entry(width=25)
Password_entry.grid(column=1,row=3 ,columnspan=2)

# Butten
pass_gen_butten = Button(text="Generate", command=password_generater)
pass_gen_butten.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4,columnspan=2)

win.mainloop()