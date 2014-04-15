class Document():
	def __init__(self, pathFile):
		
		self.listaCaracteristicas = []
		self.numeroCarcateristicas = 0
		self.listaClases = []
		self.matriz = []

		self.__setValue ( self.OpenFile(pathFile) )

	def __setValue(self, File):
		flag = True

		for line in File.readlines():
			sentence = line.strip('\n')
			if flag :
				self.numeroCarcateristicas = self.SetnumeroCarcateristicas(sentence, ',')
				self.makeListFeature( self.numeroCarcateristicas )
				flag= False
			self.__addListValues(sentence)

	def __addListValues(self, sentence):
		line = sentence.split(',', self.numeroCarcateristicas)
		listAux= []
		for x in range(0, len(line)):
		
			if x == len(line)-1:
				self.listaClases.append( line[x] )
			else:
				self.listaCaracteristicas[x].append(line[x])
			
			listAux.append(line[x])

		self.matriz.append(listAux)

	def SetnumeroCarcateristicas(self, sentence, word):
		count = 0
		for w in sentence:
			if w == word:
				count +=1
		return count 

	def makeListFeature(self, number):
		for x in range(0, number):
			auxList = []
			self.listaCaracteristicas.append(auxList)

	def OpenFile(self, path):
		try:
			File = open(path)	
			return File
		except:
			return None

	def getlistaCaracteristicas(self):
		return self.listaCaracteristicas

	def getListaClases(self):
		return self.listaClases

	def getMatriz(self):
		return self.matriz
