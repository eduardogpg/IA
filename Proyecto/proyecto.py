import pygame, sys
import math

from pygame.locals import *
from clases import Ciudad
from clases import AlgoritmoGenetico
from clases import Avion
from clases import Permutaciones
from clases import RecocidoSimulado

def deternCiudades(listaCiudades):
	for ciudad in listaCiudades:
		ciudad.bandera= False

def graficos(opcion):

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
						
						banderaAlgoritmo= True
							
						if opcion == 1:
							
							miAlgoritmoGenetico = AlgoritmoGenetico(listaCiudades, Aereopuerto)
							miAlgoritmoGenetico.Algoritmo(1000)
							listaRutas = miAlgoritmoGenetico.rutaFinal
						
						elif opcion == 2:
							
							miDeterminista = Permutaciones(len(listaCiudades), Aereopuerto,listaCiudades)
							miDeterminista.Algoritmo(miDeterminista.obtenerMatriz())
							listaRutas = miDeterminista.mejorRuta
							
						elif opcion == 3 :
							miRecocido = RecocidoSimulado(len(listaCiudades), listaCiudades)
							miRecocido.algoritmo()
							listaRutas = miRecocido.ruta

						boeing_787.establecerVuelos(listaCiudades, listaRutas )
						banderaDespegue = True

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if banderaAlgoritmo==False:
						
						if opcion == 2:
							if len(listaCiudades)<6:
								posX, posY = pygame.mouse.get_pos()
								nuevaCiudad = Ciudad(posX, posY, "Imagenes/Circulo.fw.png")
								listaCiudades.append(nuevaCiudad)
						else:
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
			
			if pos < len(listaRutas)-1:	
				siguienteCiudad = listaCiudades[listaRutas[pos+1]]
				pygame.draw.line(ventana, (50,250,100), (siguienteCiudad.obtenerPosX(), siguienteCiudad.obtenerPosY()), (ciudad.obtenerPosX(), ciudad.obtenerPosY()), 2)
				
		Aereopuerto.dibujar(ventana)
		pygame.display.update()


pygame.init()
print "Opciones : \n1-Algoritmo Genetico \n2-Determinista \n3-Recocido Simulado "
opcion = input("Selecciona una opcion : ")
graficos( opcion )