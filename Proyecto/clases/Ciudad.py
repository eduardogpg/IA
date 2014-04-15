import pygame, sys
from pygame.locals import *
import threading
import time

class Ciudad(pygame.sprite.Sprite, threading.Thread):
	
	def __init__(self, posx, posy, ruta):
		threading.Thread.__init__(self)
		pygame.sprite.Sprite.__init__(self)

		self.imagenCirculo = pygame.image.load(ruta)

		self.__rect = self.imagenCirculo.get_rect()
		self.__rect.top, self.__rect.left = (posy-(self.__rect.height/2)),(posx-(self.__rect.width/2))
		
		if self.__rect.top % 2 :
			self.__rect.top =self.__rect.top +1

		if self.__rect.left % 2 :
			self.__rect.left = self.__rect.left +1

		self.bandera = True

	def run(self):
		while self.bandera:
			self.siguienteImagen()
			time.sleep(0.1000)

	def dibujar(self, superficie):
		superficie.blit(self.imagenCirculo, self.__rect)

	def obtenerPosX(self):
		return self.__rect.left

	def obtenerPosY(self):
		return self.__rect.top
