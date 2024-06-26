#Ejercicio 2(pg 139 ejercicio 4.18).....(°0°)
def ejercicio_2():
    def calculo_del_interes():
        año_inicial=1961
        capital=1500
        interes=0.15
        año_actual=int(input(" Ingrese el año actual: "))
        n_año=año_actual-año_inicial
        invercion_actual=round(capital*(pow((1+interes),n_año)),2)
        return invercion_actual,capital,n_año,interes
    def imprecion():
        print("\n----------BIENVENIDO----------")
        invercion_actual,capital,n_año,interes=calculo_del_interes()
        print(f" Valor del capital: $ {capital}")
        print(f" Valor del interes: {interes*100}%")
        print(f" cantidad de años de interes: {n_año}")
        print(f" El valor actual de la inversion: $ {invercion_actual} \n")
    imprecion()
# Ejercicio 3(pg 169 ejercicio 5.17 ).....(0-0)
def ejercicio_3():
    def leer_datos_choferes():
        choferes = []
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
        for i in range(5):
            nombre = input(f"Ingrese el nombre del chofer {i+1}: ")
            sueldo_por_hora = float(input(f"Ingrese el sueldo por hora de {nombre}: "))
            horas_trabajadas = []
            for j in range(6):
                horas = float(input(f"Ingrese las horas trabajadas por {nombre} el {dias_semana[j]}: "))
                horas_trabajadas.append(horas)
            chofer = {
                "nombre": nombre,
                "sueldo_por_hora": sueldo_por_hora,
                "horas_trabajadas": horas_trabajadas
            }
            choferes.append(chofer)
        return choferes
    def calcular_horas_totales(chofer):
        return sum(chofer["horas_trabajadas"])
    def calcular_sueldo_semanal(chofer):
        return calcular_horas_totales(chofer) * chofer["sueldo_por_hora"]
    def calcular_total_pagado(choferes):
        total_pagado = 0
        for chofer in choferes:
            total_pagado += calcular_sueldo_semanal(chofer)
        return total_pagado
    def chofer_mas_horas_lunes(choferes):
        max_horas = -1
        nombre_chofer = ""
        for chofer in choferes:
            if chofer["horas_trabajadas"][0] > max_horas:  # Lunes es el primer día
                max_horas = chofer["horas_trabajadas"][0]
                nombre_chofer = chofer["nombre"]
        return nombre_chofer
    def imprimir_reporte(choferes):
        print("\n----- REPORTE SEMANAL DE CHOFERES -----")
        for chofer in choferes:
            nombre = chofer["nombre"]
            horas_totales = calcular_horas_totales(chofer)
            sueldo_semanal = calcular_sueldo_semanal(chofer)
            print(f"Nombre: {nombre}")
            print(f"  Horas trabajadas en la semana: {horas_totales}")
            print(f"  Sueldo semanal: ${sueldo_semanal:.2f}")
        total_pagado = calcular_total_pagado(choferes)
        print(f"\nTotal a pagar por la empresa: ${total_pagado:.2f}")
        chofer_lunes = chofer_mas_horas_lunes(choferes)
        print(f"El chofer que más horas trabajó el lunes es: {chofer_lunes}")
    def main():
        choferes = leer_datos_choferes()
        imprimir_reporte(choferes)
    if __name__ == "__main__":
        main()
# hacemos el llamado a las dos funciones como si fuera un progrma.....
def menu_de_opciones():
    print("                Menu de opciones                   ")
    print(" 1.- Ejercicio 1 (pg 139 ejercicio 4.18).")
    print(" 2.- Ejercicio 2 (pg 169 ejercicio 5.17).")
    print(" 3.- Salir del programa.")
    opcion= int(input(" Ingrese una opcion: "))
    return opcion
def main():
    print("\n-------------------EPN-------------------------")
    print("                  Bienvenido                   ")
    opcion=0
    while opcion!=3:
        opcion=menu_de_opciones()
        if opcion == 1:
            ejercicio_2()
        elif opcion == 2:
            ejercicio_3()
        elif opcion == 3:
            print(" Gracias por su atencion....\n Que tenga un gran Dia/noche.....(0w*)\n")
        else:
            print("Opción no válida, por favor intente de nuevo.\n")
main()

