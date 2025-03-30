import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np

# Función para calcular los valores
def calcular():
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
        
        # Mostrar resultado en la interfaz
        resultado.set(f"⚡ Consumo diario: {consumo_diario:.2f} KWH\n"
                      f"🔋 Potencia requerida: {potencia_requerida:.2f} KW\n"
                      f"☀️ Número de paneles: {int(np.ceil(num_paneles))}\n"
                      f"💰 Ahorro anual: ${ahorro_anual:,.2f} COP\n"
                      f"💰 Retorno de inversión: {retorno_inversion:.2f} años")
    except ValueError:
        messagebox.showerror("Error", "⚠️ Ingrese valores numéricos válidos.")

# Función para graficar el consumo energético
def graficar():
    meses = ["Enero", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    consumo = np.random.uniform(30, 60, 12)
    
    plt.figure(figsize=(8, 5))
    plt.bar(meses, consumo, color='#0078D7', alpha=0.7)  # Color azul moderno
    plt.xlabel("Meses")
    plt.ylabel("Consumo (KWH)")
    plt.title("Consumo Energético Anual")
    plt.xticks(rotation=45)
    plt.show()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora Fotovoltaica")
root.geometry("420x500")
root.configure(bg="#f0f0f0")  # Fondo gris claro

# Estilo de la interfaz
style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=5)

# Marco principal
frame = ttk.Frame(root, padding=15)
frame.pack(pady=10)

# Etiqueta de título
titulo = ttk.Label(frame, text="💡 Energia solar Fotovoltaica y paneles solares Calculadora y ", font=("Arial", 14, "bold"))
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Campos de entrada
labels = ["Consumo mensual (KWH):", "Irradiación solar (HSP):", "Potencia del panel (W):", "Costo del sistema ($):", "Costo unitario CUV ($):"]
entries = []

for i, lbl in enumerate(labels):
    ttk.Label(frame, text=lbl, font=("Arial", 10)).grid(row=i+1, column=0, sticky="w", padx=2, pady=1)
    entry = ttk.Entry(frame, width=20)
    entry.grid(row=i+1, column=1, padx=5, pady=3)
    entries.append(entry)

entry_consumo, entry_irradiacion, entry_potencia_panel, entry_costo_sistema, entry_costo_unitario = entries

# Contenedor para mostrar el resultado
result_frame = ttk.LabelFrame(root, text="Resultados", padding=10)
result_frame.pack(pady=10, padx=10, fill="both")

resultado = tk.StringVar()
label_resultado = ttk.Label(result_frame, textvariable=resultado, font=("Arial", 10), foreground="green", justify="left")
label_resultado.pack()

# Botones
btn_calcular = ttk.Button(root, text="⚙️ Calcular", command=calcular, style="TButton")
btn_calcular.pack(pady=5)

btn_graficar = ttk.Button(root, text="📊"
" Ver Gráfico", command=graficar, style="TButton")
btn_graficar.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
