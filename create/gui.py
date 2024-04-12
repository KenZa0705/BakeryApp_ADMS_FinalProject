from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from pathlib import Path
import psycopg2
from gui import *


class create_account:
    
    def commit(self):
        fname = self.entry_1.get()
        lname = self.entry_2.get()
        email = self.entry_3.get()
        password = self.entry_4.get()

        conn = psycopg2.connect(host="localhost", dbname="third_nf", user="postgres",
                        password="postgres", port=5432)

        cur = conn.cursor()  
        cur.execute('''INSERT INTO customers (first_name, last_name, email, password)
                    VALUES (%s, %s, %s, %s);''', (fname, lname, email, password))
        conn.commit()
        cur.close()
        conn.close()
        messagebox.showinfo()
        self.window.destroy()
        gui.main()
    
    def __init__(self):
        self.window = Tk()
        self.window.geometry("574x336")
        self.window.configure(bg="#F4B479")

        self.canvas = Canvas(
            self.window,
            bg="#F4B479",
            height=336,
            width=574,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1280.0,
            85.0,
            fill="#D9D9D9",
            outline=""
        )
        self.canvas.create_text(
            9.0,
            16.0,
            anchor="nw",
            text="Fill the following information:",
            fill="#000000",
            font=("Inika", 40 * -1)
        )
        self.canvas.create_text(
            9.0,
            96.0,
            anchor="nw",
            text="First Name: ",
            fill="#FFFFFF",
            font=("Inika", 24 * -1)
        )
        self.canvas.create_text(
            9.0,
            138.0,
            anchor="nw",
            text="Last Name: ",
            fill="#FFFFFF",
            font=("Inika", 24 * -1)
        )
        self.canvas.create_text(
            9.0,
            180.0,
            anchor="nw",
            text="e-mail:",
            fill="#FFFFFF",
            font=("Inika", 24 * -1)
        )
        self.canvas.create_text(
            9.0,
            222.0,
            anchor="nw",
            text="password:",
            fill="#FFFFFF",
            font=("Inika", 24 * -1)
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(359.0, 111.5, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=168.5, y=96.0, width=381.0, height=29.0)
        self.fname = self.entry_1.get()

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(359.0, 153.5, image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=168.5, y=138.0, width=381.0, height=29.0)  
        self.lname = self.entry_2.get()

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(359.0, 195.5, image=self.entry_image_3)
        self.entry_3 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=168.5, y=180.0, width=381.0, height=29.0)
        self.email = self.entry_3.get()

        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(359.0, 237.5, image=self.entry_image_4)
        self.entry_4 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=168.5, y=222.0, width=381.0, height=29.0)
        self.password = self.entry_4.get()

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.commit,
            relief="flat"
        )
        self.button_1.place(x=379.0, y=278.0, width=186.0, height=35.0)

        self.window.resizable(False, False)
        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        ASSETS_PATH = Path(r"C:\\Users\\ENZA\\Documents\\2ND YEAR SECOND SEM\\ADMS\\Bakery GUI\\build\\create\\assets\\frame0")
        return ASSETS_PATH / Path(path)
    
    
if __name__ == "__main__":
    create_account()
    
    
