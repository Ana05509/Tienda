import tkinter as tk
from tkinter import messagebox
from django.contrib.auth import authenticate
import os
import django

# Inicializar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_ventas.settings")
django.setup()

# Importar modelos de Django
from ventas.models import Producto

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Sistema de Ventas")

        # Widgets de login
        tk.Label(root, text="Usuario:").grid(row=0, column=0)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1)

        tk.Label(root, text="Contraseña:").grid(row=1, column=0)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_btn = tk.Button(root, text="Iniciar Sesión", command=self.login)
        self.login_btn.grid(row=2, column=1)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = authenticate(username=username, password=password)
        if user is not None:
            self.root.destroy()  # Cerrar ventana de login
            main_app = tk.Tk()  # Abrir la aplicación principal
            SistemaVentasApp(main_app)
            main_app.mainloop()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")


class SistemaVentasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Ventas")

        # Etiquetas y entradas para productos
        tk.Label(root, text="Nombre del Producto:").grid(row=0, column=0)
        self.producto_entry = tk.Entry(root)
        self.producto_entry.grid(row=0, column=1)

        tk.Label(root, text="Precio:").grid(row=1, column=0)
        self.precio_entry = tk.Entry(root)
        self.precio_entry.grid(row=1, column=1)

        tk.Label(root, text="Stock:").grid(row=2, column=0)
        self.stock_entry = tk.Entry(root)
        self.stock_entry.grid(row=2, column=1)

        # Botones CRUD
        self.agregar_btn = tk.Button(root, text="Agregar Producto", command=self.agregar_producto)
        self.agregar_btn.grid(row=3, column=0)

        self.actualizar_btn = tk.Button(root, text="Actualizar Producto", command=self.actualizar_producto)
        self.actualizar_btn.grid(row=3, column=1)

        self.eliminar_btn = tk.Button(root, text="Eliminar Producto", command=self.eliminar_producto)
        self.eliminar_btn.grid(row=4, column=0)

    def agregar_producto(self):
        nombre = self.producto_entry.get()
        precio = float(self.precio_entry.get())
        stock = int(self.stock_entry.get())

        try:
            Producto.objects.create(nombre=nombre, precio=precio, stock=stock)
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar el producto: {e}")

    def actualizar_producto(self):
        # Similar a agregar_producto(), pero busca un producto existente y lo actualiza.
        pass

    def eliminar_producto(self):
        # Similar a agregar_producto(), pero elimina un producto por su nombre.
        pass

# Ejecución
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
