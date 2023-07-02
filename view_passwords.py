import tkinter as tk
from tkinter import messagebox
import customtkinter
from customtkinter import CTkToplevel
import json
import pyperclip

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

        self.label = customtkinter.CTkLabel(left_pane, text="View Passwords", font=("Ubuntu", 22), text_color="White")
        self.label.place(x=50, y=30)

        self.button = customtkinter.CTkButton(left_pane, text="← Back", fg_color="#0c526b", text_color="White",
                                              width=80,
                                              command=self.back_button_clicked)
        self.button.place(x=50, y=80)

        self.label = customtkinter.CTkLabel(left_pane, text="Recent Passwords", font=("Ubuntu", 15, "underline"),
                                            text_color="White")
        self.label.place(x=50, y=150)

        def copy_to_clipboard(entry, name):
            enable_entry()
            value = entry.get()
            pyperclip.copy(value)
            disable_entry()
            messagebox.showinfo("Copied to Clipboard", f"{name} is copied to clipboard")


        def clearing_password():
            enable_entry()
            website_entry.delete(0, tk.END)
            url_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            disable_entry()

        def enable_entry():
            url_entry.configure(state="normal")
            email_entry.configure(state="normal")
            password_entry.configure(state="normal")
            url_lock_label.configure(text="🔓")
            email_lock_label.configure(text="🔓")
            password_lock_label.configure(text="🔓")

        def disable_entry():
            url_entry.configure(state="readonly")
            email_entry.configure(state="readonly")
            password_entry.configure(state="readonly")
            url_lock_label.configure(text="🔒")
            email_lock_label.configure(text="🔒")
            password_lock_label.configure(text="🔒")

        def save_password_edits():
            enable_entry()
            website_input = website_entry.get()
            url = url_entry.get()
            email = email_entry.get()
            password = password_entry.get()

            try:
                website = website_input.lower()
            except AttributeError:
                website = ""
            else:
                # Validating for empty fields
                if len(website) == 0 or len(email) == 0 or len(password) == 0:
                    messagebox.showerror("Empty Fields", "You need to find a password before editing.")
                else:
                    # Load the existing data from the JSON file
                    with open('data.json', mode='r') as data_file:
                        data = json.load(data_file)

                    # Update the specific entry in the data dictionary
                    if website in data:
                        data[website]["url"] = url
                        data[website]["email"] = email
                        data[website]["password"] = password
                        with open('data.json', mode='w') as data_file:
                            json.dump(data, data_file, indent=4)
                            clearing_password()
                            messagebox.showinfo("Password Updated Successfully",
                                                f"Password for {website} has been updated.")
                    else:
                        messagebox.showerror("Website Not Found", "The website does not exist in the data file.")

        def search_passwords(website):
            enable_entry()
            clearing_password()
            with open('data.json', mode='r') as data_file:
                data = json.load(data_file)
            if website in data:
                email = data[website]["email"]
                url = data[website]["url"]
                password = data[website]["password"]
                enable_entry()
                website_entry.insert(tk.END, website)
                url_entry.insert(tk.END, url)
                email_entry.insert(tk.END, email)
                password_entry.insert(tk.END, password)
                disable_entry()

            else:
                messagebox.showerror("No Password Found", "We couldn't find the password.\nPlease type correct name "
                                                          "for the Website Name:")

        # Display the passwords using labels or other widgets
        y_coordinate = 190  # Starting y-coordinate for the labels
        count = 0  # Counter for the number of entries displayed
        for website, info in reversed(data.items()):  # Iterate in reverse order to get the latest entries
            if count >= 10:  # Stop after displaying 10 entries
                break
            website_name = website
            website_title = website.title()  # Convert the website to title case
            website_label = customtkinter.CTkButton(left_pane, text=website_title, fg_color=RIGHT_BG_COLOR,
                                                    text_color="White", command=lambda website=website_name: search_passwords(website))
            website_label.place(x=50, y=y_coordinate)
            y_coordinate += 30  # Increase the y-coordinate for the next label
            count += 1

        # -------Right Pane--------------------

        # Frame
        right_pane = tk.Frame(self)
        right_pane.place(x=250, y=0, width=550, height=600)
        right_pane.configure(bg=RIGHT_BG_COLOR)
        # ---------------------------- SEARCH PASSWORD ------------------------------- #
        view_password_label = customtkinter.CTkLabel(right_pane, text="Passwords", fg_color="transparent",
                                                     font=(MAIN_FONT, MAIN_FONT_SIZE))
        view_password_label.place(x=250, y=30)

        # ------show password form----------------

        #  Labels
        website_name_label = customtkinter.CTkLabel(right_pane, text="Website Name:",
                                                    font=(MAIN_FONT, SECOND_FONT_SIZE))
        website_name_label.place(x=50, y=125)
        url_label = customtkinter.CTkLabel(right_pane, text="Website Address(URL):", font=(MAIN_FONT, SECOND_FONT_SIZE))
        url_label.place(x=50, y=160)
        email_label = customtkinter.CTkLabel(right_pane, text="Email/Username:", font=(MAIN_FONT, SECOND_FONT_SIZE))
        email_label.place(x=50, y=195)
        password_label = customtkinter.CTkLabel(right_pane, text="Password:", font=(MAIN_FONT, SECOND_FONT_SIZE))
        password_label.place(x=50, y=230)

        # Lock labels
        url_lock_label = customtkinter.CTkLabel(right_pane, text="🔒", font=(MAIN_FONT, SECOND_FONT_SIZE))
        url_lock_label.place(x=500, y=160)
        email_lock_label = customtkinter.CTkLabel(right_pane, text="🔒", font=(MAIN_FONT, SECOND_FONT_SIZE))
        email_lock_label.place(x=500, y=195)
        password_lock_label = customtkinter.CTkLabel(right_pane, text="🔒", font=(MAIN_FONT, SECOND_FONT_SIZE))
        password_lock_label.place(x=500, y=230)


        #  Entries
        website_entry = customtkinter.CTkEntry(right_pane, width=300, font=(MAIN_FONT, SECOND_FONT_SIZE))
        website_entry.place(x=200, y=125)
        url_entry = customtkinter.CTkEntry(right_pane, width=300, font=(MAIN_FONT, SECOND_FONT_SIZE), state="readonly")
        url_entry.place(x=200, y=160)
        email_entry = customtkinter.CTkEntry(right_pane, width=300, font=(MAIN_FONT, SECOND_FONT_SIZE), state="readonly")
        email_entry.place(x=200, y=195)
        password_entry = customtkinter.CTkEntry(right_pane, width=300, font=(MAIN_FONT, SECOND_FONT_SIZE), state="readonly")
        password_entry.place(x=200, y=230)

        #  Get input from website name
        website_name_data = website_entry.get()

        #  Buttons
        search_passwords_button = customtkinter.CTkButton(right_pane, text="Search Password",
                                                            fg_color=BTN_FG_COLOR,
                                                            text_color=BTN_TXT_COLOR, width=140,
                                                            command=lambda: search_passwords(website_entry.get())
)
        search_passwords_button.place(x=200, y=280)
        edit_passwords_button = customtkinter.CTkButton(right_pane, text="Edit Password",
                                                            fg_color=BTN_FG_COLOR,
                                                            text_color=BTN_TXT_COLOR, width=140,
                                                            command=enable_entry)
        edit_passwords_button.place(x=360, y=280)
        save_button = customtkinter.CTkButton(right_pane, text="Save", fg_color=BTN_FG_COLOR, text_color=BTN_TXT_COLOR,
                                              width=140, command=save_password_edits)
        save_button.place(x=200, y=320)
        cancel_button = customtkinter.CTkButton(right_pane, text="Cancel", fg_color=BTN_FG_COLOR,
                                                text_color=BTN_TXT_COLOR,
                                                width=140, command=clearing_password)
        cancel_button.place(x=360, y=320)

        # clipboard buttons
        url_clipboard_btn = customtkinter.CTkButton(right_pane, text="📋",
                                                    fg_color=RIGHT_BG_COLOR,
                                                    text_color=BTN_TXT_COLOR, width=15,
                                                    command=lambda: copy_to_clipboard(url_entry, "URL"))
        url_clipboard_btn.place(x=520, y=160)
        email_clipboard_btn = customtkinter.CTkButton(right_pane, text="📋",
                                                      fg_color=RIGHT_BG_COLOR,
                                                      text_color=BTN_TXT_COLOR, width=15,
                                                      command=lambda: copy_to_clipboard(email_entry, "Email"))
        email_clipboard_btn.place(x=520, y=195)
        password_clipboard_btn = customtkinter.CTkButton(right_pane, text="📋",
                                                         fg_color=RIGHT_BG_COLOR,
                                                         text_color=BTN_TXT_COLOR, width=15,
                                                         command=lambda: copy_to_clipboard(password_entry, "Password"))
        password_clipboard_btn.place(x=520, y=230)

        # Help text

        help_title_label = customtkinter.CTkLabel(right_pane, text="💡Help:", font=(MAIN_FONT, 12), text_color="White",
                                            wraplength=360, justify="left")
        help_title_label.place(x=50, y=380)

        help_text = "To view a password, select a website from the list on the left or type in the 'Website Name' " \
                    "field and click " \
                    "'Search Password' button. You can click 📋 button to copy any field to clipboard.\n\n" \
                    "To edit a password, click the 'Edit Password' button and make the necessary changes. " \
                    "Then, click the 'Save' button to update the password.\n\n" \
                    "Note:  You can only edit one password at a time.\n\n" \
                    "If you can't find a password, make sure you enter the correct website name."

        help_label = customtkinter.CTkLabel(right_pane, text=help_text, font=(MAIN_FONT, 12), text_color="White",
                                            wraplength=360, justify="left")
        help_label.place(x=125, y=380)



    def back_button_clicked(self):
        self.destroy()  # Close the view password window and return to the main window
