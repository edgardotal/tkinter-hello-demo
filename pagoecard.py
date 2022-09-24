import os, sys
from os import path
import webbrowser as wb
from tkinter import * as tk
import tkinter as tk
from PIL import *

def acceso_web():
    #url = wb.open('ecard.center/index/express_checkout/index.php')
    url = wb.open('https://ecard.center/index/express_checkout/index.php')

ventana = tk()
ventana.title("Boton de Pago")
ventana.geometry("350x150")
imagen = PhotoImage(Image.open("logologin.jpeg"))
boton = tk.Button(ventana,image =imagen,command=acceso_web)
boton.place(x=10, y=10)
ventana.mainloop()
