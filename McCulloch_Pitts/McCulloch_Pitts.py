class McCullochPitts():
	def __init__(self, path):
		self.resultList =  []
		self.kList = []
		self.listWeigth = []
		self.flag= True
		
		self.Alfa = 0
		self.File = self.openFile(path)
	
	def setValues(self, listWeigth, Alfa):
		self.listWeigth = listWeigth
		self.Alfa = Alfa

	def getEnters(self):
		for line in self.File.readlines():
			sentence = line.strip('\n')
			self.setListsValues(sentence)
			
		return len(self.kList[0])

	def getResult(self):
		return self.flag

	def Algorithm(self):
		for x in range(0, len(self.kList)): 
			weighted_sum = 0
			
			for y in range(0, len(self.kList[x])):
				weighted_sum = (float(self.kList[x][y]) * float(self.listWeigth[y]) ) + weighted_sum 

			output = self.activationFunction(weighted_sum-self.Alfa)
			
			if output != int(self.resultList[x]):
				self.flag=False
	
	def activationFunction(self,a):
		if a>=0:
			return 1
		else:
			return 0

	def setListsValues(self, sentence):
		line = sentence.split(',', 5)
		otherList = []
		for x in range(0, len(line)):
			if x == (len(line)-1 ):
				self.resultList.append(line[x])
			else:
				otherList.append((line[x]))
		self.kList.append(otherList)

	def showListZ(self):
		for z in self.resultList:
			print z

	def showListK(self):
		for k in self.kList:
			print k

	def openFile(self, path):
		try:
			File = open(path)	
			return File
		except:
			return None

listWeigth = []
Neurona = McCullochPitts('file.txt')

n = Neurona.getEnters()
Neurona.showListK()

for x in range(0, n):
	weigth =  int (raw_input("Enter a new Number for the weigth  : "))
	weigth = weigth
	listWeigth.append(weigth)

Alfa =  int (raw_input("Enter a new Number for the Alfa : "))

Neurona.setValues(listWeigth, Alfa)
Neurona.Algorithm()

if Neurona.getResult():
	print "\n\nthe weigth's and the Alfa are correct \n\n"
else:
	print "\n\nProblem with the weigth and Alfa\n\n"
