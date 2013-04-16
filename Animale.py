#!/usr/bin/python

from time import sleep

class Animale(object):

	# costruttore
	def __init__(self, nome, eta):
		self.__nome = nome
		self.__eta = eta

	# metodo get/set per il nome
	def nome(self, nome = None):
		# se il nome e' definito
		if (nome != None):
			# lo assegna
			self.__nome = nome
		# in ogni caso lo ritorna
		return self.__nome

	# metodo get/set per l'eta'
	def eta(self, eta = None):
		# se l'eta' e' definita
		if (eta != None):
			# la assegna
			self.__eta = eta
		# in ogni caso la restituisce
		return self.__eta

	# metodo per dormire
	def dorme(self, secondi = 1):
		# di default dorme 1 secondo
		t = secondi
		# si sospende per t secondi
		sleep(t)
		return t

	# metodo beve - uguale per tutti quindi lo implemento
	def beve(self):
		return "beve"

	# metodo mangia - uguale per 2 sottoclassi su 3 quindi lo implemento
	def mangia(self):
		return "mangia"
#Per i metodi che fanno cose diverse per tutte le sottoclassi, 
#posso scegliere di non implementarli in Animale. Oppure si potrebbero
#implementare metodi "astratti"
#in Python non si usano classi/metodi astratti, ma si possono specificare 
#metodi che non fanno nulla - equivalenti a quelli astratti

	# equivalente di metodo astratto
	def info(self):
		pass
	                
	# equivalente di metodo astratto
	def parla(self):
		pass

	# equivalente di metodo astratto
	def si_muove(self):
		pass


	

	
	

