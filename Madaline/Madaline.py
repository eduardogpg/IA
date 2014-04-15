# -*- encoding: utf-8 -*-

from random import randint

from clases import Values
from clases import Adaline
from clases import outPutNeuron

class Madaline():
	def __init__(self, listZ, listK, numberAdaline):

		self.listZ = listZ
		self.listK =  listK
		self.listAdalines = []
		self.finalNeuron = outPutNeuron()
		self.alfa = 0.1 
		#self.alfa = 0.00001

		self.LastWeigths =  []
		self.MakeAdalines(numberAdaline)

		self.cont = 0
		self.flag = False
	

		self.listResults = []

	def MakeAdalines(self,numberAdaline):
		for n in range(0, numberAdaline):

			myAdaline = Adaline(n, len(self.listK[0]), self.alfa, self.finalNeuron)
			self.listAdalines.append(myAdaline)

	def Algorithm(self):
		self.cont = 0

		for k in range(0, len(self.listK)):
			
			for myAdaline in self.listAdalines:
				myAdaline.setWeightedSum( self.listK[k]  )

			self.CheckAlgorithm(k)
			self.restart()

		if self.cont == len(self.listK):
			self.flag = True
		else:
			self.listResults = []


	def CheckAlgorithm(self,k):
		
		if self.finalNeuron.majorityFunction() == int(self.listZ[k]):
			self.cont = self.cont + 1
			self.listResults.append( self.finalNeuron.majorityFunction() )
		else:
			self.CorrectionError(k, self.listK[k])

	
	def CorrectionError(self, k, inputs):
		badList = []
		#less = 1000000000000
		pos = 0
		Ada = None
		for myAdaline in self.listAdalines:
			value = myAdaline.out

			if value != int(self.listZ[k]):
				badList.append(myAdaline)
		
		if len(badList) == 1:
			pos=0

		else:
			less = badList[0]
			for n in range(0, len(badList)):
				value = badList[n].weighted_sum

				if value < 0:
					value = value * (-1)

				if value < less:
					less = value
					pos = n

		badList[pos].CorrectionErrorAdaline(float(self.listZ[k]), inputs)

	def AddLastWeigths(self):
		for myMadaline in self.listAdalines:
			self.LastWeigths.append( myMadaline.listWeigths )

	def showLastWeigths(self):
		for list in self.LastWeigths:
			print list

	def restart(self):
		for myAdaline in self.listAdalines:
			myAdaline.restart()
			myMadaline.out = 0

		self.finalNeuron.listOutPut = []
		self.finalNeuron.out = 0

	def getLastW(self):
		return self.LastWeigths


		

#File = Values('IRIS.txt')
File = Values('XOR.txt')


numberAdaline = input("Numero de Adalines : ")
myMadaline = Madaline(File.getListZ(), File.getListK(), numberAdaline)

while myMadaline.flag== False:
	myMadaline.Algorithm()


myMadaline.AddLastWeigths()

print "\nLos pesos Finales son  :"
myMadaline.showLastWeigths()

File.saveNewValues( myMadaline.getLastW() )
