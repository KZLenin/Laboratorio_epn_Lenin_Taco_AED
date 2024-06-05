def calcular_impuesto(vehiculos, porcentaje_impuesto):
    impuestos = [valor * porcentaje_impuesto for valor in vehiculos]
    total_impuestos = sum(impuestos)
    return impuestos, total_impuestos

def main():
    vehiculos = {
        1: [],
        2: [],
        3: []
    }

    total_vehiculos = int(input("Ingrese la cantidad total de vehículos: "))

   
    for i in range(total_vehiculos):
        clave = int(input(f"Ingrese la clave del vehículo {i+1} : "))
        while clave not in [1, 2, 3]:
            print("Clave inválida. Por favor, ingrese una clave válida .")
            clave = int(input(f"Ingrese la clave del vehículo {i+1} : "))
        valor = float(input(f"Ingrese el valor del vehículo {i+1}: "))
        vehiculos[clave].append(valor)

    total_impuestos_por_categoria = {}
    total_impuestos = 0


    for clave, valores in vehiculos.items():
        if clave == 1:
            porcentaje_impuesto = 0.10
        elif clave == 2:
            porcentaje_impuesto = 0.07
        elif clave == 3:
            porcentaje_impuesto = 0.05

        impuestos, total_categoria = calcular_impuesto(valores, porcentaje_impuesto)
        total_impuestos_por_categoria[clave] = total_categoria
        total_impuestos += total_categoria

        print(f"\nVehículos con clave {clave}:")
        for i, valor in enumerate(valores):
            print(f" - Vehículo {i+1}: Valor = {valor}, Impuesto = {impuestos[i]}")

        print(f"Total de impuestos para vehículos con clave {clave}: {total_categoria}")

    print(f"\nTotal de impuestos para todos los vehículos: {total_impuestos}")

if __name__ == "__main__":
    main()
