import tkinter as tk
from tkinter import messagebox
import customtkinter
from password_strength import password_strength
from password_generator import password_gen
import pyperclip
import json
import os.path
from cryptography.fernet import Fernet
from view_passwords import ViewPasswordWindow
from signup import ViewSignupWindow
from login import ViewLoginWindow
from info import ViewInfoWindow

# ------Setting up defaults ----------------

MAIN_FONT = "Ubuntu"
LEFT_BG_COLOR = "#08303b"
RIGHT_BG_COLOR = "#042430"
BTN_FG_COLOR = "#0c526b"
BTN_TXT_COLOR = "White"
MAIN_FONT_SIZE = 22
SECOND_FONT_SIZE = 12
user_name = ""
default_email = ""
num_of_letters = 8
num_of_symbols = 2
num_of_numbers = 2
length_of_password = 12

# Creating main app_window
app = customtkinter.CTk(fg_color="#042430")
app.geometry("800x600")
app.title("Password Manager")


# ------Open sing-up window----------------
def view_signup():
    signup_window = ViewSignupWindow(app)
    signup_window.geometry(f"+{app.winfo_x()}+{app.winfo_y()}")  # Set the coordinates for the window
    signup_window.transient(app)
    signup_window.grab_set()
    app.wait_window(signup_window)  # Wait for the signup window to close

    app.deiconify()  # Show the main window again after the signup window is closed
    view_login()


# ------Open login window----------------
def view_login():
    login_window = ViewLoginWindow(app)
    login_window.geometry(f"+{app.winfo_x()}+{app.winfo_y()}")  # Set the coordinates for the window
    login_window.transient(app)
    login_window.grab_set()
    app.wait_window(login_window)  # Wait for the login window to close

    if login_window.authenticated:
        global default_email
        global user_name
        # Read login.json file and get username and email
        with open('data/login.json') as data_file:
            data = json.load(data_file)
            login_name = list(data.keys())[0]
            default_email = data[login_name]["email"]
            user_name = login_name
        # Proceed to the main window
        # Implement your main window logic here
        print("Main window opened")
    else:
        # Exit the application if not authenticated
        app.destroy()


# -------------Login Initialization------------------------------------

if os.path.isfile("data/login.json"):
    view_login()
else:
    view_signup()


# ------Default email change----------------
def change_default_email():
    global default_email
    change_email_dialog = customtkinter.CTkInputDialog(
        text=f"Your current email is {default_email}\nPlease type your new email:", title="Change Default Email")

    new_email = change_email_dialog.get_input()  # waits for input
    if new_email:
        default_email = new_email
        email_entry.delete(0, tk.END)
        email_entry.insert(0, default_email)
    else:
        default_email = default_email
    # once we finish login page implement json to save this email


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = website_entry.get()
    url = url_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # Generate a key if not already generated
    if not os.path.exists('data/key.key'):
        key = Fernet.generate_key()
        with open('data/key.key', 'wb') as key_file:
            key_file.write(key)

    # Encrypt the password using the generated key
    with open('data/key.key', 'rb') as key_file:
        key = key_file.read()
        cipher_suite = Fernet(key)
        password = cipher_suite.encrypt(password.encode())

    # Save the password to a JSON file
    data = {
        website_input: {
            "url": url,
            "email": email,
            "password": password.decode()
        }
    }
    with open('passwords.json', 'r+') as file:
        # Load the existing data
        try:
            existing_data = json.load(file)
        except json.JSONDecodeError:
            existing_data = {}
        # Update the existing data with new data
        existing_data.update(data)
        # Move the file pointer to the beginning of the file
        file.seek(0)
        # Write the updated data to the file
        json.dump(existing_data, file, indent=4)
        # Truncate the file to remove any remaining content
        file.truncate()

    # Clear the input fields
    website_entry.delete(0, tk.END)
    url_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    # Show a success message box
    messagebox.showinfo(title="Password Saved", message="Your password has been saved.")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website_input = website_entry.get()
    with open('passwords.json', 'r') as file:
        data = json.load(file)
        if website_input in data:
            password = data[website_input]['password']
            # Decrypt the password using the key
            with open('data/key.key', 'rb') as key_file:
                key = key_file.read()
                cipher_suite = Fernet(key)
                decrypted_password = cipher_suite.decrypt(password.encode())
            pyperclip.copy(decrypted_password.decode())
            messagebox.showinfo(title="Password Found", message="The password has been copied to the clipboard.")
        else:
            messagebox.showinfo(title="Password Not Found", message="No password found for the website.")


