# -*- encoding: utf-8 -*-
from random import randint

class Adaline():
	def __init__(self,NumberAdaline, numberInpust, alfa, finalNeuron):
		self.numberAdaline = NumberAdaline
		self.listWeigths = []
		self.weighted_sum = 0
		self.alfa = alfa
		self.setListlistWeigths(numberInpust)
		
		self.finalNeuron = finalNeuron
		self.out = 0

	def setListlistWeigths(self, numberInpust):
		for n in range(0, numberInpust):
			weigth = (randint(1,9) * .1)
			self.listWeigths.append(weigth)

	def setWeightedSum(self, listInput):

		
		for x in range(0, len(listInput)):
			self.weighted_sum = self.weighted_sum + ( float(listInput[x]) * self.listWeigths[x])
		
		self.weighted_sum = self.weighted_sum - self.alfa
		
		self.finalWeightedSum()

	def finalWeightedSum(self):
		
		self.out = self.activationFuncion(self.weighted_sum)
		#print "Salida " + str(self.out ) + "De la neurona "+ str(self.numberAdaline)
		self.finalNeuron.addListOutPut(self.out)

	def activationFuncion(self, a):
		if a >=0:
			return 1
		else:
			return -1

	def CorrectionErrorAdaline(self, z, input):

		for n in range(0, len(self.listWeigths)):
			self.listWeigths[n] = float(self.listWeigths[n] + ( self.alfa * ( (float(z) - self.weighted_sum) * float(input[n]) ) ) )


	def restart(self):
		self.weighted_sum = 0
		self.out = 0
