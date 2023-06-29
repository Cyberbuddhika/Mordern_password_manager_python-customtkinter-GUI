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
add_passwords_button = customtkinter.CTkButton(left_pane, text="Add Password", fg_color=BTN_FG_COLOR, text_color=BTN_TXT_COLOR)
add_passwords_button.place(x=50, y=260)
change_email_button = customtkinter.CTkButton(left_pane, text="Change Default Email", fg_color=BTN_FG_COLOR, text_color=BTN_TXT_COLOR)
change_email_button.place(x=50, y=295)


# -------Right Pane--------------------

# Frame
right_pane = tk.Frame(app)
right_pane.place(x=250, y=0, width=550, height=600)
right_pane.configure(bg=RIGHT_BG_COLOR)

# Title - changing based on password availability
if passwords_saved:
    welcome_label = customtkinter.CTkLabel(right_pane, text="Passwords", fg_color="transparent", font=(MAIN_FONT, 22))
    welcome_label.place(x=250, y=0)
else:
    password_title_label = customtkinter.CTkLabel(right_pane, text="Ops!!! There is no passwords to show. Try adding one",
                                                  fg_color="transparent", font=(MAIN_FONT, 15), text_color="#C0C0C0")
    password_title_label.place(x=150, y=0)

#  Password list

website_name_label = customtkinter.CTkLabel(right_pane, text="Website Name", fg_color="transparent", font=(MAIN_FONT, 15))
website_name_label.place(x=150, y=50)
website_url_label = customtkinter.CTkLabel(right_pane, text="URL", fg_color="transparent", font=(MAIN_FONT, 15))
website_url_label.place(x=250, y=50)
website_email_label = customtkinter.CTkLabel(right_pane, text="Email", fg_color="transparent", font=(MAIN_FONT, 15))
website_email_label.place(x=350, y=50)









app.mainloop()