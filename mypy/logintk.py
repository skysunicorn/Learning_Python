import tkinter as tk

login = tk.Tk()
login.geometry("360x240+500+240")
login.wm_attributes('-topmost', 1)

users = ['uMaxwell']
pswd_dict = {'uMaxwell': 'pwyy991010'}


def close_login(position):
    print(position)
    login.destroy()


login.bind('<Double-Button-1>', close_login)

main_title = tk.Variable()
login.title("Log in")

wel_lb = tk.Label(text="Welcome to Secret Land  ", width=24, height=1,
                  font=("Snell Roundhand", 28), fg='blue', anchor='n')
wel_lb.pack()

instruct = tk.StringVar()
instruct.set("please enter your username and password")
ins_lb = tk.Label(textvariable=instruct, width=36, height=1, anchor='n', fg='red')
ins_lb.pack()

tk.Label(login, text="Username:").place(x=30, y=84)
tk.Label(login, text="Password:").place(x=30, y=132)

user = tk.Entry()
user.place(x=124, y=84)
pswd = tk.Entry(show='*')
pswd.place(x=124, y=132)


def check_input():
    global instruct
    username = str('u' + user.get())
    password = str('p' + pswd.get())
    if username in users:
        if password == pswd_dict[username]:
            instruct.set("Identity Confirmed! Logged in successfully")
        elif password == 'p':
            instruct.set("Please do not leave your password blank")
        else:
            instruct.set("Wrong password! Try again")
    elif username == 'u':
        instruct.set("Please do not leave your username blank")
    else:
        instruct.set("Unregistered user! please sign up first")


b_con = tk.Button(text="Confirm", width=6, height=1, command=check_input)
b_con.place(x=240, y=180)


def register():
    instruct.set("Please pay 50$ and try again")



b_can = tk.Button(text="sign up", width=6, height=1, command=register)
b_can.place(x=120, y=180)

login.mainloop()
