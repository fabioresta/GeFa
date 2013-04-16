#!/usr/bin/python

# importa tutti i simboli da Animale
from Animale import *

# sottoclasse di Animale
class Cavallo(Animale):

	# costruttore
	def __init__(self, nome, eta, mantello):
		super(Cavallo, self).__init__(nome, eta)
		self.__mantello = mantello

	# metodi implementati

	# metodo get/set per il mantello
	def mantello(self, mantello = None):
		if (mantello != None):
			self.__mantello = mantello
		return self.__mantello

	def info(self):
		return "mantello " + self.__mantello

	def parla(self):
		return "nitrisce"

	def si_muove(self):
		return "galoppa"

	


	
