import os

def mostrar_menu():
    print("MENU")
    print("1. Ingresar calificaciones")
    print("2. Mostrar calificaciones de menor a mayor")
    print("3. Mostrar calificaciones de mayor a menor")
    print("4. Mostrar detalles de calificaciones")
    print("5. Guardar calificaciones en archivo")
    print("6. Mostrar calificaciones desde archivo")
    print("7. Salir")

def ingresar_calificaciones():
    calificaciones = []
    n = int(input("Ingrese el número de calificaciones: "))

    for _ in range(n):
        while True:
            try:
                calificacion = int(input("Ingrese la calificación (0-20): "))
                if 0 <= calificacion <= 20:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("Calificación inválida. Debe estar entre 0 y 20.")
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")
    
    return calificaciones

def mostrar_calificaciones(calificaciones, ascendente=True):
    calificaciones_ordenadas = sorted(calificaciones) if ascendente else sorted(calificaciones, reverse=True)
    print("Calificaciones:", " ".join(map(str, calificaciones_ordenadas)))

def mostrar_detalles(calificaciones):
    if not calificaciones:
        print("No hay calificaciones ingresadas.")
        return

    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)
    aprobados = sum(1 for cal in calificaciones if 14 <= cal <= 20)
    suspenso = sum(1 for cal in calificaciones if 9 <= cal <= 13)
    reprobados = sum(1 for cal in calificaciones if 1 <= cal <= 8)

    print(f"Promedio: {promedio:.2f}")
    print(f"Aprobados: {aprobados}")
    print(f"Suspenso: {suspenso}")
    print(f"Reprobados: {reprobados}")

def guardar_calificaciones_en_archivo(calificaciones):
    with open("reporte.txt", "w") as archivo:
        for cal in calificaciones:
            archivo.write(f"{cal}\n")
    print("Calificaciones guardadas en reporte.txt")

def mostrar_calificaciones_desde_archivo():
    if not os.path.exists("reporte.txt"):
        print("El archivo reporte.txt no existe.")
        return

    with open("reporte.txt", "r") as archivo:
        calificaciones = archivo.readlines()
    
    if calificaciones:
        print("Calificaciones en archivo:", " ".join(cal.strip() for cal in calificaciones))
    else:
        print("No hay calificaciones en el archivo.")

def main():
    calificaciones = []
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            calificaciones = ingresar_calificaciones()
        elif opcion == 2:
            mostrar_calificaciones(calificaciones, ascendente=True)
        elif opcion == 3:
            mostrar_calificaciones(calificaciones, ascendente=False)
        elif opcion == 4:
            mostrar_detalles(calificaciones)
        elif opcion == 5:
            guardar_calificaciones_en_archivo(calificaciones)
        elif opcion == 6:
            mostrar_calificaciones_desde_archivo()
        elif opcion == 7:
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
