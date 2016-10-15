from cm_enigma import *
enigma = Enigma()

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter.messagebox import *

mainwindow = Tk()
mainwindow.title("Enigma ciphering machine")
#mainwindow.geometry("300x50+480+240")
mainwindow.resizable(False, False)

mainwindow.columnconfigure(0,pad=5)
mainwindow.columnconfigure(1,pad=5)
mainwindow.columnconfigure(2,pad=5)
mainwindow.rowconfigure(0,pad=5)
mainwindow.rowconfigure(1,pad=5)
mainwindow.rowconfigure(2,pad=5)
mainwindow.rowconfigure(3,pad=5)
mainwindow.rowconfigure(4,pad=5)
mainwindow.rowconfigure(5,pad=5)

def btn_choose_file_click():
    file_name = askopenfilename(
        initialdir=r"C:\Users\Victor\Documents\BMSTU\sem7\IS\l2\tests",
        multiple=True)
    if file_name:
        edt_file.delete(0, END)
        edt_file.insert(0, file_name)

def btn_encrypt_click():
    enigma.setkey(keya.get(), keyb.get(), keyc.get())
    for enc_file_name in edt_file.get().split(" "):
        try:
            #enc_file_name = edt_file.get()
            in_file = open(enc_file_name, "rb")
            enc_file_name = enc_file_name + ".enc"
            out_file = open(enc_file_name, "wb")
            for x in in_file:
                out_file.write(bytes(enigma.encrypt(x)))
            out_file.close()
            in_file.close()
            messagebox.showinfo("Success",
                                "Result in file "+enc_file_name)        
        except FileNotFoundError:
            messagebox.showerror("Error", "File doesn't exist")
        
'''
def btn_decrypt_click():
    enigma.setkey(keya.get(), keyb.get(), keyc.get())
    try:
        enc_file_name = edt_file.get()
        in_file = open(enc_file_name, "rb")
        enc_file_name = enc_file_name + ".decrypted"
        out_file = open(enc_file_name, "wb")
        for x in in_file:
            out_file.write(bytes(enigma.decrypt(x)))
        out_file.close()
        in_file.close()
        messagebox.showinfo("Success",
                            "Result in file "+enc_file_name)
    except FileNotFoundError:
        messagebox.showerror("Error", "File doesn't exist")
'''

keya, keyb, keyc = IntVar(), IntVar(), IntVar()

lbl_key = Label(mainwindow, text="Rotor positions")
lbl_key.grid(row=0, columnspan=3)

lbl_keya = Label(mainwindow, text=chr(0), border=3, relief=SUNKEN)
lbl_keya.grid(row=1, column=0)
keya.trace("w", lambda *args: lbl_keya.config(text=chr(keya.get())))

lbl_keyb = Label(mainwindow, text=chr(0), border=3, relief=SUNKEN)
lbl_keyb.grid(row=1, column=1)
keyb.trace("w", lambda *args: lbl_keyb.config(text=chr(keyb.get())))

lbl_keyc = Label(mainwindow, text=chr(0), border=3, relief=SUNKEN)
lbl_keyc.grid(row=1, column=2)
keyc.trace("w", lambda *args: lbl_keyc.config(text=chr(keyc.get())))

spb_keya = Spinbox(mainwindow, width=10, from_=0, to=255, increment=1)
spb_keya.grid(row=2, column=0)
spb_keya.config(textvariable=keya)

spb_keyb = Spinbox(mainwindow, width=10, from_=0, to=255, increment=1)
spb_keyb.grid(row=2, column=1)
spb_keyb.config(textvariable=keyb)

spb_keyc = Spinbox(mainwindow, width=10, from_=0, to=255, increment=1)
spb_keyc.grid(row=2, column=2)
spb_keyc.config(textvariable=keyc)

separator = Separator(mainwindow, orient=HORIZONTAL)
separator.grid(row=3, columnspan=3, sticky="ew")

edt_file = Entry(mainwindow)
edt_file.insert(0, "tests/0.txt")
edt_file.grid(row=4, columnspan=2)

btn_choose_file = Button(mainwindow, text="Choose file...")
btn_choose_file.grid(row=4, column=2)
btn_choose_file.config(command=btn_choose_file_click)

btn_encrypt = Button(mainwindow, text="Encrypt file")
btn_encrypt.grid(row=5, column=1)
btn_encrypt.config(command=btn_encrypt_click)

btn_decrypt = Button(mainwindow, text="Decrypt file")
btn_decrypt.grid(row=5, column=2)
btn_decrypt.config(command=btn_encrypt_click)

#mainwindow.mainloop()
