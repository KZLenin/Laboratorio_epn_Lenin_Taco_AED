#EJERCICIO 3.14
#PROGRAMA PARA DETERMINAR LAS CALIFICACIONES DESDE A-F
print("\n-------------------------------------------")
print("--------BIENVENIDO QUERIDO USUARIO--------\n ")
print("PROGRAMA PARA DETERMINAR LA CALIFICACION DESDE A HASTA F....")
nota=int(input("INGRESE SU CALIFICACION DESDE 0 A 10:\n "))

if nota==10:
    print(" Ud tiene una A.")
elif nota==9:
    print(" Ud tiene una B.")
elif nota==8:
    print(" Ud tiene una C.")
elif nota==7 or 6:
    print(" Ud tiene una D.")
elif nota<=5:
    print(" Ud tiene una F.")