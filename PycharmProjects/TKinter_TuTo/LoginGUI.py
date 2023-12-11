# make a GUI for the login system that first set the username and password then check if the username and password are correct"
import tkinter as tk

class loginGUI:
    def __init__(self, master):
        self.master = master
        master.title("Login System")
        master.geometry("400x400")
        master.resizable(False, False)
        master.configure(bg="gray")

        self.username_label = tk.Label(master, text="Username:", bg="gray")
        self.username_label.pack()

        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:", bg="gray")
        self.password_label.pack()

        self.password_entry = tk.Entry(master)
        self.password_entry.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

        self.login_label = tk.Label(master, text="", bg="gray")
        self.login_label.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "Rami" and password == "1234":
            self.login_label.config(text="Login Successful", fg="green")
        else:
            self.login_label.config(text="Login Failed", fg="red")

root = tk.Tk()
login = loginGUI(root)
root.mainloop()

