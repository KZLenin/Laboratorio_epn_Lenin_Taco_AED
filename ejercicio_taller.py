import random
import webbrowser

nombres = []
huellas = []
codigos = []
numPersonas = 0

def menu_opciones():
    while True:
        print("¿Qué acción desea realizar?: ")
        print('*  1) Ingresar usuarios')
        print('*  2) Mostrar usuarios')
        print('*  3) Buscar y enviar código de recuperación')
        print('*  4) Salir del sistema')
        try:
            opcion = int(input("Ingrese la opción: "))
            if opcion in [1, 2, 3, 4]:
                return opcion
            else:
                print("Por favor, ingrese una opción válida (1, 2, 3 o 4).")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def ingreso_personal(numPersonas):
    for i in range(numPersonas):
        print("Ingrese los datos de la persona", i + 1)
        while True:
            nombreUsuario = input("Nombre: ")
            if nombreUsuario.isalpha():
                break
            else:
                print("El nombre no puede contener números ni caracteres especiales.")
        
        huellaUsuario = input("Huella: ")
        nombres.append(nombreUsuario)
        huellas.append(huellaUsuario)
        codigos.append(random.randrange(1000, 9999))

def mostrar_registros():
    for i in range(len(nombres)):
        print("-------------------------------------")
        print("Mostrando los datos de la persona", i + 1)
        print("* Nombre:", nombres[i])
        print("* Huella dactilar:", huellas[i])
        print("* Código de acceso: ", codigos[i])
        print("-------------------------------------")

def buscarEnviarCodigo(nombreUsuario):
    if nombreUsuario in nombres:
        indice = nombres.index(nombreUsuario)
        print("Usuario encontrado")
        print("Desea enviar el código a su número de teléfono")
        opcion = input("Ingrese si o no: ")
        if opcion.lower() == "si":
            num = input("Ingrese el número de teléfono: ")
            url = f'https://api.whatsapp.com/send?phone={num}&text=El código de recuperación es: {codigos[indice]}'
            webbrowser.open(url)
    else:
        print("No existe ese usuario registrado")

def validar_num_personas():
    while True:
        try:
            numPersonas = int(input("Ingrese el número de personas a registrar (1-20): "))
            if 1 <= numPersonas <= 20:
                return numPersonas
            else:
                print("Por favor, ingrese un número en el rango de 1 a 20.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def main():
    print("--------------- SISTEMA DACTILAR -------------")
    print("------------------- Bienvenid@ -------------------")
    
    while True:
        caso = menu_opciones()
        
        if caso == 1:
            numPersonas = validar_num_personas()
            ingreso_personal(numPersonas)
        
        elif caso == 2:
            mostrar_registros()
        
        elif caso == 3:
            personaBuscar = input("Ingrese nombre de la persona a enviar el código: ")
            buscarEnviarCodigo(personaBuscar)

        elif caso == 4:
            print("Muchas gracias")
            break

main()
