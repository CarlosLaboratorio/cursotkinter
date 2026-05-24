import tkinter as tk

root = tk.Tk()
root.title("Mi primera ventana")

texto1 = tk.Label(root, text="Hola soy un Texto")
texto1.pack()

texto2 = tk.Label(root, text="Hola soy otro Texto")
texto2.pack()

root.mainloop()