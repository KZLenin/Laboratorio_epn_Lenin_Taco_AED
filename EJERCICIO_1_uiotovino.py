#ejercicio para determinar las ganacias de la asosacion de vinicultores
#pedir informacion al ususario......
print("\n-------------------------------------------")
print("--------BIENVENIDO QUERIDO USUARIO--------\n ")
print("PROGRAMA PARA DETERMINAR LAS GANCIAS DEPENDIENDO\n DEL TIPO Y TAMAÑO....")
print("INGRESE LAS LETRAS EN MAYUSCULAS")
tipo=str(input("INGRESE QUE TIPO DE UVA (A o B):\n "))
print("INGRESE EL NUEMRO CORRESPONDIENTE")
tamaño=int(input("INGRESE QUE TAMAÑO ES LA UVA 1 o 2:\n "))
print("SI SE INGRESE LOS DATOS EN DECIMALES UTILIZAR EL PUENTO (.) ")
kilos_de_produccion=float(input("INGRESE CUANTOS KILOS DE PRODUCCION SON:\n "))
el_precio=float(input("INGRESE EL PRECIO POR KILO:\n "))
#datos para los ingrementos o revajas del precio.....
p_tip_tam_A_1=0.20
p_tip_tam_A_2=0.30
p_tip_tam_B_1=0.30
p_tip_tam_B_2=0.50

if tipo=='A':
    if tamaño==1:
        subprecio=el_precio*kilos_de_produccion
        precio_final=subprecio+p_tip_tam_A_1
        print(f" \n TIPO: {tipo} \n TAMAÑO: {tamaño} \n CANTIDAD DE KILOS: {kilos_de_produccion}")
        print(f" PRECIO POR kilo: {el_precio} $\n SUBTOTAL: {subprecio} $\n PRECIO POR EL TIPO Y TAMAÑO: {p_tip_tam_A_1} $")
        print(f" TOTAL: {precio_final} $\n GANCIA PARA LA ASOSIACION DE VINICULTORES: {precio_final} $ \n")
    elif tamaño==2:
        subprecio=el_precio*kilos_de_produccion
        precio_final=subprecio+p_tip_tam_A_2
        print(f" \n TIPO: {tipo} \n TAMAÑO: {tamaño} \n CANTIDAD DE KILOS: {kilos_de_produccion}")
        print(f" PRECIO POR KILO: {el_precio} $\n SUBTOTAL: {subprecio} $\n PRECIO POR EL TIPO Y TAMAÑO: {p_tip_tam_A_2} $")
        print(f" TOTAL: {precio_final} $\n GANCIA PARA LA ASOSIACION DE VINICULTORES: {precio_final} $ \n")
elif tipo=='B':
    if tamaño==1:
        subprecio=el_precio*kilos_de_produccion
        precio_final=subprecio-p_tip_tam_B_1
        print(f" \n TIPO: {tipo} \n TAMAÑO: {tamaño} \n CANTIDAD DE KILOS: {kilos_de_produccion}")
        print(f" PRECIO POR KILO: {el_precio} $\n SUBTOTAL: {subprecio} $\n PRECIO DE REBAJA POR EL TIPO Y TAMAÑO: {p_tip_tam_B_1} $")
        print(f" TOTAL: {precio_final} $\n GANCIA PARA LA ASOSIACION DE VINICULTORES: {precio_final} $ \n")
    elif tamaño==2:
        subprecio=el_precio*kilos_de_produccion
        precio_final=subprecio-p_tip_tam_B_2
        print(f" \n TIPO: {tipo} \n TAMAÑO: {tamaño} \n CANTIDAD DE KILOS: {kilos_de_produccion}")
        print(f" PRECIO POR KILO: {el_precio} $\n SUBTOTAL: {subprecio} $\n PRECIO DE REBAJA POR EL TIPO Y TAMAÑO: {p_tip_tam_B_2} $")
        print(f" TOTAL: {precio_final} $\n GANCIA PARA LA ASOSIACION DE VINICULTORES: {precio_final} $ \n")