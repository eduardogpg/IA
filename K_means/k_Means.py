from random import randint
import math

#Cambiar valores a 1
#Checar por que siempre da los mismos resultados 

class Values():
	def __init__(self, File):

		self.listaIndividuos = []

		self.setValues( self.OpenFile(File) )

	def OpenFile(self, path):
		try:
			File = open(path)	
			return File
		except:
			return None

	def SetnumeroCarcateristicas(self, sentence, word):
		count = 0
		for w in sentence:
			if w == word:
				count +=1
		return count 

	def setValues(self, File):
		
		for line in File.readlines():
			sentence = line.strip('\n')
			self.listaIndividuos.append( self.setValuesList(sentence) )

	

	def setValuesList(self, sentence):
		numeroCarcateristicas = self.SetnumeroCarcateristicas(sentence, ',')
		line = sentence.split(',', numeroCarcateristicas)
		supportList = []

		for valor in line:
			supportList.append(float (valor))

		return supportList

	def getList(self):
		return self.listaIndividuos

class centroide():
	def __init__(self, coordenadas):
		self.coordenadas = coordenadas
		self.viejasCoordenadas = []

	def obtenerCoordenadas(self):
		return self.coordenadas

	def promedio(self,lista):
	
		for posC in range(0, len(self.coordenadas)):
			suma = 0.0
			for pos in range(0,len(lista)):
				suma = suma + lista[pos][posC]
			
			self.coordenadas[posC] = suma / len(lista)

		if self.coordenadas == self.viejasCoordenadas:
			return True
		else:
			self.viejasCoordenadas = self.coordenadas
			return False

	
class k_means():
	def __init__(self, listaIndividuos, numeroClases):
		self.listaIndividuos = listaIndividuos
		self.listaCentroides = self.establecerCentroides(numeroClases)
		self.MatrizResultados = []

	def establecerCentroides(self, numeroClases):
		listaAux = []
		for pos in range(0, numeroClases):
			nuevoCentroide = centroide(self.listaIndividuos[randint(0, len(self.listaIndividuos)-1)])
			listaAux.append(nuevoCentroide)
		return listaAux

	def algoritmo(self):
		bandera = False
		while bandera == False:
			
			MatrizResultados = []
			for pos in range(0, len(self.listaCentroides) ):
				MatrizResultados.append([])

			
			MatrizDitancias = []
			for posCentroide in range(0, len(self.listaCentroides)):
				centroideActual = self.listaCentroides[posCentroide]

				listaDistanciaCentroides = []

				for posIndividuos in range(0, len(self.listaIndividuos)):
					individuo = self.listaIndividuos[posIndividuos]
					listaDistanciaCentroides.append ( self.calcularDistancia( centroideActual.obtenerCoordenadas(), individuo ) )
				
				MatrizDitancias.append(listaDistanciaCentroides)

			for posIndividuos in range(0, len(self.listaIndividuos)):
				listaValores = []
				for posMa in range(0, len(MatrizDitancias)):
					listaValores.append(MatrizDitancias[posMa][posIndividuos])

				pos = self.obtenerPosicionMenor(listaValores)
				listaAux = MatrizResultados[pos]
				listaAux.append(self.listaIndividuos[posIndividuos])
				MatrizResultados[pos] = listaAux


			p = True
			for posCentroide in range(0, len(self.listaCentroides)):
				centroide = self.listaCentroides[posCentroide]
				if centroide.promedio(MatrizResultados[posCentroide]) != True:
					p=False

			if p == True:
				self.MatrizResultados = MatrizResultados
				bandera = True
	
	def calcularDistancia(self, listaUno, listaDos):
		distancia = 0
		for pos in range(0, len(listaUno)):
			distancia = distancia + ((listaDos[pos] - listaUno[pos])** 2)
		
		return math.sqrt( distancia )


	def obtenerPosicionMenor(self, lista):
		posMenor = 0
		menor = lista[posMenor]
		for pos in range(0, len(lista)):
			valor = lista[pos]
			if valor < menor:
				menor = valor
				posMenor = pos

		return posMenor

	def mostrarResultados(self):

		for lista in self.MatrizResultados:
			print len(lista)

	def posMayor(self, lista):
		posMayor = 0
		mayor = lista[posMayor]

		for pos in range(0, len(lista)):
			valor = lista[pos]
			if valor > mayor:
				posMayor = pos
				mayor = valor

		return posMayor


	def probarEjemplo(self):
		listaValores = []
		for pos in range(0, len(self.listaIndividuos[0])):
			listaValores.append( float(input("Valores : ")))

		listaDistancia = []
		for posCentroide in range(0, len(self.listaCentroides)):
			centroideActual = self.listaCentroides[posCentroide] 
			listaDistancia.append ( self.calcularDistancia( centroideActual.obtenerCoordenadas(), listaValores ) )  
		
		print "Pertenece a la clase :  " + str( self.posMayor(listaDistancia))		


valores = Values('Iris.txt')
closter = k_means(valores.getList(), input("Numero de Clases : "))
closter.algoritmo()
closter.mostrarResultados()
#closter.probarEjemplo()
