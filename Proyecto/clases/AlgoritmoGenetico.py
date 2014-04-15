from random import randint
import math

class AlgoritmoGenetico():
	def __init__(self, listaCiudades, puntoDeSalida):

		self.despegue = False

		self.MejorResultado = 10000000000000000
		self.rutaFinal = []
		self.listaCiudades = listaCiudades
		self.puntoDeSalida = puntoDeSalida
		self.matrizPoblacion =  self.crearPoblacion(listaCiudades, 100)


	def crearPoblacion(self, listaCiudades, generaciones):
		matrizPoblacion = []
		for pos in range(0, generaciones):
			listaAux = self.obtenerListaPermutacion(len(listaCiudades))
			matrizPoblacion.append(listaAux)

		return matrizPoblacion

	def obtenerListaPermutacion(self, numeroMaximo):
		listaPermutacion =[]
		for pos in range(0,numeroMaximo):
			numeroRandom = randint(0, numeroMaximo-1)
			if numeroRandom in listaPermutacion:
				bandera=False
				while bandera==False:
					numeroRandom = randint(0, numeroMaximo-1)
					if numeroRandom in listaPermutacion:
						bandera= False
					else:
						listaPermutacion.append(numeroRandom)
						bandera=True

			else:
				listaPermutacion.append(numeroRandom)

		return listaPermutacion

	def calcularDistanciaDosPuntos(self, puntoUno, puntoDos):
		a = puntoUno.obtenerPosX() - puntoDos.obtenerPosX()
		b = puntoUno.obtenerPosY() - puntoDos.obtenerPosY()

		if a <0:
			a= a*-1
		if b<0:
			b= b*-1

		return math.sqrt( (a**2) + (b**2) ) 

	def obtenerDistancia(self, matriz):
		listaValores = []
		for listaRutas in matriz:
			distancia = 0
			for posRuta in range(0, len(listaRutas)):

				ciudad = self.listaCiudades[ listaRutas[posRuta] ]

				if posRuta < len(listaRutas)-1:
					siguienteCiudad = self.listaCiudades [ listaRutas[posRuta+1] ]
	
				else:
					siguienteCiudad = self.puntoDeSalida
				
				distanciaAB = self.calcularDistanciaDosPuntos(siguienteCiudad, ciudad)
				distancia = distancia + distanciaAB

			listaValores.append(distancia)

		return listaValores

	def torneo(self, lista, matriz):
		matrizGanadores = []
		for pos in range(0, len(lista)):
			posUno = randint(0,len(matriz)-1)
			posDos = randint(0,len(matriz)-1)
			valorUno = lista[posUno]
			valorDos = lista[posDos]

			if valorUno <= valorDos:
				matrizGanadores.append( matriz[posUno] )
			else:
				matrizGanadores.append( matriz[posDos] )
				
		return matrizGanadores

	def Cruza(self, matriz):
		nuevaMatriz = []
		bandera= False
		pos = 0
		while bandera== False:

			if pos < len(matriz):
				listaUno = matriz[pos]
				pos = pos+1
				listaDos = matriz[pos]
				pos=pos+1
				#print listaUno
				#print listaDos
				#print self.cruzaListas(listaUno, listaDos)
				#print self.cruzaListas(listaDos, listaUno)
				#print "\n\n"
				nuevaMatriz.append( self.cruzaListas(listaUno, listaDos) )
				nuevaMatriz.append( self.cruzaListas(listaUno, listaDos) )
			else:
				bandera= True

		return nuevaMatriz
	
	def cruzaListas(self, listaUno, listaDos):
		puntoCruza = randint(1, len(listaUno)-1 ) 

		listaAux = []
		for posValor in range (0, len(listaUno)):
			if posValor < puntoCruza:
				listaAux.append(listaUno[posValor])
		listaAuxDos = []

		for posValor in range(puntoCruza, len(listaUno)):
			listaAuxDos.append (listaUno[posValor])

		for valor in listaDos:
			for valorDos in listaAuxDos:
				if valor == valorDos:
					listaAux.append(valor)

		return listaAux

	def mutacion(self, matriz):
		matrizMutacion = []
		for lista in matriz:
			if 10 < randint(0,100):
				#print lista
				#nuevaLista = self.cambiarValoresLista( lista )
				#print nuevaLista
				matrizMutacion.append( self.cambiarValoresLista( lista ) )

				#print "\n\n"
			else:
				matrizMutacion.append(lista)

		return matrizMutacion

	def cambiarValoresLista(self,lista):
		puntoMutacion = randint(0, len(lista)-1)
		listaAux=[]

		for pos in range(0, len(lista)):
			if pos < puntoMutacion:
				listaAux.append(lista[pos])

		n = lista[puntoMutacion:]
		p = n[0]
		A = n[len(n)-1]
		n[0] = A
		n[len(n)-1] =p
		for valor in n:
			listaAux.append(valor)

		return listaAux

	def MejorRuta(self, listaValores, matriz):
		listaAux =listaValores
		listaAux.sort()

		if listaAux[0] < self.MejorResultado:

			A = self.menor_lista(listaValores)

			self.MejorResultado = A[0]
			self.rutaFinal = matriz[A[1]]
			

	def menor_lista(self,lista): 
		posMenor=0
		menor = lista[posMenor]
		listaA =[]
		for pos in range(0, len(lista)): 
		    valor = lista[pos]
		    if valor < menor: 
		        menor = valor
		        posMenor= pos
		listaA.append(menor)
		listaA.append(posMenor)
		return listaA

	def Algoritmo(self, numeroGeneraciones):
		print "Comenza Algoritmo "

		for posGeneraciones in range(0, numeroGeneraciones):
			#Primer paso completado
			matriz = self.matrizPoblacion

			#Problematica Aplicada
			listaValoresDistancia = self.obtenerDistancia(matriz)

			matrizGanadores = self.torneo(listaValoresDistancia, matriz)

			self.MejorRuta(listaValoresDistancia, matriz)

			MatrizCruza = self.Cruza(matrizGanadores)

			self.matrizPoblacion = self.mutacion(MatrizCruza)

		print "\n\nAlgoritmo Terminado Mejor Resultado : "
		print self.rutaFinal

		self.despegue = True