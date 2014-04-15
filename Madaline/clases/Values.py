class Values():
	def __init__(self, File):
		self.listK = []
		self.listZ = []

		self.setValues( self.OpenFile(File) )


	def OpenFile(self, path):
		try:
			File = open(path)	
			return File
		except:
			return None

	def setValues(self, File):
		for line in File.readlines():
			sentence = line.strip('\n')
			self.setValuesList(sentence)

	def setValuesList(self, sentence):
		line = sentence.split(',', 5)
		supportList = []

		for x in range(0, len(line)):
			if x == (len(line)-1):
				self.listZ.append(line[x])
			else:
				supportList.append(line[x])

		supportList.append(-1)
		self.listK.append(supportList) 

	def getListZ(self):
		return self.listZ

	def getListK(self):
		return self.listK

	def saveNewValues(self, listWeigth):
		f =  open("pesos.txt", "w")
		
		for line in listWeigth:
			f.write(str(line)+ "\n")
