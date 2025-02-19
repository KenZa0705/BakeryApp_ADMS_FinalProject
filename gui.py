
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import psycopg2
# from tkinter import *
# Explicit imports to satisfy Flake8 
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from create import gui


from tkinter import Tk, Canvas, Button, Entry, PhotoImage

class MyApp:
    def __init__(self, window):
        
        def createaccount():     #this function is to create a new account for a customer
            self.window.destroy()
            gui.create_account()
            pass

        conn = psycopg2.connect(host="localhost", dbname="third_nf", user="postgres",
                        password="postgres", port=5432)

        cur = conn.cursor()
        
        self.window = window
        self.window.geometry("700x550")
        self.window.configure(bg="#FFFFFF")
        
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=550,
            width=700,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(350.0, 45.0, image=self.image_image_1)
        
        self.canvas.create_text(
            251.0,
            26.0,
            anchor="nw",
            text="Geo-San Bakery ",
            fill="#000000",
            font=("Libre Caslon Display Regular", 32 * -1)
        )
        
        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(535.0, 284.0, image=self.image_image_2)
        
        self.canvas.create_text(
            409.0,
            129.0,
            anchor="nw",
            text="Sign In",
            fill="#000000",
            font=("Libre Bodoni Regular", 24 * -1)
        )
        
        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(190.0, 281.0, image=self.image_image_3)
        
        self.canvas.create_text(
            409.0,
            165.0,
            anchor="nw",
            text="The start of a wonderful bread experience",
            fill="#000000",
            font=("Libre Bodoni Regular", 10 * -1)
        )
        
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=createaccount,
            relief="flat"
        )
        self.button_1.place(x=484.0, y=377.0, width=102.0, height=15.0)
        
        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(595.0, 48.0, image=self.image_image_4)
        
        self.image_image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(655.0, 45.0, image=self.image_image_5)
        
        self.image_image_6 = PhotoImage(file=self.relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(45.0, 45.0, image=self.image_image_6)
        
        self.image_image_7 = PhotoImage(file=self.relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(105.0, 45.0, image=self.image_image_7)
        
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(536.0, 227.0, image=self.entry_image_1)
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(x=409.0, y=209.0, width=254.0, height=34.0)
        
        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(536.0, 299.0, image=self.entry_image_2)
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(x=409.0, y=281.0, width=254.0, height=34.0)
        
        self.canvas.create_text(
            238.0,
            514.0,
            anchor="nw",
            text="2024, KEI Group and affiliates. All rights reserved",
            fill="#000000",
            font=("Libre Bodoni Regular", 10 * -1)
        )
        
        self.image_image_8 = PhotoImage(file=self.relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(223.0, 521.0, image=self.image_image_8)
        
        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(x=410.0, y=330.0, width=250.0, height=40.0)
        
        self.canvas.create_text(
            522.0,
            196.0,
            anchor="nw",
            text="email",
            fill="#000000",
            font=("Arial", 10 * -1)
        )
        
        self.canvas.create_text(
            514.0,
            268.0,
            anchor="nw",
            text="password",
            fill="#000000",
            font=("Arial", 10 * -1)
        )
        
        self.window.resizable(False, False)
        self.window.mainloop()
        
    def relative_to_assets(self, path: str) -> Path:
        ASSETS_PATH = Path(r"C:\Users\ENZA\Documents\2ND YEAR SECOND SEM\ADMS\Bakery GUI\build\assets\frame0")
        return ASSETS_PATH / Path(path)
        
def main():
    window = Tk()
    app = MyApp(window)
            
if __name__ == "__main__":
    main()
