# ejercicio del departamento de quimica......(0w0)
# login y verificacion...
def verificacion_y_login():
    while True:
        usuario = input(" Ingrese tu usuario: ")
        password = input(" Ingrese tu password: ")
        if usuario == "Admin" and password == "Secret*":
            break
        else:
            print("------------Error-----------")
            print(" Usuario o contraseña incorrectos. \n Intente de nuevo.")
    return usuario
# menu de opciones....
def menu_de_opciones(usuario):
    print(f"-----------------BIENVENIDO {usuario} -----------------")
    print("-----------------MENU DE OPCIONES-----------------")
    print("1.- Grados centígrados a grados Fahrenheit.")
    print("2.- Grados kelvin a grados centígrados.")
    print("3.- Salir del programa.")
    opcion = int(input("Ingrese la opcion: "))
    return opcion
# tranformacion de °C a°F
def centigrados_a_fahrenheit():
    centigrado = float(input("Ingrese el valor en Centigrados: "))
    ecuacion_a_fahrenheit = ((9/5) * centigrado) + 32
    print(f"El valor en Fahrenheit es: {ecuacion_a_fahrenheit} °F")
# 
def kelvin_a_centigrados():
    kelvin = float(input("Ingrese el valor en Kelvin: "))
    ecuacion_a_centigrado = kelvin - 273.15
    print(f"El valor en centigrados es: {ecuacion_a_centigrado} °C")
def salida_del_programa():
    print("Final del programa..\nGracias por su atención...\nLindo día/noche...")
def main():
    print("\n-------------------EPN-------------------------")
    usuario = verificacion_y_login()
    opcion = 0
    while opcion != 3:
        opcion = menu_de_opciones(usuario)
        if opcion == 1:
            centigrados_a_fahrenheit()
        elif opcion == 2:
            kelvin_a_centigrados()
        elif opcion == 3:
            salida_del_programa()
        else:
            print("Opción no válida, por favor intente de nuevo.")
            
main()