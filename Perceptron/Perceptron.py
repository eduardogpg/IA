#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from random import randint

class Perceptron():
	def __init__(self, path):
		self.listWeigth = []
		self.resultList =  []
		self.kList = []

		self.alfa = 0 
		self.flag= False
		
		self.listY = []
		self.File = self.openFile(path)


	def setValues(self):
		self.getEnters()
		
		for x in range(0, len(self.kList[0])):
			self.listWeigth.append(  (randint(1,10) * .1)  )
		
		self.alfa = (randint(0,10)*.1)
		
	def getEnters(self):
		for line in self.File.readlines():
			word = line.strip('\n')
			self.setValuesLists(word)
		
	def getResult(self):
		return self.flag

	def getListZ(self):
		return self.resultList

	def getListY(self):
		return self.listY

	def Algorithm(self):
		contador = 0
		listR = []

		for k in range(0, len(self.kList)): 
			weighted_sum = 0
			
			for y in range(0, len(self.kList[k])): 
				weighted_sum = (float(self.kList[k][y]) * self.listWeigth[y])+ weighted_sum 
																	
			output = self.activationFunction(weighted_sum-self.alfa)
			
			if output == float(self.resultList[k]):
				contador = contador + 1
				listR.append(output)

			else:
				self.New_W(float(self.resultList[k]),output,self.kList[k])	
			
		if contador== len(self.resultList):
			self.listY = listR
			self.flag= True

	
	def New_W(self,z,y,listK):
		
		for x in range(0,len(listK)):
			self.listWeigth[x] = ( ( (self.alfa * (z-y) ) * ( float(listK[x]) ) ) + self.listWeigth[x] ) 
			
		#print "Nuevos Pesos " + str(self.listWeigth)

	def activationFunction(self,a):
		if a>=0:
			return float(1)
		else:
			return  float(-1)

	def setValuesLists(self, sentence):
		line = sentence.split(',', 5)
		otraList = []
		for x in range(0, len(line)):
			if x == (len(line)-1 ):
				self.resultList.append(line[x])
			else:
				otraList.append((line[x]))

		otraList.append(-1)#x5

		self.kList.append(otraList)

	def openFile(self, path):
		try:
			File = open(path)	
			return File
		except:
			return None

#################################################

def saveNewValues(listWeigth):
	f =  open("pesos.txt", "w")
	
	for x in range(0, len(listWeigth)):
		demo = str(listWeigth[x])
		f.write(demo+"\n")
	print str(listWeigth)

Neurona = Perceptron('IRIS.txt')
Neurona.setValues()

print "\nThe first values of the weights are : \n" + str(Neurona.listWeigth) + " \n\n"

count = 0

while Neurona.getResult()==False:
	Neurona.Algorithm()
	count +=1

	if count>= 100000:
		Neurona.flag=True

if count< 100000:
	
	for x in range(0,len(Neurona.listWeigth)):
		print "Weigth "+str(x+1)+ " : " + str(Neurona.listWeigth[x] )  + " " 

	saveNewValues(Neurona.listWeigth)

else:
	print "Tu Funcion es NO linealmente separable"