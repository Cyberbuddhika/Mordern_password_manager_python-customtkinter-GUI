
import customtkinter



MAIN_FONT = "Ubuntu"
LEFT_BG_COLOR = "#08303b"
RIGHT_BG_COLOR = "#042430"
BTN_FG_COLOR = "#0c526b"
BTN_TXT_COLOR = "White"
MAIN_FONT_SIZE = 22
SECOND_FONT_SIZE = 12


class ViewInfoWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("View Passwords")
        self.geometry("500x200")
        self.configure(fg_color="#042430")

        self.label = customtkinter.CTkLabel(self, text="About Me and the App", font=("Ubuntu", 22, "underline"), text_color="White" )
        self.label.place(x=150, y=30)
        self.label = customtkinter.CTkLabel(self, text="Developed by:", font=("Ubuntu", 15),
                                            text_color="White")
        self.label.place(x=50, y=80)
        self.label = customtkinter.CTkLabel(self, text="@cyberbuddhika", font=("Ubuntu", 13),
                                            text_color="White")
        self.label.place(x=160, y=80)
        self.label = customtkinter.CTkLabel(self, text="Email me:", font=("Ubuntu", 15),
                                            text_color="White")
        self.label.place(x=50, y=120)
        self.label = customtkinter.CTkLabel(self, text="buddhikajayasingha@gmail.com", font=("Ubuntu", 13),
                                            text_color="White")
        self.label.place(x=160, y=120)
