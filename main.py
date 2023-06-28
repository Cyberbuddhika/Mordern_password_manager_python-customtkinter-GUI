import tkinter as tk
import customtkinter

#  Creating main app_window
app = customtkinter.CTk(fg_color="#042430")
app.geometry("800x600")
app.title("Password Manager")
app.configure(padx=25, pady=25)

# app.grid_rowconfigure(1, weight=1)
# app.grid_columnconfigure(0, weight=1)

canvas = tk.Canvas(app, width=600, height=400, bg='#042430')

#  right pane
# side_pane = customtkinter.CTkFrame(app, width=500, height=600, fg_color="#031c26", bg_color="#031c26")
# side_pane.grid(row=0, column=2,  sticky="s")


# label

welcome_label = customtkinter.CTkLabel(app, text="Welcome Buddhika", fg_color="transparent", font=("Segoe UI", 22))
welcome_label.place(x=0, y=0)

# buttons
view_passwords_button = customtkinter.CTkButton(app, text="View Passwords", fg_color="#0c526b", text_color="white")
view_passwords_button.place(x=0, y=70)
add_passwords_button = customtkinter.CTkButton(app, text="Add Password", fg_color="#0c526b", text_color="white")
add_passwords_button.place(x=0, y=110)
change_email_button = customtkinter.CTkButton(app, text="Change default email", fg_color="#0c526b", text_color="white")
change_email_button.place(x=0, y=150)






app.mainloop()