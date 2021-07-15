import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import cryptography
from cryptography.fernet import Fernet
import pyqrcode
m = tk.Tk()

m.title("Cryptography Tools")

def qrcodeconvert():
     res = codeqr.get()
     
     with open(res, 'rb') as o_file:
         o = o_file.read()
     
     qr = pyqrcode.create(o)
     qr.png("qrcode.png", scale=10)
     qr.show()


def window():
     tk.Label(m, text="Source File For QR Code Conversion").grid(row=9)
     codeqr.grid(row=11, column=1)
     qrbutton = tk.Button(m, text="Convert To QR", command=qrcodeconvert)
     qrbutton.grid(row=13, column=1)
     
#Function for Decrypting Files
def dc():
     x = e1.get()
     y = e2.get()
     
     with open('auth.key', 'rb') as mykey:
         key = mykey.read()
         print(key)
     
     f = Fernet(key)
     
     with open(x, 'rb') as encrypted_file:
         encrypted = encrypted_file.read()

     decrypted = f.decrypt(encrypted)

     with open(y, 'wb') as decrypted_file:
         decrypted_file.write(decrypted)
         
#Function for Encrypting Files
def submit():
     x = e1.get()
     y = e2.get()
     
     with open('auth.key', 'rb') as mykey:
         key = mykey.read()
         print(key)
     
     f = Fernet(key)
    
     with open(x, 'rb') as o_file:
         o = o_file.read()

     encrypted = f.encrypt(o)

     with open (y, 'wb') as encrypted_file:
         encrypted_file.write(encrypted)
         
#Function for generating a key
def keygen():
     key = Fernet.generate_key()
     with open('auth.key', 'wb') as mykey:
         mykey.write(key)
         
     with open('auth.key', 'rb') as mykey:
         key = mykey.read()
         print(key)

#labels for Buttons and all sorts of stuff
tk.Label(m, text="Source File").grid(row=0)
tk.Label(m, text="Output File").grid(row=1)
btn = tk.Button(m, text="Encrypt", command=submit)
btn2 = tk.Button(m, text="Generate Encryption Key", command=keygen)
btn3 = tk.Button(m, text="Decrypt", command=dc)
testwindow = tk.Button(m, text="Show QR Code Tool", command=window)


e1 = tk.Entry(m)
e2 = tk.Entry(m)
codeqr = tk.Entry(m)

#text design and alignment
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#button design and alignment
btn.grid(row=2, column=1)
btn2.grid(row=3, column=1)
btn3.grid(row=4, column=1)
testwindow.grid(row=7, column=1)

m.mainloop()