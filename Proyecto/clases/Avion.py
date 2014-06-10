import pygame, sys
from pygame.locals import *
import threading
import time

class Avion(pygame.sprite.Sprite,  threading.Thread):
	def __init__(self, posX, posY, AereopuertoSalida):
		threading.Thread.__init__(self)
		pygame.sprite.Sprite.__init__(self)

		self.imagenAereopuerto = pygame.image.load('Imagenes/avion.fw.png')
		self.__rect = self.imagenAereopuerto.get_rect()

		self.__rect.top = posY
		self.__rect.left = posX

		if self.__rect.top % 2 :
			self.__rect.top =self.__rect.top +1

		if self.__rect.left % 2 :
			self.__rect.left = self.__rect.left +1
			
		self.listaRuta = []
		self.listaDistancia = []

		self.listaCiudades = []

		self.posRutaActual = 0
		self.arribo = False

		self.recorrido = True

		self.AereopuertoSalida = AereopuertoSalida

	def establecerVuelos(self, listaCiudades, listaRuta):
		self.listaCiudades = listaCiudades
		self.listaRuta = listaRuta

	def run(self):
		pass
		
	def dibujar(self, superficie):
		superficie.blit(self.imagenAereopuerto, self.__rect)

	def obtenerPosicionX(self):
		return	self.__rect.left

	def obtenerPosicionY(self):
		return self.__rect.top

	def obtenerDistanciaRuta(self, posicion):
		return self.listaDistancia(posicion)

	def siguienteCiudad(self):
		
		if self.recorrido == True:
			self.posRutaActual = self.posRutaActual +1
			self.arribo = False
		
	def ruta(self):

		if self.recorrido == True:
			if self.arribo == True:
				self.siguienteCiudad()
			else:
				
				banderaDerecha = False
				banderaArriba = False

				if self.posRutaActual < len(self.listaCiudades):
					posCiudad = self.listaRuta[self.posRutaActual]
					Ciudad = self.listaCiudades[posCiudad]

					if self.__rect.left == Ciudad.obtenerPosX():
						banderaDerecha= True

					if self.__rect.top == Ciudad.obtenerPosY():
						banderaArriba= True

					if (banderaArriba == True ) and (banderaDerecha ==True):
						self.arribo= True

					if banderaDerecha== False:
						if self.__rect.left < Ciudad.obtenerPosX():
							self.__rect.left = self.__rect.left + 2
						else:
							self.__rect.left = self.__rect.left -2

					if banderaArriba == False:
						if self.__rect.top < Ciudad.obtenerPosY():
							self.__rect.top = self.__rect.top +2
						else:
							self.__rect.top = self.__rect.top -2

				else:
					self.recorrido = False