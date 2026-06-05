"""
Hello World App - Tkinter Demo
Aplicación básica de escritorio con interfaz gráfica
Autor: Edgardo Talavera
"""

import tkinter as tk
from tkinter import ttk

class HelloApp:
    """Aplicación simple de saludo con Tkinter"""
    
    def __init__(self):
        # Ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Hello World - Tkinter Demo")
        self.ventana.geometry("400x300")
        self.ventana.resizable(True, True)
        
        # Frame principal
        self.frame = tk.Frame(self.ventana, relief=tk.RIDGE, borderwidth=2)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Etiqueta
        self.label = tk.Label(
            self.frame, 
            text="Hello, World!", 
            font=("Arial", 24),
            fg="blue"
        )
        self.label.pack(fill=tk.X, expand=True, pady=20)
        
        # Botón de salir
        self.boton_salir = tk.Button(
            self.frame,
            text="Salir",
            command=self.ventana.destroy,
            bg="red",
            fg="white",
            font=("Arial", 12)
        )
        self.boton_salir.pack(side=tk.BOTTOM, pady=10)
        
        # Mensaje en consola
        print("✅ Aplicación iniciada correctamente")
    
    def ejecutar(self):
        """Inicia el loop principal de la aplicación"""
        self.ventana.mainloop()

# Punto de entrada
if __name__ == "__main__":
    app = HelloApp()
    app.ejecutar()