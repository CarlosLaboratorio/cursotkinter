import tkinter as tk    #Importamos la libreria Tkinter

#Función que se ejecuta al cerrar la ventanas
def al_cerrar():
    print("Limpiando datos antes de salir...")
    root.destroy()  #Cierra la ventana correctamente
    
    
#Crear la ventana principal
root = tk.Tk()

#Detecta cuando se presiona la X de la ventana y ejecuta la función personalizada
root.protocol('WM_DELETE_WINDOW', al_cerrar)

#Mantiene ventana abierta
root.mainloop()