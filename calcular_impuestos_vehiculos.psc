Algoritmo calcular_impuestos_vehiculos
	Definir vehiculos_1, vehiculos_2, vehiculos_3 Como Real
	Definir total_vehiculos, clave, i Como Entero
	Definir valor, impuesto, total_impuesto_1, total_impuesto_2, total_impuesto_3, total_general Como Real
	vehiculos_1 <- 0
	vehiculos_2 <- 0
	vehiculos_3 <- 0
	Escribir 'Ingrese la cantidad total de vehículos: '
	Leer total_vehiculos
	Para i<-1 Hasta total_vehiculos Hacer
		Escribir 'Ingrese la clave del vehículo ', i, ' : '
		Leer clave
		Mientras clave<1 O clave>3 Hacer
			Escribir 'Clave inválida. Por favor, ingrese una clave válida (1, 2 o 3): '
			Leer clave
		FinMientras
		Escribir 'Ingrese el valor del vehículo ', i, ': '
		Leer valor
		Si clave=1 Entonces
			vehiculos_1 <- vehiculos_1+valor
		FinSi
		Si clave=2 Entonces
			vehiculos_2 <- vehiculos_2+valor
		SiNo
			vehiculos_3 <- vehiculos_3+valor
		FinSi
	FinPara
	total_impuesto_1 <- vehiculos_1*0.10
	total_impuesto_2 <- vehiculos_2*0.07
	total_impuesto_3 <- vehiculos_3*0.05
	total_general <- total_impuesto_1+total_impuesto_2+total_impuesto_3
	Escribir ''
	Escribir 'Vehículos con clave 1:'
	Escribir ' - Total Valor: ', vehiculos_1
	Escribir ' - Total Impuesto: ', total_impuesto_1
	Escribir ''
	Escribir 'Vehículos con clave 2:'
	Escribir ' - Total Valor: ', vehiculos_2
	Escribir ' - Total Impuesto: ', total_impuesto_2
	Escribir ''
	Escribir 'Vehículos con clave 3:'
	Escribir ' - Total Valor: ', vehiculos_3
	Escribir ' - Total Impuesto: ', total_impuesto_3
	Escribir ''
	Escribir 'Total de impuestos para todos los vehículos: ', total_general
FinAlgoritmo
