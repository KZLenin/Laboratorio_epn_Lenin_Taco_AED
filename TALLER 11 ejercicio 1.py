# Ejercicio 1 
from os import system
import random
import re


datosBiometricos = [[],[],[]]
numeroPersonas = 0

def validarNombre(input_str, mensaje_error):
    while True:
        nombreUsuario = input(input_str)
        if nombreUsuario.strip() and re.match("^[A-Za-z]+$",nombreUsuario):
            return nombreUsuario
        else:
            print(mensaje_error)


def menudeOpciones():
    print("SISTEMA BIOMETRICO")
    print("------Bienvenid@------")
    print("Que accion desea realizar?")
    print("1.- Login")
    print("2.- Registro")
    print("3.- Recuperar clave")
    print("4.- Buscar usuario")
    print("5.- Salir")

def login():
    try:
        user = input("Ingrese el rostro de la persona: ")
        if user in datosBiometricos[1]:
            print("-----Bienvenid@-----")
            print("Acceso a los modulos")
            print("Que accion desea realizar?")
            print("3.- Cerrar sesion")
            input("Ingrese la opcion: ")
        else:
            print("No existe usuario")
    except Exception as e:
        print(f'Error durante el login {e}')

def registro():
    try:
        numeroPersonas = int(input("Ingrese el numero de personas: "))
        if (numeroPersonas >0 and numeroPersonas < 21):
            for i in range (numeroPersonas):
                print(f'Ingrese los datos de la persona {(i+1)}')
                nombreUsuario = validarNombre("Ingrese el nombre: ", "El nombre no puede estar vacio y solo debe contener letras")
                huellaUsuario = input("Ingrese la huella de usuario: ")
                datosBiometricos[0].append(nombreUsuario)
                datosBiometricos[1].append(huellaUsuario)
                datosBiometricos[2].append(random.randrange(1000,9999))
        else:
            print("Error en el ingreso de cantidad de personas")
    except Exception as e:
        print(f'Error durante el registro {e}')

def recuperarClave():
    try:
        print("-----Modelo de recuperacion-----")
        nombreUsuario = validarNombre("Ingrese el nombre: ", "El nombre no puede estar vacio y solo debe contener letras")
        if (nombreUsuario in datosBiometricos[0]):
            codigo = datosBiometricos[0].index(nombreUsuario)
            print(f'Codigo de {nombreUsuario} {datosBiometricos[2][codigo]}')
        else:
            print("No existe esa persona")
    except Exception as e:
        print(f'Error durante la recucperacion de la clave {e}')

def buscarUsuario():
    try: 
        print("--- Modulo de busqueda ---")
        nombreUsuario = validarNombre("Ingrese el nombre: ", "El nombre no puede estar vacio y solo debe contener letras")
        if (nombreUsuario in datosBiometricos[0]):
            indice = datosBiometricos[0].index(nombreUsuario)
            print(f'Huella de {nombreUsuario}: {datosBiometricos[1][indice]}')
            print(f'Codigo de {nombreUsuario}: {datosBiometricos[2][indice]}')
    except Exception as e:
        print(f'Error durante busqueda {e}')

def main ():
    while True:
        menudeOpciones()
        try:
            tipo = int(input("Ingrese la opcion a realizar: "))
            if (tipo == 5 ):
                break
            elif (tipo ==1):
                login()
            elif (tipo == 2):
                registro()
            elif (tipo == 3):
                recuperarClave()
            elif (tipo == 4):
                buscarUsuario()
            else:
                print("Opcion no valida, intente de nuevo")
        except ValueError:
            print("Ingrese un valor valido")
        except Exception as e:
            print(f'Error inesperado: {e}')
    print("---- Muchas gracias por usar nuestro sistema ----")
main()