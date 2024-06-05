#DETECTOR DE GAS...... >-<
#Presentacion del programa
print("++++++++++BIENVENIDO QUERIDO USUARIO++++++++++")
#Variable global..... 
contador_de_talleres=0
talleres=1
#solucion del problema....
while talleres<=3:
    print(f"El taller {talleres} se detecta fuga de gas?")
    estado_del_taller=input("Ingrese (si o no):")
    if estado_del_taller=="si":
        contador_de_talleres+=1
    talleres+=1
if contador_de_talleres>1:
    print("Mandar mensajes al correo del gerente...")
else :
    print ("Gracias por su colaboración....>-<...")

