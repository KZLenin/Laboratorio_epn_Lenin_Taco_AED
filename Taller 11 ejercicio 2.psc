Algoritmo MatrizDiagonal
	Dimensionar matriz(100,100)
	Definir fila, columna, i, j Como Entero
	Definir esDiagonal Como Lógico
	esDiagonal <- Verdadero
	Escribir 'Ingrese el tamaño de la matriz (n x n):'
	Leer fila
	columna <- fila
	Escribir 'Ingrese los elementos de la matriz:'
	Para i<-1 Hasta fila Con Paso 1 Hacer
		Para j<-1 Hasta columna Con Paso 1 Hacer
			Leer matriz[i,j]
		FinPara
	FinPara
	Para i<-1 Hasta fila Con Paso 1 Hacer
		Para j<-1 Hasta columna Con Paso 1 Hacer
			Si (i<>j) Y (matriz[i,j]<>0) Entonces
				esDiagonal <- Falso
			FinSi
		FinPara
	FinPara
	Si esDiagonal Entonces
		Escribir 'La matriz es diagonal.'
	SiNo
		Escribir 'La matriz no es diagonal.'
	FinSi
FinAlgoritmo
