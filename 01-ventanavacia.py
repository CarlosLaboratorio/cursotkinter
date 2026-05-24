import tkinter as tk

#1. Crear la raíz. La instancia principal.
root = tk.Tk()
root.title('Mi primera GUI')

#2. Crear un componente
etiqueta = tk.Label(root,text="Practicando de nuevo Tkinter").pack()
#etiqueta.pack()

#3. Iniciar la app. Mantener la ventana abierta.
root.mainloop()


#No llames tkinter.py a tus archivos ya que es un nombre reservado.
#Puedes probar si tienes tkinter abriendo el cmd y escribiendo el código python -m tkinter
#carlosmasterweb.github.io/cursos.html