# ---------------------------- UI SETUP ------------------------------- #
# Create frames
left_frame = customtkinter.CTkFrame(app, bg_color=LEFT_BG_COLOR)
left_frame.grid(row=0, column=0, padx=50, pady=50)

right_frame = customtkinter.CTkFrame(app, bg_color=RIGHT_BG_COLOR)
right_frame.grid(row=0, column=1, padx=50, pady=50)

# Left Frame
website_label = customtkinter.CTkLabel(left_frame, text="Website:", bg_color=LEFT_BG_COLOR, fg_color=BTN_TXT_COLOR,
                                      font=(MAIN_FONT, MAIN_FONT_SIZE))
website_label.grid(row=0, column=0, pady=(0, 10))
website_entry = customtkinter.CTkEntry(left_frame, width=30)
website_entry.grid(row=1, column=0, pady=(0, 20))

search_button = customtkinter.CTkButton(left_frame, text="Search", bg_color=BTN_FG_COLOR, fg_color=BTN_TXT_COLOR,
                                       font=(MAIN_FONT, SECOND_FONT_SIZE), command=search_password)
search_button.grid(row=2, column=0)

# Right Frame
url_label = customtkinter.CTkLabel(right_frame, text="URL:", bg_color=RIGHT_BG_COLOR, fg_color=BTN_TXT_COLOR,
                                  font=(MAIN_FONT, MAIN_FONT_SIZE))
url_label.grid(row=0, column=0, pady=(0, 10))
url_entry = customtkinter.CTkEntry(right_frame, width=30)
url_entry.grid(row=1, column=0, pady=(0, 20))

email_label = customtkinter.CTkLabel(right_frame, text="Email/Username:", bg_color=RIGHT_BG_COLOR,
                                    fg_color=BTN_TXT_COLOR, font=(MAIN_FONT, MAIN_FONT_SIZE))
email_label.grid(row=2, column=0, pady=(0, 10))
email_entry = customtkinter.CTkEntry(right_frame, width=30)
email_entry.insert(0, default_email)
email_entry.grid(row=3, column=0, pady=(0, 20))

password_label = customtkinter.CTkLabel(right_frame, text="Password:", bg_color=RIGHT_BG_COLOR,
                                       fg_color=BTN_TXT_COLOR, font=(MAIN_FONT, MAIN_FONT_SIZE))
password_label.grid(row=4, column=0, pady=(0, 10))
password_entry = customtkinter.CTkEntry(right_frame, width=30)
password_entry.grid(row=5, column=0, pady=(0, 20))

generate_password_button = customtkinter.CTkButton(right_frame, text="Generate Password", bg_color=BTN_FG_COLOR,
                                                  fg_color=BTN_TXT_COLOR, font=(MAIN_FONT, SECOND_FONT_SIZE),
                                                  command=password_gen)
generate_password_button.grid(row=6, column=0, pady=(0, 20))

add_button = customtkinter.CTkButton(right_frame, text="Add", bg_color=BTN_FG_COLOR, fg_color=BTN_TXT_COLOR,
                                    font=(MAIN_FONT, SECOND_FONT_SIZE), command=save)
add_button.grid(row=7, column=0)

change_default_email_button = customtkinter.CTkButton(right_frame, text="Change Default Email", bg_color=BTN_FG_COLOR,
                                                      fg_color=BTN_TXT_COLOR, font=(MAIN_FONT, SECOND_FONT_SIZE),
                                                      command=change_default_email)
change_default_email_button.grid(row=8, column=0)

# Run the app
app.mainloop()
