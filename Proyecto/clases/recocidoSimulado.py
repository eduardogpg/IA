from random import randint
import math

class RecocidoSimulado():

	def __init__(self, numero,  listaCiudades):

		self.listaCiudades = listaCiudades
		self.ruta = self.generarRutaAleatoria(numero)
		self.distancia = self.obtenerDistancia(self.ruta)


	def calcularDistanciaDosPuntos(self, puntoUno, puntoDos):
		a = puntoUno.obtenerPosX() - puntoDos.obtenerPosY()
		b = puntoUno.obtenerPosY() - puntoDos.obtenerPosY()

		if a <0:
			a= a*-1
		if b<0:
			b= b*-1

		return math.sqrt( (a**2) + (b**2) ) 

	def obtenerDistancia(self, lista):

		distancia = 0
		for pos in range(0, len(lista)): #Controla que no se desborde 

			posCiudad = lista[pos]
			ciudad = self.listaCiudades[posCiudad]

			if pos < len(lista)-1:
				siguienteCiudad = self.listaCiudades[ lista[pos + 1 ] ]
				distanciaPuntos = self.calcularDistanciaDosPuntos(ciudad, siguienteCiudad)
				distancia = distancia + distanciaPuntos
		
			else:
				siguienteCiudad = self.listaCiudades[ 0 ]
				distanciaPuntos = self.calcularDistanciaDosPuntos(ciudad, siguienteCiudad)
				distancia = distancia + distanciaPuntos


		return distancia

	def generarRutaAleatoria(self, numero):
		listaAux =[]
		for x in range(0, numero):
			numeroRandon = randint(0, numero-1)
			
			if numeroRandon in listaAux :
				bandera =  False
				while bandera == False:
					numeroRandon = randint(0, numero-1)
					if numeroRandon in listaAux:
						bandera = False
					else:
						listaAux.append(numeroRandon)
						bandera = True

			else:
				listaAux.append(numeroRandon)

		return listaAux

	def perturbacion(self, lista):
		numUno  = randint(0, len(lista)-1)
		numDos  = randint(0, len(lista)-1)

		a = lista[numUno]
		b = lista[numDos]
		lista[numDos] = a
		lista[numUno] = b
		
		return lista

	def algoritmo(self):

		mejorRuta = self.ruta
		mejorDistancia = self.distancia

		temperatura = 1000
		print "Ruta de Incio " +str(self.ruta)
		print self.distancia

		while temperatura >0.01:
			
			for x in range(0, 10000):
				nuevaRuta = self.perturbacion(self.ruta)
				nuevaDistancia = self.obtenerDistancia(nuevaRuta)

				if nuevaDistancia < self.distancia:
					
					self.distancia = nuevaDistancia
					self.ruta = nuevaRuta

				else:
					valor = math.exp( ( self.distancia - nuevaDistancia) / temperatura )
					numeroRandon = (randint(0,10) )
					if numeroRandon > valor:
						self.distancia = nuevaDistancia
						self.ruta = nuevaRuta

				if nuevaDistancia < mejorDistancia:
					print nuevaDistancia
					mejorDistancia = nuevaDistancia
					mejorRuta = nuevaRuta
				
			temperatura =temperatura * 0.9
			#print mejorDistancia



		print mejorRuta
		#print self.ruta
		print mejorDistancia
		self.ruta = mejorRuta