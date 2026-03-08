

import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.geometry('800x400')
root.title("Northwind Management")

# Crear el widget Notebook (pestañas)
notebook = ttk.Notebook(root)

# Crear los frames que irán dentro de las pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)

# Añadir las pestañas al Notebook
notebook.add(tab1, text="formulario de clientes")
notebook.add(tab2, text="Formulario de abogado")
notebook.add(tab3, text="Formulario de casos")
notebook.add(tab4, text="Formulario de empleado")

# Empaquetar el Notebook para que se muestre en la ventana
notebook.pack(expand=True, fill="both")

# CONTENIDO DE LA PESTAÑA 1 (PRODUCTS)
# Título
titulo = tk.Label(tab1, text="FORMULARIO CLIENTES ",font=("Arial", 16, "bold"),fg="magenta")
titulo.pack(pady=20)

# Frame para contener el formulario
form_frame = tk.Frame(tab1)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1: ProductID
tk.Label(form_frame, text="Cliente ID", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1, )
CustomerID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: ProductName
tk.Label(form_frame, text="nombre:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
ProductName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ProductName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: SupplierID
tk.Label(form_frame, text="Sector:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierID.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: CategoryID
tk.Label(form_frame, text="correo:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
CategoryID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CategoryID.grid(row=4, column=1, sticky="w", pady=10)


# Fila 6: Price
tk.Label(form_frame, text="Telofono", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Price = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Price.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: Price
tk.Label(form_frame, text="referido", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
Price = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
Price.grid(row=6, column=1, sticky="w", pady=10)

# Frame para botones
button_frame = tk.Frame(tab1)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear.pack(side=tk.LEFT, padx=5)

# CONTENIDO DE LA PESTAÑA 2 (CUSTOMERS)
titulo2 = tk.Label(tab2, text="Formulario de abogados", font=("Arial", 16, "bold"), fg="green")
titulo2.pack(pady=20)

form_frame = tk.Frame(tab2)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1: Nombre
tk.Label(form_frame, text="nombre:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: Apellido
tk.Label(form_frame, text="apellido", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: Telefono
tk.Label(form_frame, text="telefono:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: Especialidad
tk.Label(form_frame, text="Especialidad", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Tarifa hora
tk.Label(form_frame, text="TarifaHora", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: Disponibilidad 
tk.Label(form_frame, text="Disponibilidad", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: Experiencia
tk.Label(form_frame, text="Experiencia", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=7, column=1, sticky="w", pady=10)


# Frame para botones 
button_frame = tk.Frame(tab2)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear.pack(side=tk.LEFT, padx=5)




# PESTAÑA 3 casos
titulo3 = tk.Label(tab3, text="Formulario de casos", font=("Arial", 16, "bold"), fg="blue")
titulo3.pack(pady=20)


form_frame3 = tk.Frame(tab3)
form_frame3.pack(pady=20, anchor="w", padx=50)

tk.Label(form_frame3, text= "numerocaso", font=("ARIAL", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=1, column=1, sticky="w", pady=10)

tk.Label(form_frame3, text= "CASO", font=("ARIAL", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form_frame3, text= "RamaDerecho", font=("ARIAL", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=3, column=1, sticky="w", pady=10)

tk.Label(form_frame3, text= "FechaApertura", font=("ARIAL", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=4, column=1, sticky="w", pady=10)

tk.Label(form_frame3, text= "Cliente", font=("ARIAL", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=5, column=1, sticky="w", pady=10)

tk.Label(form_frame3, text= "Fecha-conclusion", font=("ARIAL", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=6, column=1, sticky="w", pady=10)


button_frame = tk.Frame(tab3)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear.pack(side=tk.LEFT, padx=5)

#pestaña 4


# CONTENIDO DE LA PESTAÑA 1 (PRODUCTS)
# Título
titulo = tk.Label(tab4, text="FORMULARIO Empleados ",font=("Arial", 16, "bold"),fg="magenta")
titulo.pack(pady=20)

# Empaquetar el Notebook para que se muestre en la ventana
notebook.pack(expand=True, fill="both")

# Frame para contener el formulario
form_frame4 = tk.Frame(tab4)
form_frame4.pack(pady=20, anchor="w", padx=50)


tk.Label(form_frame4, text= "Empleado ID", font=("ARIAL", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=1, column=1, sticky="w", pady=10)

tk.Label(form_frame4, text= "Nombre", font=("ARIAL", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form_frame4, text= "Telefono", font=("ARIAL", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=3, column=1, sticky="w", pady=10)

tk.Label(form_frame4, text= "Cargo", font=("ARIAL", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=4, column=1, sticky="w", pady=10)

tk.Label(form_frame4, text= "Correo", font=("ARIAL", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=5, column=1, sticky="w", pady=10)




root.mainloop()vvvvvvvvv
