from cm_enigma import *

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter.messagebox import *

class application(Tk):
    def __init__(self, parent=None):
        Tk.__init__(self, parent)
        self.parent = parent
        self.title("Enigma ciphering machine")
        self.resizable(False, False)
        
        self.initialize()
        
        self.enigma = Enigma()


    def initialize(self):
        self.grid()
        
        self.columnconfigure(0,pad=5)
        self.columnconfigure(1,pad=5)
        self.columnconfigure(2,pad=5)
        self.rowconfigure(0,pad=5)
        self.rowconfigure(1,pad=5)
        self.rowconfigure(2,pad=5)
        self.rowconfigure(3,pad=5)
        self.rowconfigure(4,pad=5)
        self.rowconfigure(5,pad=5)

        #self.keya, self.keyb, self.keyc = IntVar(), IntVar(), IntVar()
        self.keya, self.keyb, self.keyc = StringVar(value="0"), StringVar(value="0"), StringVar(value="0")

        self.lbl_key = Label(self, text="Rotor positions")
        self.lbl_key.grid(row=0, columnspan=3)

        self.lbl_keya = Label(self, text=chr(0), border=3, relief=SUNKEN)
        self.lbl_keya.grid(row=1, column=0)
        self.keya.trace("w", lambda *args: self.lbl_keya.config(text=chr(int(self.keya.get() or 0))))

        self.lbl_keyb = Label(self, text=chr(0), border=3, relief=SUNKEN)
        self.lbl_keyb.grid(row=1, column=1)
        self.keyb.trace("w", lambda *args: self.lbl_keyb.config(text=chr(int(self.keyb.get() or 0))))

        self.lbl_keyc = Label(self, text=chr(0), border=3, relief=SUNKEN)
        self.lbl_keyc.grid(row=1, column=2)
        self.keyc.trace("w", lambda *args: self.lbl_keyc.config(text=chr(int(self.keyc.get() or 0))))

        self.spb_keya = Spinbox(self, width=10, from_=0, to=255, increment=1)
        self.spb_keya.grid(row=2, column=0)
        self.spb_keya.config(textvariable=self.keya)

        self.spb_keyb = Spinbox(self, width=10, from_=0, to=255, increment=1)
        self.spb_keyb.grid(row=2, column=1)
        self.spb_keyb.config(textvariable=self.keyb)

        self.spb_keyc = Spinbox(self, width=10, from_=0, to=255, increment=1)
        self.spb_keyc.grid(row=2, column=2)
        self.spb_keyc.config(textvariable=self.keyc)

        separator = Separator(self, orient=HORIZONTAL)
        separator.grid(row=3, columnspan=3, sticky="ew")

        self.edt_file = Entry(self)
        self.edt_file.insert(0, "tests/0.txt")
        self.edt_file.grid(row=4, columnspan=2)

        self.btn_choose_file = Button(self, text="Choose file...")
        self.btn_choose_file.grid(row=4, column=2)
        self.btn_choose_file.config(command=self.btn_choose_file_click)

        self.btn_encrypt = Button(self, text="Encrypt file")
        self.btn_encrypt.grid(row=5, column=1)
        self.btn_encrypt.config(command=self.btn_encrypt_click)

        self.btn_decrypt = Button(self, text="Decrypt file")
        self.btn_decrypt.grid(row=5, column=2)
        self.btn_decrypt.config(command=self.btn_encrypt_click)

        
    def btn_choose_file_click(self):
        file_name = askopenfilename(
            initialdir=r"C:\Users\Victor\Documents\BMSTU\sem7\IS\l2\tests",
            multiple=True)
        if file_name:
            self.edt_file.delete(0, END)
            self.edt_file.insert(0, file_name)

    def btn_encrypt_click(self):
        self.enigma.setkey(int(self.keya.get()), int(self.keyb.get()), int(self.keyc.get()))
        for enc_file_name in self.edt_file.get().split(" "):
            try:
                #enc_file_name = edt_file.get()
                in_file = open(enc_file_name, "rb")
                enc_file_name = enc_file_name + ".enc"
                out_file = open(enc_file_name, "wb")
                for x in in_file:
                    out_file.write(bytes(self.enigma.encrypt(x)))
                out_file.close()
                in_file.close()
                messagebox.showinfo("Success",
                                    "Result in file "+enc_file_name)        
            except FileNotFoundError:
                messagebox.showerror("Error", "File doesn't exist")

if __name__=='__main__':
    app = application()
    try:
        app.mainloop()
    except Exception as e:
        messagebox.showerror("Fatal error", str(e))
