
# Inicialización de listas paralelas
nombres = []
cantidades = []

# Variable de control del bucle principal
salir = False

while not salir:
    print("Menú de opciones:")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue
        nombres.append(nombre)
        cantidades.append(cantidad)
        print("Producto agregado con éxito.")

    elif opcion == "2":
        print("Productos agotados:")
        agotados = False
        for i in range(len(nombres)):
            if cantidades[i] == 0:
                print(f"- {nombres[i]}")
                agotados = True
        if not agotados:
            print("No hay productos agotados.")

    elif opcion == "3":
        producto = input("Ingrese el nombre del producto a actualizar: ")
        if producto in nombres:
            index = nombres.index(producto)
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                if nueva_cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    continue
                cantidades[index] = nueva_cantidad
                print("Stock actualizado.")
            except ValueError:
                print("Por favor ingrese un número válido.")
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        print("Listado de productos:")
        if len(nombres) == 0:
            print("No hay productos registrados.")
        else:
            for i in range(len(nombres)):
                print(f"{nombres[i]}: {cantidades[i]} unidades")

    elif opcion == "5":
        print("Gracias por usar el sistema.")
        salir = True

    else:
        print("Opción inválida. Intente nuevamente.")
