import random
import tkinter as tk
from tkinter import messagebox

# Crear cartas con imágenes falsas
cartas = ["😀", "🤖", "🐍", "🚀", "🦄", "🎸"] * 2
random.shuffle(cartas)
cartas_seleccionadas = []

# Función para manejar la selección de cartas
def seleccionar_carta(boton, index):
    global cartas_seleccionadas
    if len(cartas_seleccionadas) < 2:
        boton.config(text=cartas[index], state="disabled")
        cartas_seleccionadas.append((boton, cartas[index]))
        if len(cartas_seleccionadas) == 2:
            ventana.after(1000, verificar_cartas)

# Verificar si las cartas seleccionadas coinciden
def verificar_cartas():
    global cartas_seleccionadas
    boton1, carta1 = cartas_seleccionadas[0]
    boton2, carta2 = cartas_seleccionadas[1]
    
    if carta1 == carta2:
        boton1.config(state="disabled")
        boton2.config(state="disabled")
    else:
        boton1.config(text="", state="normal")
        boton2.config(text="", state="normal")
    
    cartas_seleccionadas = []

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Juego de Memoria")
ventana.geometry("300x300")

botones = []
for i in range(12):
    boton = tk.Button(ventana, text="", width=10, height=3, command=lambda i=i: seleccionar_carta(botones[i], i))
    boton.grid(row=i//4, column=i%4)
    botones.append(boton)

ventana.mainloop()
