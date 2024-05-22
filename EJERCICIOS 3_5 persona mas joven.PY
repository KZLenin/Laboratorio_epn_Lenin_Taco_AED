#EJERCICIO 3,5 
#DETERMINAR LA PERSONA MENOR DE EDAD....
print("\n-------------------------------------------")
print("--------BIENVENIDO QUERIDO USUARIO--------\n ")
print("PROGRAMA PARA DETERMINAR LA PERSONA MENOR DE EDAD....")
print("...POR FAVOR LA PRIMERA PERSONA INGRESE SUS DATOS...")
nombre_1=str(input(" INGRESE SU NOMBRE:\n "))
edad_1=int(input(" INGRESE SU EDAD:\n "))
print("...POR FAVOR LA SEGUNDA  PERSONA INGRESE SUS DATOS...")
nombre_2=str(input(" INGRESE SU NOMBRE:\n "))
edad_2=int(input(" INGRESE SU EDAD:\n "))
print("...POR FAVOR LA TERCERA Y ULTIMA PERSONA INGRESE SUS DATOS...")
nombre_3=str(input(" INGRESE SU NOMBRE:\n "))
edad_3=int(input(" INGRESE SU EDAD:\n "))

if edad_1<18:
    print(f"LA PERSONA: {nombre_1} \n CON EDAD DE: {edad_1} AÑOS\n ES MENOR DE EDAD...")
elif edad_2<18:
    print(f"LA PERSONA: {nombre_2} \n CON EDAD DE: {edad_2} AÑOS\n ES MENOR DE EDAD...")
elif edad_3<18:
    print(f"LA PERSONA: {nombre_3} \n CON EDAD DE: {edad_3} AÑOS\n ES MENOR DE EDAD...")