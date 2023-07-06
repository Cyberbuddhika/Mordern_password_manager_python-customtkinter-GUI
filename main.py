import tkinter as tk
from tkinter import messagebox
import customtkinter
from password_strength import password_strength
from password_generator import password_gen
import pyperclip
import json
from view_passwords import ViewPasswordWindow
from signup import ViewSignupWindow
from login import ViewLoginWindow
from info import ViewInfoWindow
import os.path
from cryptography.fernet import Fernet

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

#  Creating main app_window
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
    email = email_entry.get()
    dialog = customtkinter.CTkInputDialog(
        text=f"Your current email is: {email}\n\nPlease enter a new email to set as your default email.", title="Change Default Email")
    new_email = dialog.get_input()  # waits for input
    if new_email:
        # Step 1: Read the JSON file
        with open('data/login.json', 'r') as file:
            data = json.load(file)
        # Step 2: Update the email value
        for user_data in data.values():
            if 'email' in user_data:
                user_data['email'] = new_email
                default_email = new_email
                break

        # Step 3: Write the modified data back to the JSON file
        with open('data/login.json', 'w') as file:
            json.dump(data, file, indent=4)

        # Additional code to update the email_entry in your GUI
        email_entry.delete(0, tk.END)
        email_entry.insert(0, default_email)
    else:
        print("user canceled or tried saving empty string. email haven't changed.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = website_entry.get()
    url = url_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website_input or not email or not password:
        messagebox.showerror("Empty Fields", "Please fill all the input fields")
        return

    # Generate a key if not already generated
    if not os.path.exists('data/key.key'):
        key = Fernet.generate_key()
        with open('data/key.key', 'wb') as key_file:
            key_file.write(key)

    # Retrieve the encryption key
    with open('data/key.key', 'rb') as key_file:
        key = key_file.read()

    # Create a cipher
    cipher = Fernet(key)

    # Encrypt data
    encrypted_pw = cipher.encrypt(password.encode()).decode('utf-8')

    try:
        website = website_input.lower()
    except AttributeError:
        website = ""

    new_data = {
        website: {
            "url": url,
            "email": email,
            "password": encrypted_pw
        }
    }

    try:
        with open('data/data.json', mode='r') as data_file:
            # Read old data
            data = json.load(data_file)
    except FileNotFoundError:
        data = new_data
    else:
        if website in data:
            response = messagebox.askyesno(title="Duplicate password",
                                           message=f"You have a previously saved password for {website}.\n\nDo you want to update it with the new password?")
            if response:
                # Update old data with new data
                data[website]["url"] = url
                data[website]["email"] = email
                data[website]["password"] = encrypted_pw
                messagebox.showinfo("Password Updated Successfully",
                                    f"Password for {website} has been updated successfully.\n\nURL: {url}\nEmail: {email}")
            else:
                return
        else:
            # Save new data
            data.update(new_data)
            messagebox.showinfo("Password Saved Successfully",
                                f"New password for {website} has been saved successfully.\n\nURL: {url}\nEmail: {email}")

    with open('data/data.json', mode='w') as data_file:
        json.dump(data, data_file, indent=4)

    Clearing_password_sec()
    set_focus()


# ------showing password strength----------------
def showing_password_strength(event):
    input_password = password_entry.get()
    strength_text = password_strength(input_password)
    if "Strong" in strength_text:
        password_strength_label.configure(text=strength_text, text_color="green")
    elif "Moderate" in strength_text:
        password_strength_label.configure(text=strength_text, text_color="yellow")
    else:
        password_strength_label.configure(text=strength_text, text_color="red")


# ------Clearing add password section----------------
def Clearing_password_sec():
    website_entry.delete(0, tk.END)
    url_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    global default_email  # Add this line to access the global default_email variable
    email_entry.insert(tk.END, default_email)  # Insert the updated default email


# ------Open View password window----------------
def view_passwords():
    try:
        with open('data/data.json', mode='r') as data_file:
            # Read old data
            data = json.load(data_file)
    except FileNotFoundError:
        text = "You don't have any saved passwords yet. Let's add your first password!\nTo get started, go to 'Add " \
               "Password' section and add your first password"
        messagebox.showinfo("No Saved Passwords", text)

    else:
        # Get the coordinates of the main window
        main_window_x = app.winfo_x()
        main_window_y = app.winfo_y()

        # Calculate the coordinates for the "View Password" window
        view_window_x = main_window_x
        view_window_y = main_window_y

        view_window = ViewPasswordWindow(app)
        view_window.geometry(f"+{view_window_x}+{view_window_y}")  # Set the coordinates for the window
        view_window.transient(app)
        view_window.grab_set()
        app.withdraw()  # Hide the main window
        app.wait_window(view_window)
        app.deiconify()  # Show the main window again after the password window is closed


# -------Open info window--------------------
def open_information_window():
    view_window = ViewInfoWindow(app)
    view_window.transient(app)
    view_window.grab_set()
    app.wait_window(view_window)
    app.deiconify()  # Show the main window again after the password window is closed


# ---- Catching error when login or signup windows manually close------

try:
    # -------Left Pane--------------------

    # Frame
    left_pane = tk.Frame(app)
    left_pane.place(x=0, y=0, width=300, height=600)
    left_pane.configure(bg=LEFT_BG_COLOR)

except tk.TclError:
    print("Login or signup window closed.")
    # Handles the case when the window has been destroyed

else:
    canvas = tk.Canvas(left_pane, width=100, height=100, highlightthickness=0, background=LEFT_BG_COLOR)
    password_logo = tk.PhotoImage(file="icons8-password-100.png")
    canvas.create_image(50, 50, image=password_logo)
    canvas.place(x=75, y=25)

    # label
    welcome_label = customtkinter.CTkLabel(left_pane, text="Welcome Back!", fg_color="transparent",
                                           font=(MAIN_FONT, MAIN_FONT_SIZE))
    welcome_label.place(x=50, y=130)
    welcome_label2 = customtkinter.CTkLabel(left_pane, text=user_name, font=(MAIN_FONT, MAIN_FONT_SIZE))
    welcome_label2.place(x=50, y=165)

    # buttons
    view_passwords_button = customtkinter.CTkButton(left_pane, text="View Passwords", fg_color=BTN_FG_COLOR,
                                                    text_color=BTN_TXT_COLOR, command=view_passwords)
    view_passwords_button.place(x=50, y=225)
    # change_login_button = customtkinter.CTkButton(left_pane, text="Change Login", fg_color=BTN_FG_COLOR,
    #                                               text_color=BTN_TXT_COLOR)
    # change_login_button.place(x=50, y=260)
    change_email_button = customtkinter.CTkButton(left_pane, text="Change Default Email", fg_color=BTN_FG_COLOR,
                                                  text_color=BTN_TXT_COLOR, command=change_default_email)
    change_email_button.place(x=50, y=260)
    info_button = customtkinter.CTkButton(left_pane, text="Info", fg_color=BTN_FG_COLOR, text_color=BTN_TXT_COLOR,
                                          command=open_information_window)
    info_button.place(x=50, y=295)

    # -------Right Pane--------------------

    # Frame
    right_pane = tk.Frame(app)
    right_pane.place(x=250, y=0, width=550, height=600)
    right_pane.configure(bg=RIGHT_BG_COLOR)

    # Title - changing based on activity
    add_password_label = customtkinter.CTkLabel(right_pane, text="+ Add a Password", fg_color="transparent",
                                                font=(MAIN_FONT, MAIN_FONT_SIZE))
    add_password_label.place(x=180, y=50)


    # ------Add password form----------------

    # ------Showing Generating password----------------
    def showing_generated_password():
        global length_of_password
        length_of_password = password_length_entry.get()

        if not length_of_password:
            length_of_password = 12
            password_length_entry.insert(tk.END, 12)
        elif not length_of_password.isdigit():
            error_message = "Password length must be a number."
            messagebox.showerror("Incorrect password length", error_message)
            password_length_entry.delete(0, tk.END)
        elif int(length_of_password) > 40:
            length_of_password = 40
            error_message = "Password length cannot be greater than 40."
            messagebox.showerror("Incorrect password length", error_message)
        else:
            length_of_password = int(length_of_password)
            if length_of_password >= num_of_letters + num_of_symbols + num_of_numbers:
                generated_password = password_gen(num_of_letters, num_of_symbols, num_of_numbers, length_of_password)
                password_entry.delete(0, tk.END)  # Clear the existing password
                password_entry.insert(tk.END, generated_password)
                showing_password_strength(generated_password)
                pyperclip.copy(generated_password)  # using pyperclip to add password to clipboard
            else:
                error_message = "Please increase the password length or reduce the number of letters, symbols, or numbers."
                messagebox.showerror("Insufficient password length", error_message)


    # ------Settings for random password generator----------------

    # Labels

    Password_Generator_Settings_label = customtkinter.CTkLabel(right_pane, text="Customize Your Generated Password",
                                                               font=(MAIN_FONT, 14, "underline"))
    Password_Generator_Settings_label.place(x=100, y=395)
    password_length_label = customtkinter.CTkLabel(right_pane, text="Select the length of your password (maximum 40):",
                                                   font=(MAIN_FONT, SECOND_FONT_SIZE))
    password_length_label.place(x=100, y=430)
    Number_of_letters_label = customtkinter.CTkLabel(right_pane,
                                                     text="Select number of letters for your password (maximum 20):",
                                                     font=(MAIN_FONT, SECOND_FONT_SIZE))
    Number_of_letters_label.place(x=100, y=455)
    Number_of_symbols_label = customtkinter.CTkLabel(right_pane,
                                                     text="Select number of symbols for your Password (maximum 08):",
                                                     font=(MAIN_FONT, SECOND_FONT_SIZE))
    Number_of_symbols_label.place(x=100, y=480)
    Number_of_numbers_label = customtkinter.CTkLabel(right_pane,
                                                     text="Select number of numbers for your Password (maximum 08):",
                                                     font=(MAIN_FONT, SECOND_FONT_SIZE))
    Number_of_numbers_label.place(x=100, y=505)

    # Entry

    password_length_entry = customtkinter.CTkEntry(right_pane, width=50, height=20, font=(MAIN_FONT, SECOND_FONT_SIZE),
                                                   fg_color="#3a7ebf")
    password_length_entry.place(x=450, y=430)
    password_length_entry.insert(tk.END, 12)


    #  Dropdowns

    def num_letters_callback(choice):
        global num_of_letters
        num_of_letters = int(choice)


    num_letters = customtkinter.CTkOptionMenu(app,
                                              values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                                                      "14", "15", "16", "17", "18", "19", "20"], width=50, height=20,
                                              command=num_letters_callback)
    num_letters.set("8")
    num_letters.place(x=700, y=460)


    def num_symbols_callback(choice):
        global num_of_symbols
        num_of_symbols = int(choice)


    num_symbols = customtkinter.CTkOptionMenu(app, values=["1", "2", "3", "4", "5", "6", "7", "8"], width=50, height=20,
                                              command=num_symbols_callback)
    num_symbols.set("2")
    num_symbols.place(x=700, y=485)


    def num_numbers_callback(choice):
        global num_of_numbers
        num_of_numbers = int(choice)


    num_number = customtkinter.CTkOptionMenu(app, values=["1", "2", "3", "4", "5", "6", "7", "8"], width=50, height=20,
                                             command=num_numbers_callback)
    num_number.set("2")
    num_number.place(x=700, y=510)

    # ---------Add Password section----------

    #  Labels
    website_name_label = customtkinter.CTkLabel(right_pane, text="Website Name:", font=(MAIN_FONT, SECOND_FONT_SIZE))
    website_name_label.place(x=50, y=125)
    url_label = customtkinter.CTkLabel(right_pane, text="Website Address(URL):", font=(MAIN_FONT, SECOND_FONT_SIZE))
    url_label.place(x=50, y=160)
    email_label = customtkinter.CTkLabel(right_pane, text="Email/Username:", font=(MAIN_FONT, SECOND_FONT_SIZE))
    email_label.place(x=50, y=195)
    password_label = customtkinter.CTkLabel(right_pane, text="Password:", font=(MAIN_FONT, SECOND_FONT_SIZE))
    password_label.place(x=50, y=230)

    # Password strength showing
    password_strength_label = customtkinter.CTkLabel(right_pane, text="",
                                                     font=(MAIN_FONT, SECOND_FONT_SIZE, "bold"))
    password_strength_label.place(x=200, y=260)

    #  Entries
    website_entry = customtkinter.CTkEntry(right_pane, width=300, font=(MAIN_FONT, SECOND_FONT_SIZE))
    website_entry.place(x=200, y=125)
    url_entry = customtkinter.CTkEntry(right_pane, width=300, font=(MAIN_FONT, SECOND_FONT_SIZE))
    url_entry.place(x=200, y=160)
    email_entry = customtkinter.CTkEntry(right_pane, width=300, font=(MAIN_FONT, SECOND_FONT_SIZE))
    email_entry.insert(tk.END, default_email)
    email_entry.place(x=200, y=195)
    password_entry = customtkinter.CTkEntry(right_pane, width=300, font=(MAIN_FONT, SECOND_FONT_SIZE))
    password_entry.place(x=200, y=230)

    #  Button
    generate_passwords_button = customtkinter.CTkButton(right_pane, text="Generate Secure Password", fg_color=BTN_FG_COLOR,
                                                        text_color=BTN_TXT_COLOR, width=300,
                                                        command=showing_generated_password)
    generate_passwords_button.place(x=200, y=300)
    save_button = customtkinter.CTkButton(right_pane, text="Save", fg_color=BTN_FG_COLOR, text_color=BTN_TXT_COLOR,
                                          width=75, command=save)
    save_button.place(x=275, y=350)
    cancel_button = customtkinter.CTkButton(right_pane, text="Cancel", fg_color=BTN_FG_COLOR, text_color=BTN_TXT_COLOR,
                                            width=75, command=Clearing_password_sec)
    cancel_button.place(x=360, y=350)

    # Bind the checking_password_strength function to the KeyRelease event of the entry widget
    password_entry.bind("<KeyRelease>", showing_password_strength)

    # ------Setting Focus on website name entry on password form----------------
    def set_focus():
        website_entry.focus_set()


    # ------Binding Enter key to save password function on password form----------------
    app.bind("<Return>", save)

    # Call the set_focus function after a short delay
    app.after(100, set_focus)

    app.mainloop()
