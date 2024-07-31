import re

# Lista para almacenar los pedidos
pedidos = []

# Función para mostrar el menú
def mostrar_menu():
    print("Menú de opciones:")
    print("1. Registrar nuevo pedido")
    print("2. Visualizar todos los pedidos")
    print("3. Ver detalle de un pedido")
    print("4. Salir")

# Función para validar entrada de números
def validar_numero(mensaje, longitud_maxima):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit() and len(entrada) <= longitud_maxima:
            return entrada
        else:
            print(f"Entrada inválida. Debe ser un número con máximo {longitud_maxima} dígitos.")

# Función para validar entrada de texto
def validar_texto(mensaje, min_longitud, max_longitud):
    while True:
        entrada = input(mensaje)
        if re.match("^[a-zA-Z]{3,10}$", entrada) and min_longitud <= len(entrada) <= max_longitud:
            return entrada
        else:
            print(f"Entrada inválida. Debe tener entre {min_longitud} y {max_longitud} caracteres y no contener números.")

# Función para registrar un nuevo pedido
def registrar_pedido():
    print("Registrar nuevo pedido")

    nombre_cliente = validar_texto("Ingrese el nombre del cliente: ", 3, 10)
    apellido_cliente = validar_texto("Ingrese el apellido del cliente: ", 3, 10)
    telefono_cliente = validar_numero("Ingrese el teléfono del cliente: ", 10)
    nombre_policrush = validar_texto("Ingrese el nombre de la policrush: ", 3, 10)
    apellido_policrush = validar_texto("Ingrese el apellido de la policrush: ", 3, 10)
    telefono_policrush = validar_numero("Ingrese el teléfono de la policrush: ", 10)
    dependencia_policrush = validar_texto("Ingrese la dependencia de la policrush: ", 5, 15)

    print("Seleccione el regalo:")
    print("1. Poliflor + Polipeluche ($2.50)")
    print("2. Poliflor + Policarta ($1.50)")
    print("3. Poliflor + Polillavero ($2.00)")
    print("4. Poliflor + Polivaso ($2.75)")
    
    regalo_opcion = validar_numero("Ingrese la opción del regalo (1-4): ", 1)
    regalo_opciones = {
        '1': 2.50,
        '2': 1.50,
        '3': 2.00,
        '4': 2.75
    }
    
    if regalo_opcion in regalo_opciones:
        precio_base = regalo_opciones[regalo_opcion]
        precio_final = precio_base * 1.10  # Agregar 10% extra
        codigo_pedido = validar_numero("Ingrese un código de pedido (máximo 4 dígitos): ", 4)

        pedido = {
            "codigo": codigo_pedido,
            "nombre_cliente": nombre_cliente,
            "apellido_cliente": apellido_cliente,
            "telefono_cliente": telefono_cliente,
            "nombre_policrush": nombre_policrush,
            "apellido_policrush": apellido_policrush,
            "telefono_policrush": telefono_policrush,
            "dependencia_policrush": dependencia_policrush,
            "regalo_opcion": regalo_opcion,
            "precio_final": precio_final
        }

        pedidos.append(pedido)
        print("Pedido registrado exitosamente.")
    else:
        print("Opción de regalo no válida.")

# Función para visualizar todos los pedidos
def visualizar_pedidos():
    if pedidos:
        print("Listado de pedidos:")
        for pedido in pedidos:
            print(pedido)
    else:
        print("No existen pedidos registrados.")

# Función para ver el detalle de un pedido
def ver_detalle_pedido():
    codigo_pedido = validar_numero("Ingrese el código del pedido a buscar: ", 4)
    pedido_encontrado = None

    for pedido in pedidos:
        if pedido["codigo"] == codigo_pedido:
            pedido_encontrado = pedido
            break

    if pedido_encontrado:
        print("Detalle del pedido:")
        print(pedido_encontrado)
    else:
        print("Pedido no encontrado.")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = validar_numero("Ingrese una opción (1-4): ", 1)

        if opcion == '1':
            registrar_pedido()
        elif opcion == '2':
            visualizar_pedidos()
        elif opcion == '3':
            ver_detalle_pedido()
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
