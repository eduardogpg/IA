import math

class Permutaciones():

	def __init__(self, numeroPermutacion, aereopuerto ,listaCiudades):
		self.aereopuerto = aereopuerto
		self.listaCiudades = listaCiudades

		self.listaNumeros = self.obtenerLista(numeroPermutacion)
		self.matrizCombinaciones = self.matrizPermutaciones(numeroPermutacion)
		
		for lista in self.matrizCombinaciones:
			print lista
			
		self.tratamientoMatriz()
		
		self.mejorRuta = []


		#self.distanciasPuntosAereopuerto()
		#self.Algoritmo(self.matrizCombinaciones)

	def distanciasPuntosAereopuerto(self):
		for ciudad in self.listaCiudades:
			print self.calcularDistanciaDosPuntos(self.aereopuerto, ciudad)

	def obtenerMatriz(self):
		return self.matrizCombinaciones

	def factorial(self, numero):
		resultado = 1
		
		while numero > 0:
			resultado = resultado * numero
			numero -=1
		return resultado

	def obtenerLista(self, numeroPermutaciones):
		lista = []
		for pos in range(1, numeroPermutaciones):
			lista.append(pos)
		return lista

	def cambioPos(self, posCambio):
		ValorMover = self.listaNumeros[ posCambio ]
		valorDesplazo = self.listaNumeros[ posCambio - 1]

		self.listaNumeros[posCambio] = valorDesplazo
		self.listaNumeros[posCambio -1] = ValorMover

	def matrizPermutaciones(self, numeroPermutacion):
		matriz = []
		contador = 0
		
		posCambio = len(self.listaNumeros)-1

		for posFila in range(0, self.factorial(numeroPermutacion)):
			lista =[]
			
			for valor in self.listaNumeros:
				lista.append(valor)
			matriz.append(lista)
			contador +=1
			
			if contador == numeroPermutacion:
				contador = 0
				self.cambioPos(posCambio)
				posCambio -=1
				if posCambio == 0:
					posCambio = len(self.listaNumeros)-1
		
		return self.agregarNumeroPermutacion(matriz, numeroPermutacion)

	def agregarNumeroPermutacion(self, matriz, numero):
		nuevaMatriz = []
		pos = len(matriz[0])+1
		banderaIzquierda = True	
			
		for lista in matriz:
			
			if banderaIzquierda== True:
				pos -=1
				if pos < 0:
					pos = 0
					banderaIzquierda = False
			else:
				pos +=1
				if pos == len(matriz[0]):
					pos= len(matriz[0])-1
					banderaIzquierda = True

			lista.insert(pos,numero)
			nuevaMatriz.append(lista)

		return nuevaMatriz	

	def tratamientoMatriz(self):
		for lista in self.matrizCombinaciones:
			for pos in range(0, len(lista)):
				lista[pos] = lista[pos] - 1


	def calcularDistanciaDosPuntos(self, puntoUno, puntoDos):
		a = puntoUno.obtenerPosX() - puntoDos.obtenerPosX()
		b = puntoUno.obtenerPosY() - puntoDos.obtenerPosY()

		if a <0:
			a= a*-1
		if b<0:
			b= b*-1

		return math.sqrt( (a**2) + (b**2) ) 

	def Algoritmo(self, matrizCombinaciones):

		listaDistancias = []

		for lista in matrizCombinaciones:
			
			distancia  = 0 #self.calcularDistanciaDosPuntos( self.aereopuerto, self.listaCiudades[ lista[0] ])

			for pos in range(0, len(lista)): #Controla que no se desborde 
				posCiudad = lista[pos]
				ciudad = self.listaCiudades[posCiudad]

				if pos < len(lista)-1:
					siguienteCiudad = self.listaCiudades[ lista[pos + 1 ] ]
					distanciaPuntos = self.calcularDistanciaDosPuntos(ciudad, siguienteCiudad)
					distancia = distancia + distanciaPuntos
			
				else:
					pass
					#siguienteCiudad = self.listaCiudades[ 0 ]
					#distanciaPuntos = self.calcularDistanciaDosPuntos(ciudad, siguienteCiudad)
					#distancia = distancia + distanciaPuntos

			
			listaDistancias.append(distancia)

		print len(listaDistancias)
		self.mejorRuta = self.matrizCombinaciones[ self.calcularMenorLista(listaDistancias) ]
		print self.mejorRuta

	def calcularMenorLista(self, lista):
		posMenor = 0
		menor = lista[posMenor]

		for pos in range(0, len(lista)):
			valor = lista[pos]
			if valor < menor:
				menor = valor
				posMenor = pos

		return posMenor
