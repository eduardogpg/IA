#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from random import randint

class PerceptronPrueba():
	def __init__(self, path, pathW):
		
		self.listWeigth = []
		self.resultList =  []
		self.kList = []

		self.threshold = 0 
		self.listY = []
		
		self.File = self.openFile(path)
		self.FileW = self.openFile(pathW)

	
	def setValues(self):
		self.threshold = (randint(0,10)*.1)
		
		for line in self.File.readlines():
			word = line.strip('\n')
			self.setValuesLists(word)

		for line in self.FileW.readlines():
			Weigth =float(line.strip('\n'))
			self.listWeigth.append(Weigth)

	def getListZ(self):
		return self.resultList

	def getListY(self):
		return self.listY

	def getlistWeigth(self):
		return self.listWeigth

	def Algorithm(self):
		
		for x in range(0, len(self.kList)): 
			weighted_sum = 0
			
			for y in range(0, len(self.kList[x])):
				weighted_sum = (float(self.kList[x][y]) * self.listWeigth[y])+ weighted_sum 

			output = self.activationFunction(weighted_sum-self.threshold)
			self.listY.append(output)
			
	def activationFunction(self,a):
		if a>=0:
			return float(1)
		else:
			return  float(-1)

	def openFile(self, path):
		try:
			File = open(path)	
			return File
		except:
			return None

	def setValuesLists(self, sentence):
		line = sentence.split(',', 5)
		otraList = []
		for x in range(0, len(line)):
			if x == (len(line)-1 ):
				self.resultList.append(line[x])
			else:
				otraList.append((line[x]))

		otraList.append(-1)#w5
		self.kList.append(otraList)

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

Demo = PerceptronPrueba("pruebas.txt", "pesos.txt")

Demo.setValues()

Demo.Algorithm()
print "\n\nLast Weigth's : "+ str(Demo.getlistWeigth())

Matrix = confusionMatrix(Demo.getListZ(), Demo.getListY())
print Matrix[0]
print Matrix[1]