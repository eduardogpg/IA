import pygame, sys
import math

from pygame.locals import *
from clases import Ciudad
from clases import AlgoritmoGenetico
from clases import Avion



def deternCiudades(listaCiudades):
	for ciudad in listaCiudades:
		ciudad.bandera= False

def graficos():

	ventana = pygame.display.set_mode((1200,800))
	pygame.display.set_caption('Rutas Aereonaves')
	
	listaCiudades = []
	
	fondo = pygame.image.load("Imagenes/mapa.jpg")
	
	Aereopuerto = Ciudad(260,303,"Imagenes/CirculoDos.fw.png") #Mi Punto de Salida
	boeing_787 = Avion(260, 303, Aereopuerto)

	banderaAlgoritmo = False
	banderaDespegue = False

	listaRutas = []

	while True:
		ventana.blit(fondo,(0,0))
	
		for event in pygame.event.get():
			if event.type == QUIT:
				deternCiudades(listaCiudades)
				pygame.quit()
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					if banderaAlgoritmo== False:
						
						miAlgoritmoGenetico = AlgoritmoGenetico(listaCiudades, Aereopuerto)
						banderaAlgoritmo= True
						miAlgoritmoGenetico.Algoritmo(100)
						boeing_787.establecerVuelos(listaCiudades, miAlgoritmoGenetico.rutaFinal)
						banderaDespegue = miAlgoritmoGenetico.despegue
						listaRutas = miAlgoritmoGenetico.rutaFinal

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if banderaAlgoritmo==False:
						posX, posY = pygame.mouse.get_pos()
						nuevaCiudad = Ciudad(posX, posY, "Imagenes/Circulo.fw.png")
						listaCiudades.append(nuevaCiudad)
					

		for ciudad in listaCiudades:
			ciudad.dibujar(ventana)
		

		if banderaDespegue== True:
			boeing_787.dibujar(ventana)
			boeing_787.ruta()

		
		for pos in range(0 , len(listaRutas)):
			ciudad = listaCiudades[ listaRutas[pos] ]
			if pos == 0:
				pygame.draw.line(ventana, (250,0,0), (Aereopuerto.obtenerPosX(), Aereopuerto.obtenerPosY()), (ciudad.obtenerPosX(), ciudad.obtenerPosY()), 2)
			if pos < len(listaRutas)-1:
				Ciudadpasada = listaCiudades[listaRutas[pos+1]]

				pygame.draw.line(ventana, (50,250,100), (Ciudadpasada.obtenerPosX(), Ciudadpasada.obtenerPosY()), (ciudad.obtenerPosX(), ciudad.obtenerPosY()), 2)
			else:
				pygame.draw.line(ventana, (0,0,250), (Aereopuerto.obtenerPosX(), Aereopuerto.obtenerPosY()), (ciudad.obtenerPosX(), ciudad.obtenerPosY()), 2)

		Aereopuerto.dibujar(ventana)
		pygame.display.update()

pygame.init()
graficos()