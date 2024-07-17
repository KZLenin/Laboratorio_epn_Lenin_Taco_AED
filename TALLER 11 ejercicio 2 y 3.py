# ejercicio 1
def ejercicio_1():
    N = int(input("\n Ingrese el número de focos: "))

    contadorVerde = 0
    contadorBlanco = 0
    contadorRojo = 0

    for i in range(N):
        color = input("Ingrese el color del foco (verde, blanco, rojo): ").strip().lower()
        
        if color == "verde":
            contadorVerde += 1
        elif color == "blanco":
            contadorBlanco += 1
        elif color == "rojo":
            contadorRojo += 1

    print("Focos verdes:", contadorVerde)
    print("Focos blancos:", contadorBlanco)
    print("Focos rojos:", contadorRojo)
    N = int(input("Ingrese el número de focos: "))
# ejercicio 2
def ejercicio_2():
    def es_matriz_diagonal(matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        # Verificar si la matriz es cuadrada
        if filas != columnas:
            return False
        for i in range(filas):
            for j in range(columnas):
                if i != j and matriz[i][j] != 0:
                    return False
        return True
    n = int(input("Ingrese el tamaño de la matriz (n x n): "))
    # Inicializar la matriz
    matriz = []
    print("Ingrese los elementos de la matriz:")
    for i in range(n):
        fila = []
        for j in range(n):
            elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
            fila.append(elemento)
        matriz.append(fila)
    if es_matriz_diagonal(matriz):
        print("La matriz es diagonal.")
    else:
        print("La matriz no es diagonal.")
def MENU():
    print(" Menu de opciones:")
    print("\n 1.- Ejecicio 1.(pagina 138, ejercicio 4.4)")
    print(" 2.- Ejecicio 2.(pagina 168, ejercicio 5.5)")
    print(" 3.- Salir")
    opcion = input("\n Ingrese una opcion: ")
    return int(opcion)
def main():
    print("\n-------------------EPN-------------------------")
    print("                  Bienvenido                   ")
    opcion = 0
    while opcion != 3:
        opcion = MENU()
        if opcion == 1:
            ejercicio_1()
        elif opcion == 2:
            ejercicio_2()
        elif opcion == 3:
            print("Gracias por su atención....\nQue tenga un gran Día/noche.....(0w*)\n")
        else:
            print("Opción no válida, por favor intente de nuevo.\n")
main()