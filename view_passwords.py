import tkinter as tk
from tkinter import messagebox
import customtkinter
from customtkinter import CTkToplevel
import json

MAIN_FONT = "Ubuntu"
LEFT_BG_COLOR = "#08303b"
RIGHT_BG_COLOR = "#042430"
BTN_FG_COLOR = "#0c526b"
BTN_TXT_COLOR = "White"
MAIN_FONT_SIZE = 22
SECOND_FONT_SIZE = 12

class ViewPasswordWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("View Passwords")
        self.geometry("800x600")
        self.configure(fg_color="#042430")

        # Load the saved passwords from data.json
        with open('data.json', mode='r') as data_file:
            data = json.load(data_file)

        # -------Left Pane--------------------

        # Frame
        left_pane = tk.Frame(self)
        left_pane.place(x=0, y=0, width=300, height=600)
        left_pane.configure(bg=LEFT_BG_COLOR)

        canvas = tk.Canvas(left_pane, width=100, height=100, highlightthickness=0, background=LEFT_BG_COLOR)
        password_logo = tk.PhotoImage(file="icons8-password-100.png")
        canvas.create_image(50, 50, image=password_logo)
        canvas.place(x=75, y=25)

        self.label = customtkinter.CTkLabel(left_pane, text="View Passwords", font=("Ubuntu", 22), text_color="White")
        self.label.place(x=50, y=30)

        self.button = customtkinter.CTkButton(left_pane, text="← Back", fg_color="#0c526b", text_color="White", width=80,
                                              command=self.back_button_clicked)
        self.button.place(x=50, y=80)

        self.label = customtkinter.CTkLabel(left_pane, text="Latest Passwords", font=("Ubuntu", 15, "underline"), text_color="White")
        self.label.place(x=50, y=150)

        # Display the passwords using labels or other widgets
        y_coordinate = 190  # Starting y-coordinate for the labels
        count = 0  # Counter for the number of entries displayed
        for website, info in reversed(data.items()):  # Iterate in reverse order to get the latest entries
            if count >= 10:  # Stop after displaying 10 entries
                break
            website_title = website.title()  # Convert the website to title case
            website_label = customtkinter.CTkButton(left_pane, text=website_title, fg_color=RIGHT_BG_COLOR, text_color="White")
            website_label.place(x=50, y=y_coordinate)
            y_coordinate += 30  # Increase the y-coordinate for the next label
            count += 1

    def back_button_clicked(self):
        self.destroy()  # Close the view password window and return to the main window

