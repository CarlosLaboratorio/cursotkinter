import tkinter as tk
root = tk.Tk()
root.title("Ventana Centrada")

#Tamaño de la ventana
ancho_ventana = 600
alto_ventana = 400

#Obtener tamaño de la pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

#Calcular posición centrada
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2

#Aplicar tamaño y posición
root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
root.attributes("-alpha",0.9)    #Aplica leve transparencia
root.attributes("-topmost",True) #Muestra la ventana al frente de todo

root.mainloop()