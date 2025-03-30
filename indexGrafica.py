from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def calcular():
    """Calcula la cantidad de paneles solares necesarios y el retorno de inversión"""
    try:
        consumo_mensual = float(entry_consumo.get())
        irradiacion = float(entry_irradiacion.get())
        potencia_panel = float(entry_potencia_panel.get())
        costo_sistema = float(entry_costo_sistema.get())
        costo_unitarioCuv = float(entry_costo_unitario.get())

        # Cálculos
        consumo_diario = consumo_mensual / 30
        potencia_requerida = consumo_diario / irradiacion
        num_paneles = potencia_requerida / (potencia_panel / 1000)
        ahorro_anual = consumo_mensual * costo_unitarioCuv * 12
        retorno_inversion = costo_sistema / ahorro_anual

        resultado.set(f"⚡ Consumo diario: {consumo_diario:.2f} KWH\n"
                      f"🔋 Potencia requerida: {potencia_requerida:.2f} KW\n"
                      f"☀️ Número de paneles: {int(np.ceil(num_paneles))}\n"
                      f"💰 Ahorro anual: ${ahorro_anual:,.2f} COP\n"
                      f"💰 Retorno de inversión: {retorno_inversion:.2f} años")
    except ValueError:
        messagebox.showerror(" Error", "Ingrese valores numéricos válidos")

def graficar():
    """gráfico con los consumos ingresados y muestra el promedio"""
    try:
        meses = ["Dic", "Nov", "Oct", "Sep", "Ago", "Jul"]
        consumos = [float(entry.get()) for entry in entries_consumo]

        promedio = sum(consumos) / len(consumos)  # Calcula el promedio

        plt.figure(figsize=(8, 5))
        plt.bar(meses, consumos, color='blue', alpha=0.7, label="Consumo mensual")
        plt.axhline(promedio, color='red', linestyle='dashed', label=f'Promedio {promedio:.2f} KWH')
        
        plt.xlabel("Meses")
        plt.ylabel("Consumo (KWH)")
        plt.title("Histórico de Consumo Energético")
        plt.legend()
        plt.xticks(rotation=45)
        plt.show()
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos para los consumos")

# Interfaz gráfica
root = tk.Tk()
root.title(" 💡Calculadora de Energia solar Fotovoltaica y paneles solares  ") 
root.geometry("450x600")

frame = tk.Frame(root)
frame.pack(pady=20)

# Entradas para cálculos fotovoltaicos
labels = ["Consumo mensual (KWH)", "Irradiación solar (HSP)", "Potencia panel (W)", 
          "Costo del sistema ($)", "Costo unitario de electricidad ($/KWH)"]
entries = []

for lbl in labels:
    tk.Label(frame, text=lbl).pack()
    entry = ttk.Entry(frame)
    entry.pack()
    entries.append(entry)

entry_consumo, entry_irradiacion, entry_potencia_panel, entry_costo_sistema, entry_costo_unitario = entries

resultado = tk.StringVar() 
tk.Label(frame, textvariable=resultado, fg='green').pack()


ttk.Button(frame, text="⚙️ Calcular", command=calcular).pack(pady=5)

# Sección para graficar consumos mensuales
tk.Label(frame, text="Ingrese consumos mensuales (KWH)").pack()
entries_consumo = []
for mes in ["Dic", "Nov", "Oct", "Sep", "Ago", "Jul"]:
    tk.Label(frame, text=mes).pack()
    entry = ttk.Entry(frame)
    entry.pack()
    entries_consumo.append(entry)


ttk.Button(frame, text=" 📊 Graficar Consumo", command=graficar).pack(pady=5)

root.mainloop()