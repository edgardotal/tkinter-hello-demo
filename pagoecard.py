from os import path
import webbrowser as wb
from PIL import Image
#from PIL import ImageTk
#import tkinter
#import tkinter as tk
import os, sys



def acceso_web():
    #url = wb.open('ecard.center/index/express_checkout/index.php')
    url = wb.open('https://ecard.center/index/express_checkout/index.php')



ventana= tk.Tk()
ventana.title("Boton de Pago")
ventana.geometry("350x150")
imagen = ImageTk.PhotoImage(Image.open("logologin.jpeg"))
boton = tk.Button(ventana,image =imagen,command=acceso_web)
boton.place(x=10, y=10)
ventana.mainloop()
