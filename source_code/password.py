import tkinter as tk
from tkinter import Button, Entry, Label, Text, Tk, ttk
from tkinter.constants import END


def write_file(filename, content, method):
    try:
        with open(filename, method) as file:
            file.write(content)
        file.close()
    except:
        pass


def read_file(filename):
    try:
        with open(str(filename), "r") as file:
            return str(file.read())
    except:
        pass


def encrypt_data(data):
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    fernet = Fernet(key)
    enc_message = fernet.encrypt(data.encode())
    print(enc_message)
    # decMessage = fernet.decrypt(encMessage).decode()
    # print("decrypted string: ", decMessage)


def display_passwords():
    show_pass_window = Tk()
    show_pass_window.title("saved passwords")
    show_pass_window.geometry("300x400")
    show_pass_window.minsize(300, 400)
    show_pass_window.maxsize(300, 400)

    output = tk.Text(show_pass_window, width=36, height=30)
    output.place(y=1, x=1)

    output.insert(END, read_file('data.txt'))

def forget_password():
    forget_password_window = Tk()
    forget_password_window.title("Reset Passwords")
    forget_password_window.geometry("300x200")
    forget_password_window.minsize(300, 200)
    forget_password_window.maxsize(300, 200)
    tk.Label(forget_password_window,text="Enter pet name : ").place(x=1,y=10)
    recovery_pet_name=ttk.Entry(forget_password_window)
    recovery_pet_name.place(x=90,y=10)
    button_var=ttk.Button(forget_password_window,text="Enter",command=show_current_pass)
    button_var.place(x=220,y=10)

def show_current_pass():pass

def write_password_to_file():

    if password.get() != '':
        write_file("data.txt", str(tag.get())+'\n', "a")
        tag.delete(0, END)
        write_file("data.txt", str(username.get())+'\n', "a")
        username.delete(0, END)
        write_file("data.txt", str(password.get())+'\n', "a")
        password.delete(0, END)


def cheak_acess_key():
    if AccessKey.get() == read_file('key.txt'):
        AccessKey.delete(0, END)
        display_passwords()
    elif read_file('key.txt') != '':
        AccessKey.delete(0, END)
        ttk.Label(main, text="wrong access key",
                  foreground='red').place(y=180, x=100)
        button_var = Button(main, text="Forget Password", height=1,
                            borderwidth=0, fg="blue", font=('Helvetica 9 underline'),command=forget_password)
        button_var.place(x=0, y=120)


def set_new_acess_key(): 
    if old_pass.get() == read_file("key.txt"):
        if new_pass.get() == conf_pass.get():
            write_file("key.txt", str(conf_pass.get())+'\n', "w")
            write_file("key.txt", PasswordRecovertAnswer.get(), "a")
            ttk.Label(settings, text="Password Set",foreground='green').place(y=170, x=100)
            try:PasswordSetUp.destroy()
            except:pass
        else:Label(settings, text="password doesnt match",foreground='red').place(y=140, x=30)
    else:Label(settings, text="old key is wrong",foreground='red').place(y=140, x=30)
    old_pass.delete(0, END)
    new_pass.delete(0, END)
    conf_pass.delete(0, END)
    try:PasswordRecovertAnswer.delete(0, END)
    except:pass


def change():
    root.select(settings)


if __name__ == "__main__":

    root = tk.Tk()

    root.title("Password saver")

    try:root.iconbitmap('.\icon.ico')
    except:pass

    root.geometry("300x230")
    root.minsize(300, 230)
    root.maxsize(300, 230)

    root = ttk.Notebook(root)
    root.pack(expand=True)

    main = tk.Frame(root, width=400, height=500, border=0)
    settings = ttk.Frame(root, width=400, height=500)

    main.place(x=1, y=1)
    settings.place(x=1, y=1)

    root.add(main, text='Main page')
    root.add(settings, text='settings')

#####################-main page-################################

    ttk.Label(main, text="TAG : ").place(y=10, x=1)
    tag = ttk.Entry(main)
    tag.place(y=10, x=150)

    ttk.Label(main, text="USERNAME : ").place(y=40, x=1)
    username = ttk.Entry(main)
    username.place(y=40, x=150)

    ttk.Label(main, text="PASSWORD :").place(y=70, x=1)
    password = ttk.Entry(main, show='*')
    password.place(y=70, x=150)

    ttk.Label(main, text="ACCESS KEY :").place(y=100, x=1)
    AccessKey = ttk.Entry(main, show='*')
    AccessKey.place(y=100, x=150)

    button_var = ttk.Button(main, text="submit",command=write_password_to_file)
    button_var.place(x=50, y=150)

    button_var = ttk.Button(main, text="show password",command=cheak_acess_key)
    button_var.place(x=140, y=150)

#####################-settings-###############################

    old_pass = ttk.Entry(settings, show="*")
    if read_file("key.txt") != "":
        ttk.Label(settings, text="OLD PASS : ").place(y=10, x=1)
        old_pass.place(y=10, x=150)

    ttk.Label(settings, text="NEW PASSWORD : ").place(y=40, x=1)
    new_pass = ttk.Entry(settings, show="*")
    new_pass.place(y=40, x=150)

    ttk.Label(settings, text="CONFIRM PASSWORD : ").place(y=70, x=1)
    conf_pass = ttk.Entry(settings, show="*")
    conf_pass.place(y=70, x=150)

    if read_file("key.txt") == '':
        PasswordSetUp = ttk.Button(main, text="Set Up The Access Key", command=change, width=50)
        PasswordSetUp.place(y=100, x=0)
        ttk.Label(settings, text="Petname (recovery) : ").place(y=110, x=1)
        PasswordRecovertAnswer = ttk.Entry(settings)
        PasswordRecovertAnswer.place(y=110, x=150)

    button_var = ttk.Button(settings, text="change access password",command=set_new_acess_key)
    button_var.place(x=140, y=170)
    root.mainloop()
