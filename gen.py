from datetime import datetime

universo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
pares = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]
nopar = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33]
primo = [2,3,5,7,9,11,13,17,19,23,29,31]
d = [1,1,1,1,1,1]

def BuscarPrimo():
	# uno y dos inuniversoan si hay un minimo de uno o dos primos en la serie de numeros
	uno = False
	dos = False
	for x in d:
		for y in primo:
			if x==y:
				if not uno:
					uno = True
				else:
					if not dos:
						dos = True
				if uno and dos:
					return True
	return False

def BuscarPares():
	uno = False
	dos = False
	tres = False
	for x in d:
		for y in pares:
			if x==y:
				if not uno:
					uno = True
				else:
					if not dos:
						dos = True
					else:
						if not tres:
							tres=True
				if uno and dos and tres:
					return True
	return False

def BuscarNones():
	uno = False
	dos = False
	tres = False
	for x in d:
		for y in nopar:
			if x==y:
				if not uno:
					uno = True
				else:
					if not dos:
						dos = True
					else:
						if not tres:
							tres=True
				if uno and dos and tres:
					return True
	return False

def VerificarSuma():
	suma=0
	for x in d:
		suma = suma + x
	if suma > 93 and suma < 106:
		return True
	else:
		return False

def BuscarRepetidos():
	for x in d:
		i=0
		for y in d:
			if x==y:
				i=i+1
			if i > 1:
				return False
	return True

def GenerarNumeros():
	inicio = datetime.now()
	posicion = 5
	imprimir = True
	variador = 1
	i = 1 #contraseñas generadas en total

	while posicion >= 0:
		if imprimir:
			for x in range(33):
				d[posicion] = universo[x]
				if BuscarRepetidos() and BuscarNones() and BuscarPares() and BuscarPrimo() and VerificarSuma():
					print(f"{d[0]}\t{d[1]}\t{d[2]}\t{d[3]}\t{d[4]}\t{d[5]}") 	# envia la d generada a un archivo de texto
					i += 1
		posicion -= variador 					# baja un espacio para su analisis 
		if posicion == -1:
			break
		if d[posicion] != universo[32]:	# compara el caracter en el espacio de posicion con el ultimo caracter del alfabeto
			d[posicion] = universo[int(universo.index(d[posicion]))+1] #disminuye una posicion en la d y avanza un caracter en el alfabeto
			for x in range(6): # rellena con la primer letra del alfabeto todos los campos a la izquierda, cada que el script da un salto de posicion.
				if 6-x-1>posicion:
					d[6-x-1] = universo[0]	
			posicion += variador 				# retorna posicion a su estado anterior, para generar las ds con el nuevo caracter en posicion-1
			variador = 1						# retorna variador a 1 para hacer el barrido de hisquierda a derecha con las nuevas modificaciones.
			imprimir = True
		else:
			posicion += variador 			# como la posicion actual llego al final del alfabeto, avanza un espacio para verificar la siguiente posicion
			variador += 1					# var -> variador, suma 1 para desplazar la posicion hacia la izquierda
			imprimir = False
	fin = datetime.now()
	print(f"Inicio de ejecucion {inicio}")
	print(f"Fin de ejecucion {fin}")
	print(f"Numero de contraseñas {i}")


GenerarNumeros()