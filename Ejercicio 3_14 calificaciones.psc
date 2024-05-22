
	Algoritmo determinar_calificacion
		Escribir '-------------------------------------------'
		Escribir '--------BIENVENIDO QUERIDO USUARIO--------'
		Escribir ' '
		Escribir 'PROGRAMA PARA DETERMINAR LA CALIFICACION DESDE A HASTA F....'
		Escribir ''
		Escribir 'Ingrese su calificación desde 0 a 10: '
		Leer nota
		Si nota==10 Entonces
			Escribir 'Ud tiene una A.'
		SiNo
			Si nota==9 Entonces
				Escribir 'Ud tiene una B.'
			SiNo
				Si nota==8 Entonces
					Escribir 'Ud tiene una C.'
				SiNo
					Si nota==7 O nota==6 Entonces
						Escribir 'Ud tiene una D.'
					SiNo
						Escribir 'Ud tiene una F.'
					FinSi
				FinSi
			FinSi
		FinSi
FinAlgoritmo

