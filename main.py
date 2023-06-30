import tkinter as tk
import customtkinter
from password_strength import password_strength
from password_generator import password_gen


# ------Showing Generating password----------------
def showing_generated_password():
    generated_password = password_gen()
    password_entry.delete(0, tk.END)  # Clear the existing password
    password_entry.insert(tk.END, generated_password)
    showing_password_strength(generated_password)


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
    email_entry.insert(tk.END, default_email)


# ------Setting up defaults ----------------

MAIN_FONT = "Ubuntu"
LEFT_BG_COLOR = "#08303b"
RIGHT_BG_COLOR = "#042430"
BTN_FG_COLOR = "#0c526b"
BTN_TXT_COLOR = "White"
MAIN_FONT_SIZE = 22
SECOND_FONT_SIZE = 12
default_email = "buddhika@gmail.com"

passwords_saved = True

#  Creating main app_window
app = customtkinter.CTk(fg_color="#042430")
app.geometry("800x600")
app.title("Password Manager")

# -------Left Pane--------------------

# Frame
left_pane = tk.Frame(app)
left_pane.place(x=0, y=0, width=300, height=600)
left_pane.configure(bg=LEFT_BG_COLOR)

canvas = tk.Canvas(left_pane, width=100, height=100, highlightthickness=0, background=LEFT_BG_COLOR)
password_logo = tk.PhotoImage(file="icons8-password-100.png")
canvas.create_image(50, 50, image=password_logo)
canvas.place(x=75, y=25)

# label
welcome_label = customtkinter.CTkLabel(left_pane, text="Welcome Back!", fg_color="transparent",
                                       font=(MAIN_FONT, MAIN_FONT_SIZE))
welcome_label.place(x=50, y=130)
welcome_label2 = customtkinter.CTkLabel(left_pane, text="buddhika", font=(MAIN_FONT, MAIN_FONT_SIZE))
welcome_label2.place(x=50, y=165)

# buttons
view_passwords_button = customtkinter.CTkButton(left_pane, text="View Passwords", fg_color=BTN_FG_COLOR,
                                                text_color=BTN_TXT_COLOR)
view_passwords_button.place(x=50, y=225)
change_login_button = customtkinter.CTkButton(left_pane, text="Change Login", fg_color=BTN_FG_COLOR,
                                              text_color=BTN_TXT_COLOR)
change_login_button.place(x=50, y=260)
change_email_button = customtkinter.CTkButton(left_pane, text="Change Default Email", fg_color=BTN_FG_COLOR,
                                              text_color=BTN_TXT_COLOR)
change_email_button.place(x=50, y=295)
info_button = customtkinter.CTkButton(left_pane, text="Info", fg_color=BTN_FG_COLOR, text_color=BTN_TXT_COLOR)
info_button.place(x=50, y=330)

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

#  Labels
website_name_label = customtkinter.CTkLabel(right_pane, text="Website:", font=(MAIN_FONT, SECOND_FONT_SIZE))
website_name_label.place(x=50, y=125)
url_label = customtkinter.CTkLabel(right_pane, text="URL:", font=(MAIN_FONT, SECOND_FONT_SIZE))
url_label.place(x=50, y=160)
email_label = customtkinter.CTkLabel(right_pane, text="Email/Username:", font=(MAIN_FONT, SECOND_FONT_SIZE))
email_label.place(x=50, y=195)
password_label = customtkinter.CTkLabel(right_pane, text="Password:", font=(MAIN_FONT, SECOND_FONT_SIZE))

# Password strength showing
password_label.place(x=50, y=230)
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
                                      width=75)
save_button.place(x=275, y=350)
cancel_button = customtkinter.CTkButton(right_pane, text="Cancel", fg_color=BTN_FG_COLOR, text_color=BTN_TXT_COLOR,
                                        width=75, command=Clearing_password_sec)
cancel_button.place(x=360, y=350)

# Bind the checking_password_strength function to the KeyRelease event of the entry widget
password_entry.bind("<KeyRelease>", showing_password_strength)

app.mainloop()
