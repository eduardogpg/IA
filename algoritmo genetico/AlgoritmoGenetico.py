from random import randint

def creacionPoblacion(numeroColumnas,numeroFilas):
	matriz = []
	for numeroC in range(0, numeroFilas):
		tupla = []
		for numeroF in range(0, numeroColumnas):
			valor  = randint(0,1) 
			tupla.append(valor)
		matriz.append(tupla)

	return matriz

class ProblemaObtimizacion():
	def __init__(self):
		pass

	def funcionObtimizar(self, valor):
		nuevoValor = valor * 2
		return nuevoValor

class AlgoritmoGenetico():
	def __init__(self, matriz, problema, max):
		self.matriz = matriz
		self.ProblemaObtimizacion = problema

		self.listadoMejoresResultados = []
		self.listadoIndividuos = []
		self.listadoGeneracionIndividuos = []
		self.maximoMejoresIndividuos = max

	def algoritmo(self, numeroGeneracions):
		for posGeneracion in range(0, numeroGeneracions):
			
			#paso numero dos
			matriz = self.matriz
			listaValores = self.__listaValoresBinarios(matriz)
			#print listaValores
			listadoValoresProblematica = self.establecerProblematica(listaValores)

			#print listadoValoresProblematica
			self.busquedaMejores(listadoValoresProblematica, matriz, posGeneracion)
			
			#paso numero tres
			matrizGanadores = self.torneo(listadoValoresProblematica, matriz)
			
			#paso numero cuatro
			matrizCruza = self.cruzaValores(matrizGanadores)

			#paso cinco
			self.matriz =  self.mutacion(matrizCruza)
		
	def mostrarValores(self):
		for posValor in range(0, len(self.listadoMejoresResultados)):
			print "Resultado  : "+ str(self.listadoMejoresResultados[posValor])
			print "Individo : "+ str(self.listadoIndividuos[posValor])
			print "Numero de Generacion "+ str(self.listadoGeneracionIndividuos[posValor])

			print "\n\n"

	def busquedaMejores(self, listadoValoresProblematica, matriz, Generacion):
	

		valores = self.obteneyMayor(listadoValoresProblematica)
		mayorGeneracion = valores[0]
		posicion = valores[1]
		
		if len(self.listadoMejoresResultados) < self.maximoMejoresIndividuos:
			self.listadoMejoresResultados.append(mayorGeneracion)
			self.listadoGeneracionIndividuos.append(Generacion)
			self.listadoIndividuos.append( matriz[posicion] )

		else:
			listaMenor = self.menor(self.listadoMejoresResultados)
			if mayorGeneracion > listaMenor[0]:
				self.listadoMejoresResultados[listaMenor[1]] = mayorGeneracion
				self.listadoGeneracionIndividuos[listaMenor[1]] = Generacion
				self.listadoIndividuos[listaMenor[1]] = matriz[posicion]

	def menor(self, lista):
		menor = self.obteneyMayor(lista)[0]
		posMenor = 0
		listaMenor=[]
		for posValor in range(0, len(lista)):
			valor = lista[posValor]
			if valor <= menor:
				menor = valor
				posMenor = posValor

		listaMenor.append(menor)
		listaMenor.append(posMenor)
		return listaMenor

	def obteneyMayor(self, lista):
		listaAux = []
		mayor = 0
		posMayor = 0
		for posValor in range(0, len(lista)):
			valor = lista[posValor]
			if valor>mayor:
				mayor = valor
				posMayor = posValor

		#print lista
		#print mayor
		listaAux.append(mayor)
		listaAux.append(posMayor)
		return listaAux

	def mutacion(self, matriz):
		matrizMutacion = []
		porMutacion = 40
		for lista in matriz:
			porcentaje = randint(0,100)
			if porcentaje <= porMutacion:
				matrizMutacion.append( self.cambiarValoresLista( lista ) )
			else:
				matrizMutacion.append(lista)

		return matrizMutacion

	def cambiarValoresLista(self,lista):
		puntoMutacion = randint(0, len(lista))
		listaAux = []
		for posValor in range(0,len(lista)):
			valor = lista[posValor]
			if posValor >= puntoMutacion:
				if valor == 1:
					nuevoValor = 0
				else:
					nuevoValor = 1
			else:
				nuevoValor = valor
			listaAux.append(nuevoValor)

		return listaAux

	def cruzaValores(self, matriz):
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
		

	def torneo(self, lista, matriz):
		matrizGanadores = []
		for pos in range(0, len(lista)):
			posUno = randint(0,len(matriz)-1)
			posDos = randint(0,len(matriz)-1)
			valorUno = lista[posUno]
			valorDos = lista[posDos]

			if valorUno>= valorDos:
				matrizGanadores.append( matriz[posUno] )
			else:
				matrizGanadores.append( matriz[posDos] )

		return matrizGanadores

	def establecerProblematica(self, lista):
		nuevaLista = []
		for valor in lista:
			nuevaLista.append( self.ProblemaObtimizacion.funcionObtimizar(valor) )
		return  nuevaLista

	def __listaValoresBinarios(self, matriz):
		listaValores = []
		for lista in matriz:
			listaValores.append( self.valorBinario(lista) )
		return listaValores

	def valorBinario(self, lista):
		listaAux = self.__cambioPosicion(lista)
		suma = 0
		posBinario= 1
		for valor in listaAux:
			if valor == 1:
				suma = suma + posBinario
			posBinario = posBinario * 2

		return suma

	def __cambioPosicion(self, listaNormal):
		
		listaCambioPosicion = []
		for pos in range(0, len(listaNormal)):
			listaCambioPosicion.append(0)

		posAux = len(listaCambioPosicion)-1
		for pos in range(0, len(listaNormal)):
			valor = listaNormal[pos]
			listaCambioPosicion[posAux] = valor
			posAux -=1

		return listaCambioPosicion


print "\n\n"
problema = ProblemaObtimizacion()
aGenetico = AlgoritmoGenetico( creacionPoblacion(15, 100) , problema, input("Numero de mejores individuos a Mostrar : "))
aGenetico.algoritmo(input("Numero de eras : "))
print "\n\n"
aGenetico.mostrarValores()
#print creacionPoblacion(5, 10)