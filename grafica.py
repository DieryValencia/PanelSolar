import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np

def calcular_promedio():
    try:
        consumos = [float(entry.get()) for entry in entry_list]
        promedio = sum(consumos) / len(consumos)
        consumo_mensual.set(f"Promedio: {promedio:.2f} KWH")
        return consumos, promedio
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")
        return None, None

def graficar():
    consumos, promedio = calcular_promedio()
    if consumos is None:
        return
    
    meses = ["Dic", "Nov", "Oct", "Sep", "Ago", "Jul"]
    meses.append("Prom")
    consumos.append(promedio)
    
    plt.figure(figsize=(8, 5))
    plt.bar(meses, consumos, color=['blue'] * 6 + ['red'], alpha=0.7)
    plt.xlabel("Meses")
    plt.ylabel("Consumo (KWH)")
    plt.title("Histórico de Consumo Energético")
    plt.xticks(rotation=45)
    plt.show()

# Interfaz gráfica
root = tk.Tk()
root.title("Histórico de Consumo Energético")
root.geometry("400x400")

tk.Label(root, text="Ingrese el consumo en KWH por mes").pack()

frame = tk.Frame(root)
frame.pack(pady=10)

entry_list = []
meses = ["Dic", "Nov", "Oct", "Sep", "Ago", "Jul"]

for mes in meses:
    tk.Label(frame, text=mes).grid(row=meses.index(mes), column=0)
    entry = ttk.Entry(frame)
    entry.grid(row=meses.index(mes), column=1)
    entry_list.append(entry)

consumo_mensual = tk.StringVar()
tk.Label(root, textvariable=consumo_mensual, fg='green').pack()

ttk.Button(root, text="Calcular y Graficar", command=graficar).pack(pady=5)

root.mainloop()
