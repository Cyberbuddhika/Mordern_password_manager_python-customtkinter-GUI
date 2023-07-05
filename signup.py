import tkinter as tk
from tkinter import messagebox
import customtkinter
from customtkinter import CTkToplevel
import json
from login import ViewLoginWindow
import bcrypt


MAIN_FONT = "Ubuntu"
LEFT_BG_COLOR = "#08303b"
RIGHT_BG_COLOR = "#042430"
BTN_FG_COLOR = "#0c526b"
BTN_TXT_COLOR = "White"
MAIN_FONT_SIZE = 22
SECOND_FONT_SIZE = 12


class ViewSignupWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("View Passwords")
        self.geometry("400x500")
        self.configure(fg_color="#042430")

        # Create a Canvas widget
        self.canvas = tk.Canvas(self, width=100, height=100, background="#042430", highlightthickness=0)
        self.canvas.place(x=150, y=20)

        # Load and display an image on the canvas
        self.image = tk.PhotoImage(file="icons8-password-100.png")
        self.canvas.create_image(0, 0, anchor="nw", image=self.image)

        self.label = customtkinter.CTkLabel(self, text="Welcome", font=("Ubuntu", 22), text_color="White")
        self.label.place(x=150, y=130)


        # Function to toggle the visibility of the password entry field
        def toggle_password_visibility():
            if password_entry.cget("show") == "*":
                password_entry.configure(show="")
            else:
                password_entry.configure(show="*")

        def clearing_password():
            user_name_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)

        def sing_up():
            login_name = user_name_entry.get()
            master_password = password_entry.get()
            encoded_password = master_password.encode("utf-8")
            hashed_pw = bcrypt.hashpw(encoded_password, bcrypt.gensalt(10)).decode("utf-8")
            email = email_entry.get()
            if len(login_name) == 0 or len(master_password) == 0 or len(email) == 0:
                messagebox.showerror("Empty Fields", "Please fill all the input fields.")
            else:
                login_data = {
                    login_name: {
                        "password": hashed_pw,
                        "email": email,
                    }
                }
                data = login_data
                print(data)
                with open('data/login.json', mode='w') as data_file:
                    json.dump(data, data_file, indent=4)
                    print(data)
                    clearing_password()
                    self.close()

        # -------Sign-up Screen--------------------

        self.label = customtkinter.CTkLabel(self, text="Let's create your Master Password.",
                                            font=("Ubuntu", SECOND_FONT_SIZE), text_color="White")
        self.label.place(x=100, y=170)

        create_account_button = customtkinter.CTkButton(self, text="Create Account",
                                                        fg_color=BTN_FG_COLOR,
                                                        text_color=BTN_TXT_COLOR, width=200,
                                                        command=sing_up)
        create_account_button.place(x=100, y=360)

        self.label = customtkinter.CTkLabel(self, text="User Name:",
                                            font=("Ubuntu", SECOND_FONT_SIZE), text_color="White")
        self.label.place(x=20, y=220)
        self.label = customtkinter.CTkLabel(self, text="Master Password:",
                                            font=("Ubuntu", SECOND_FONT_SIZE), text_color="White")
        self.label.place(x=20, y=260)
        self.label = customtkinter.CTkLabel(self, text="Your Email:",
                                            font=("Ubuntu", SECOND_FONT_SIZE), text_color="White")
        self.label.place(x=20, y=300)
        user_name_entry = customtkinter.CTkEntry(self, width=200, font=(MAIN_FONT, SECOND_FONT_SIZE))
        user_name_entry.place(x=150, y=220)
        password_entry = customtkinter.CTkEntry(self, width=200, font=(MAIN_FONT, SECOND_FONT_SIZE), show="*")
        password_entry.place(x=150, y=260)
        email_entry = customtkinter.CTkEntry(self, width=200, font=(MAIN_FONT, SECOND_FONT_SIZE))
        email_entry.place(x=150, y=300)
        show_password_button = customtkinter.CTkButton(self, text='\u29A0',
                                                       fg_color=RIGHT_BG_COLOR,
                                                       text_color=BTN_TXT_COLOR, width=5,
                                                       command=toggle_password_visibility)
        show_password_button.place(x=360, y=260)


    def close(self):
        self.destroy()  # Close the view password window and return to the main window



