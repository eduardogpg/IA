# -*- encoding: utf-8 -*-
from random import randint

class outPutNeuron():
	def __init__(self):
		self.out = 0
		self.listOutPut = []

	def addListOutPut(self, value):
		self.listOutPut.append(value)

	def majorityFunction(self):
		#Es int
		varOne, varTwo = 0,0


		for x in self.listOutPut:
			if x == 1:
				varOne = varOne + 1
			else:
				varTwo = varTwo + 1

		if varOne > varTwo:
			self.out = 1
		else:
			self.out = -1

		print self.out
		return self.out

class Adaline():
	def __init__(self,NumberAdaline, listW, alfa, finalNeuron):
		self.numberAdaline = NumberAdaline
		self.listWeigths = []
		self.weighted_sum = 0.0
		self.alfa = alfa
		
		self.setListlistWeigths(listW)
		
		self.finalNeuron = finalNeuron
		self.out = 0

	def setListlistWeigths(self, listW):
		
		for n in range(0, len(listW)):
			value = float(listW[n])
			self.listWeigths.append(value)

	def setWeightedSum(self, listInput):

		for n in range(0, len(listInput)):
			value = float(listInput[n])
			self.weighted_sum = float(self.weighted_sum) + ( value * self.listWeigths[n])
			
		self.weighted_sum = self.weighted_sum - self.alfa
		
		self.finalWeightedSum()

	def finalWeightedSum(self):
		
		self.out = self.activationFuncion(self.weighted_sum)
		self.finalNeuron.addListOutPut(self.out)

	def activationFuncion(self, a):
		if a >=0:
			return 1
		else:
			return -1

	def restart(self):
		self.weighted_sum = 0
		self.out = 0

class Madaline():
	def __init__(self, listZ, listK, numberAdaline, ListWe):

		self.MatrixW = ListWe

		self.listZ = listZ
		self.listK =  listK
		self.listAdalines = []
		self.finalNeuron = outPutNeuron()
		self.alfa = 0.0001 #(randint(1,9) * .1)

		self.LastWeigths =  []
		self.MakeAdalines(numberAdaline)

		self.cont = 0
		self.flag = False
	
		self.listResult = []

	def MakeAdalines(self,numberAdaline):
		
		for n in range(0, numberAdaline):
			myAdaline = Adaline(n, self.MatrixW[n] , self.alfa, self.finalNeuron)
			self.listAdalines.append(myAdaline)
		
	def Algorithm(self):
		self.cont = 0

		for k in range(0, len(self.listK)):
			
			for myAdaline in self.listAdalines:
				myAdaline.setWeightedSum( self.listK[k] )

			self.listResult.append(self.finalNeuron.majorityFunction() )

			self.restart()


	def restart(self):
		for myAdaline in self.listAdalines:
			myAdaline.restart()
			myMadaline.out = 0

		self.finalNeuron.listOutPut = []

	def getListResul(self):
		return self.listResult

	def getListZ(self):
		return self.listZ

class Values():
	def __init__(self, Demo, Weigth):
		self.FileDemo = self.OpenFile ( Demo )
		self.FileWeigth = self.OpenFile( Weigth )

		self.listZ = []
		self.listK = []

		self.matrixW = []

		self.setValues( self.FileDemo )
		self.setValuesW (self.FileWeigth )

		self.numberAdaline = 0

	def setValuesW(self, File):
		cont = 0

		for s in File.readlines():
			
			lines = s.strip('\n')

			cont +=1
			sentence = lines.replace("[", "");
			sentence = sentence.replace("]", "");
			sentence = sentence.replace(" ", "");

			copy =sentence.split(',', self.numberWeigths(sentence) )
			supportList = []

			for x in range(0, len(copy)):
				supportList.append(copy[x])
			self.matrixW.append(supportList)
		
		self.numberAdaline = cont

	def numberWeigths(self, sentence):
		cont = 0
		for y in sentence:
			if str(y) == ",":
				cont +=1
		return cont

	def OpenFile(self, path):
		try:
			File = open(path)	
			return File
		except:
			return None

	def setValues(self, File):
		for line in File.readlines():
			sentence = line.strip('\n')
		
			l = sentence.split(',', 5)
			supportList= []

			for x in range(0, len(l)):
				if x == (len(l)- 1):
					self.listZ.append(l[x])
				else:
					supportList.append(l[x])

			supportList.append(-1)	
			self.listK.append(supportList)


	def getListZ(self):
		return self.listZ

	def getListK(self):
		return self.listK

	def getMatrix(self):
		return self.matrixW

	def getNumberAdalines(self):
		return self.numberAdaline

def confusionMatrix(listZ, listY):
	Matrix = [[0,0],[0,0]]
	
	for x in range(0, len(listZ)):
		if int(listZ[x]) == int(listY[x]):

			if int(listZ[x])==1:
				Matrix[0][0] = Matrix[0][0] + 1
			else:
				Matrix[1][1] = Matrix[1][1] + 1

		else:
			if int(listZ[x])==1:
				Matrix[0][1] = Matrix[0][1] + 1
			else:
				Matrix[1][0] = Matrix[1][0] + 1

	return Matrix

File = Values('Prueba.txt', 'Pesos.txt')

numberAdaline = input("Numero de Adalines : ")

myMadaline = Madaline(File.getListZ(), File.getListK(), numberAdaline, File.getMatrix() )

myMadaline.Algorithm()


Matrix = confusionMatrix(File.getListZ(), myMadaline.getListResul() )
print Matrix[0]
print Matrix[1]
