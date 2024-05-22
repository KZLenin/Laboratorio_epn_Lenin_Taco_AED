Algoritmo PersonaMasJoven
    Definir nombre1, nombre2, nombre3 como Cadena
    Definir edad1, edad2, edad3 como Entero
    
    Escribir "Ingrese el nombre y la edad de la primera persona:"
    Leer nombre1
    Leer edad1
    
    Escribir "Ingrese el nombre y la edad de la segunda persona:"
    Leer nombre2
    Leer edad2
    
    Escribir "Ingrese el nombre y la edad de la tercera persona:"
    Leer nombre3
    Leer edad3
    
    Si edad1 < edad2 y edad1 < edad3 Entonces
        Escribir "La persona más joven es:", nombre1, "con edad de:", edad1
    Sino
        Si edad2 < edad1 y edad2 < edad3 Entonces
            Escribir "La persona más joven es:", nombre2, "con edad de:", edad2
        Sino
            Escribir "La persona más joven es:", nombre3, "con edad de:", edad3
        FinSi
    FinSi
FinAlgoritmo
