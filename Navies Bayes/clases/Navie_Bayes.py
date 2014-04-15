
class Navie_Bayes():
	def __init__(self, Matriz, ListaClases ):
		self.Matriz = Matriz
		
		self.ListaClases = ListaClases
		self.ListadoClases = self.obtenerlListaLlaves(ListaClases)
		self.valoresListadosClases = self.obtenerListaValores( self.ListadoClases, ListaClases )
		self.valoresRealesClases = self.obtenerValoresReales( self.valoresListadosClases )

		self.listadoLlavesCaratetisticas = []

		self.listaMatricesCaracteristicas = []
		self.listaMatricesCaracteristicasReales = []
		
		self.crearMatrices(Matriz)

	def algoritmo(self):
		listaValores = []
		bandera= False
		for pos in range(0, len(self.listadoLlavesCaratetisticas)):
			valor = raw_input("Introdusca el valor del atributo "+str(pos+1) +" : ")
			listaValores.append(valor)

		for posValor in range(0, len(listaValores)):
			valor = listaValores[posValor]
			lista = self.listadoLlavesCaratetisticas[posValor]
			
			if valor in lista:
				for posLista in range(0, len(lista)):
					nuevoValor = lista[posLista]
					bandera = True
					if nuevoValor == valor:
						listaValores[posValor] = posLista
			else:
				print "Los Datos no Coinciden"
				print self.listadoLlavesCaratetisticas
				break
		#print listaValores
		if bandera== True:
			MatrizAux = []
			for posMatriz in range(0, len(self.listaMatricesCaracteristicasReales)):
				matriz = self.listaMatricesCaracteristicasReales[posMatriz]
				#print matriz
				listaSN = []
				for posClase in range(0, len(self.ListadoClases)): #Si o No
					lista = matriz[posClase]
					posicion = listaValores[posMatriz]
					listaSN.append( lista[posicion])

				#print listaSN
				MatrizAux.append(listaSN)
			
			MatrizAux = self.cambioPosicionMatriz(MatrizAux)
			print "\n\n"
			#print MatrizAux 
			
			listaResultados =[]
			for posLista in range(0, len(MatrizAux)):
				lista = []
				listaA = MatrizAux[posLista]
				for valor in listaA:
					lista.append(valor)

				primero = self.valoresRealesClases[posLista]
				lista.append(primero)
				listaResultados.append (self.multiplicacion(lista))

			print self.ListadoClases
			print listaResultados

			valorMaximo = -10000
			posFinal = 0
			for posvalor in range(0, len(listaResultados)):
				valor = listaResultados[posvalor]
				
				if valor > valorMaximo:	
					valorMaximo = valor
					posFinal = posvalor
				
			print "\nProbabilidad : "+str(valorMaximo) + " Clase " +str(self.ListadoClases[posFinal])
			
	def cambioPosicionMatriz(self, matriz):
		Matriz =[]
		for posX in range(0, len(matriz[0])):
			listaAux = []

			for posY in range(0, len(matriz)):
				valor = matriz[posY][posX]
				listaAux.append(valor)
			Matriz.append(listaAux)

		return Matriz

	def crearMatrices(self, Matriz):
		numeroAtributos = len(Matriz[0])-1

		listaEstadosLista = []
		for columna in range(0, numeroAtributos):
			listaEstados = []
			for fila in range(0, len(Matriz)):
				listaEstados.append(Matriz[fila][columna])

			listaEstadosLista.append(listaEstados)

		for pos in range(0, len(listaEstadosLista)):
			listaEstadosLlaves = self.obtenerlListaLlaves(listaEstadosLista[pos])
			
			self.listadoLlavesCaratetisticas.append(listaEstadosLlaves)
			self.listaMatricesCaracteristicas.append ( self.crearMatriz(listaEstadosLlaves,listaEstadosLista[pos]) )
		self.listaMatricesCaracteristicasReales = self.listaMatricesCaracteristicas
		
		for posMatriz in range(0, len(self.listaMatricesCaracteristicasReales)):
			matriz = self.listaMatricesCaracteristicasReales[posMatriz]
			matrizR= []

			for posF in range(0, len(matriz)):
				listaAux = matriz[posF]
				nuevaLista = []
				suma = 0
				for valor in listaAux:
					suma = suma + valor

				for valor in listaAux:
					nuevoValor = float(valor)/ float(suma)
					nuevoValor = int(nuevoValor * 1000) / 1000.0
					nuevaLista.append(nuevoValor)
				matrizR.append(nuevaLista)

			self.listaMatricesCaracteristicasReales[posMatriz] = matrizR

	def crearMatriz(self, listaLlaves, listaColumna):
		matriz = []
		for valorClase in self.ListadoClases:
			listaAux = []
			for valorColumna in listaLlaves:
				value = self.obtenerValor(valorColumna ,valorClase ,listaColumna)
				listaAux.append(value)
			matriz.append(listaAux)
		
		return matriz

	def obtenerValor(self,  valorColumna, valorClase, listaColumna):
		counter = 0
		for posClass in range(0, len(self.ListaClases)): #Los 14
			className = self.ListaClases[posClass]

			if className == valorClase:
				if valorColumna == listaColumna[posClass]:
					counter +=1
		return counter

	def obtenerlListaLlaves(self, listaValores):
		lista = []
		for valor in listaValores:
			if valor in lista:
				pass
			else:
				lista.append(valor)
		return  lista

	def obtenerListaValores(self, listaLlaves , lista):
		listaValores = []
		for valor in listaLlaves:
			listaValores.append(0)

		for pos in range(0, len(listaLlaves)):
			for value in lista:
				if value == listaLlaves[pos]:
					listaValores[pos] = listaValores[pos] + 1

		return listaValores

	def obtenerValoresReales(self, listaValores):
		lista = []
		suma = 0
		for valor in listaValores:
			suma = suma + float(valor)

		for valor in listaValores:
			nuevoValor = (float(valor) / suma)
			lista.append (nuevoValor)
		return lista

	def mostrarValores(self):
		print "\n________________\nValores : \n"
		print self.ListadoClases
		print self.valoresListadosClases
		print self.valoresRealesClases
		
		print "\n"
		for matriz in self.listaMatricesCaracteristicasReales:
			for fila in matriz:
				print fila
			print "\n"
	
	def multiplicacion(self, lista):
		valor = 1
		for v in lista:
			valor = valor * v
		return valor