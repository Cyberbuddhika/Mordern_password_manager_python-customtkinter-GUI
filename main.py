import tkinter as tk
import customtkinter

MAIN_FONT = "Ubuntu"
LEFT_BG_COLOR = "#08303b"
RIGHT_BG_COLOR = "#042430"
BTN_FG_COLOR = "#0c526b"
BTN_TXT_COLOR = "White"

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

canvas = tk.Canvas(left_pane, width=100, height=100,  highlightthickness=0, background=LEFT_BG_COLOR)
password_logo = tk.PhotoImage(file="icons8-password-100.png")
canvas.create_image(50, 50, image=password_logo)
canvas.place(x=75, y=25)

# label
welcome_label = customtkinter.CTkLabel(left_pane, text="Welcome Back!", fg_color="transparent", font=(MAIN_FONT, 22))
welcome_label.place(x=50, y=130)
welcome_label2 = customtkinter.CTkLabel(left_pane, text="buddhika", font=(MAIN_FONT, 20))
welcome_label2.place(x=50, y=165)

# buttons
view_passwords_button = customtkinter.CTkButton(left_pane, text="View Passwords", fg_color=BTN_FG_COLOR, text_color=BTN_TXT_COLOR)
view_passwords_button.place(x=50, y=225)
change_login_button = customtkinter.CTkButton(left_pane, text="Change Login", fg_color=BTN_FG_COLOR, text_color=BTN_TXT_COLOR)
change_login_button.place(x=50, y=260)
change_email_button = customtkinter.CTkButton(left_pane, text="Change Default Email", fg_color=BTN_FG_COLOR, text_color=BTN_TXT_COLOR)
change_email_button.place(x=50, y=295)
info_button = customtkinter.CTkButton(left_pane, text="Info", fg_color=BTN_FG_COLOR, text_color=BTN_TXT_COLOR)
info_button.place(x=50, y=330)


# -------Right Pane--------------------

# Frame
right_pane = tk.Frame(app)
right_pane.place(x=250, y=0, width=550, height=600)
right_pane.configure(bg=RIGHT_BG_COLOR)

# Title - changing based on activity
add_password_label = customtkinter.CTkLabel(right_pane, text="+ Add a Password", fg_color="transparent", font=(MAIN_FONT, 22))
add_password_label.place(x=180, y=50)

#  Add password form

#  Labels
website_name_label = customtkinter.CTkLabel(right_pane, text="Website:", font=(MAIN_FONT, 18))
website_name_label.place(x=50, y=125)
url_label = customtkinter.CTkLabel(right_pane, text="URL:", font=(MAIN_FONT, 18))
url_label.place(x=50, y=160)
email_label = customtkinter.CTkLabel(right_pane, text="Email/Username:", font=(MAIN_FONT, 18))
email_label.place(x=50, y=195)
password_label = customtkinter.CTkLabel(right_pane, text="Password:", font=(MAIN_FONT, 18))
password_label.place(x=50, y=230)

# #  Entries
# website_input = Entry(width=32)
# website_input.focus()
# website_input.grid(column=1, row=1, columnspan=1)
# email_input = Entry(width=55)
# email_input.insert(0, "buddhika@gmail.com")
# email_input.grid(column=1, row=2, columnspan=2)
# password_input = Entry(width=32)
# password_input.grid(column=1, row=3)
#
# #  Buttons
# password_btn = Button(text="Generate Password", width=18, command=password_gen)
# password_btn.grid(column=2, row=3)
# add_btn = Button(width=48, text="Add", command=save)
# add_btn.grid(column=1, row=4, columnspan=2)
# search_btn = Button(text="Search", width=18, command=search)
# search_btn.grid(column=2, row=1)











app.mainloop()