from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def calcular():
    try:
        consumo_mensual = float(entry_consumo.get())
        irradiacion = float(entry_irradiacion.get())
        potencia_panel = float(entry_potencia_panel.get())
        costo_sistema = float(entry_costo_sistema.get())
        costo_unitarioCuv = float(entry_costo_unitario.get())
        
        
        consumo_diario = consumo_mensual / 30
        potencia_requerida = consumo_diario / irradiacion
        num_paneles = potencia_requerida / (potencia_panel / 1000)
        ahorro_anual = consumo_mensual * costo_unitarioCuv * 12
        retorno_inversion = costo_sistema / ahorro_anual
        
        resultado.set(f"Consumo diario: {consumo_diario:.2f} KWH\n"
                      f"Potencia requerida: {potencia_requerida:.2f} KW\n"
                      f"Número de paneles: {int(np.ceil(num_paneles))}\n"
                      f"Retorno de inversión: {retorno_inversion:.2f} años")
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")

def graficar():
    meses = ["Enero", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    consumo = np.random.uniform(30, 60, 12)
    
    plt.figure(figsize=(8, 5))
    plt.bar(meses, consumo, color='blue', alpha=0.7)
    plt.xlabel("Meses")
    plt.ylabel("Consumo (KWH)")
    plt.title("Consumo Energético Anual")
    plt.xticks(rotation=45)
    plt.show()
  

# Interfaz gráfica
root = tk.Tk()
root.title("Calculadora Fotovoltaica")
root.geometry("400x400")
 


frame = tk.Frame(root)
frame.pack(pady=20)


labels = ["Consumo mensual (KWH)", "Irradiación solar (HSP)", "Potencia panel (W)", "Costo del sistema ($)" ]
entries = []

for lbl in labels:
    tk.Label(frame, text=lbl).pack()
    entry = ttk.Entry(frame)
    entry.pack()
    entries.append(entry)

entry_consumo, entry_irradiacion, entry_potencia_panel, entry_costo_sistema,entry_costo_unitario = entries

resultado = tk.StringVar() 
tk.Label(frame, textvariable=resultado, fg='green').pack()



ttk.Button(frame, text="Calcular", command=calcular).pack(pady=5)
tk.Button(frame, text="Ver Gráfico", command=graficar).pack()

root.mainloop()
