import datetime
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
        self.geometry("500x500")
        self.configure(fg_color="#042430")

        self.label = customtkinter.CTkLabel(self, text="Copyright", font=("Ubuntu", 22, "underline"), text_color="White" )
        self.label.place(x=200, y=20)

        # ------Setting up copyright notice----------------
        current_year = datetime.date.today().year

        # Copyright notice
        copyright_notice = f"Copyright (c) {current_year} @cyberbuddhika"
        copyright_notice_label = customtkinter.CTkLabel(self,
                                                        text=copyright_notice,
                                                        font=(MAIN_FONT, 12))
        copyright_notice_label.place(x=20, y=80)
        copyright_text = "Permission is hereby granted, free of charge, to any person obtaining a copy of this " \
                         "software \nand associated documentation files (the 'Software'), to deal in the Software " \
                         "without \nrestriction, including without limitation the rights to use, copy, modify, merge, " \
                         "publish, \ndistribute, sublicense, and/or sell copies of the Software, and to permit persons " \
                         "to whom \nthe Software is furnished to do so, subject to the following conditions:\n\nThe " \
                         "above copyright notice and this permission notice shall be included in all copies or\n " \
                         "substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY " \
                         "OF ANY KIND, EXPRESS OR IMPLIED, \nINCLUDING BUT NOT LIMITED TO THE WARRANTIES OF " \
                         "MERCHANTABILITY, FITNESS FOR \nA PARTICULAR PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL" \
                         "THE AUTHORS OR \nCOPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY," \
                         "WHETHER IN \nAN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION" \
                         "WITH \nTHE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."

        self.label = customtkinter.CTkLabel(self, text=copyright_text, font=("Ubuntu", 10),
                                            text_color="White", justify="left")
        self.label.place(x=20, y=150)
        self.label = customtkinter.CTkLabel(self, text="Email me:", font=("Ubuntu", 10),
                                            text_color="White")
        self.label.place(x=20, y=450)
        self.label = customtkinter.CTkLabel(self, text="buddhikajayasingha@gmail.com", font=("Ubuntu", 10),
                                            text_color="White")
        self.label.place(x=70, y=450)