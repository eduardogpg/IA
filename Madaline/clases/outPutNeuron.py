# -*- encoding: utf-8 -*-
from random import randint

class outPutNeuron():
	def __init__(self):
		self.out = 0
		self.listOutPut = []

	def addListOutPut(self, value):
		self.listOutPut.append(value)

	def majorityFunction(self):
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

		return self.out
