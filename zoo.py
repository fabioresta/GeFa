#!/usr/bin/python
# coding=utf8

# importiamo funzioni utili
from time import sleep
from random import randint, shuffle


# importiamo le classi
from Cane import *
from Cavallo import *
from Leone import *

# lista degli animali da generare, inizialmente vuota
zoo = []

# possibili nomi degli animali - lista di 5 nomi random
nomi_cani = [ "Lassie", "Rocky", "Laika", "Lucky", "Tobia" ]
nomi_cavalli = [ "Freccia", "Spirit", "Stella", "Strike", "Furia" ]
nomi_leoni = [ "Leo", "Leonida", "Leonzio", "Simba", "Lebi" ]

# possibili caratteristiche degli animali 
razze_cani = [ "pastore", "levriero", "maremmano", "schnauzer", "barboncino", "bassotto" ]
mantelli_cavalli = [ "nero", "baio", "pezzato", "fulvo" ]
pesi_leoni = range(150,225)

# generazione numero di animali da creare per ogni specie
num_cani = randint(1,10) 
num_cavalli = randint(1,10) 
num_leoni = randint(1,10) 

# eta' massime
max_eta_cane = 20
max_eta_cavallo = 25
max_eta_leone = 20

# crea i cani
for i in range(num_cani):
	zoo.append(
		Cane(
			nome = nomi_cani[randint(0,len(nomi_cani)-1)],
			eta = randint(1,max_eta_cane),
			#razza = 10  #attenzione alle concatenazioni con valori dati da input			
			razza = razze_cani[randint(0,len(razze_cani)-1)]
		)
	)

# crea i cavalli
for i in range(num_cavalli):
	zoo.append(
		Cavallo(
			nome = nomi_cavalli[randint(0,len(nomi_cavalli)-1)],
			eta = randint(1,max_eta_cavallo),
			mantello = mantelli_cavalli[randint(0,len(mantelli_cavalli)-1)]
		)
	)

# crea i leoni
for i in range(num_leoni):
	zoo.append(
		Leone(
			nome = nomi_leoni[randint(0,len(nomi_leoni)-1)],
			eta = randint(1,max_eta_leone),
			peso = pesi_leoni[randint(0,len(pesi_leoni)-1)]
		)
	)

# mischia tutti gli animali in-place -> modifica zoo
shuffle(zoo)

# usiamo gli oggetti animali
for i in range(20):
	# scegliamo un animale a caso
	id_zoo = randint(0,len(zoo)-1)
	# scegliamo una azione a caso
	id_azione = randint(0,4)
	# bestia fa riferimento all'animale scelto
	bestia = zoo[id_zoo]

	# costruiamo la frase
	frase = bestia.nome()
	frase = frase + " (età "
	frase = frase + str(bestia.eta())
	frase = frase + " anni, "
	frase = frase + bestia.info()
	frase = frase + ") "

	# e effettuiamo l'azione
	if id_azione == 0:
		frase = frase + bestia.parla()
	elif id_azione == 1:
		frase = frase + bestia.si_muove()
	elif id_azione == 2:
		frase = frase + bestia.mangia()
	elif id_azione == 3:
		frase = frase + bestia.beve()
	elif id_azione == 4:
		periodo = bestia.dorme(randint(1,3))
		frase = frase + "ha dormito per "
		frase = frase + str(periodo)
		frase = frase + " secondi"

	print frase

	# sospensione per 1 secondo tra un animale e l'altro
	sleep(1)

