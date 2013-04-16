#!/usr/bin/python

# importa tutti i simboli da Animale
from Animale import *

# sottoclasse di Animale
class Cane(Animale):

	# costruttore
	def __init__(self, nome, eta, razza):
		super(Cane, self).__init__(nome, eta)
		self.__razza = razza

	# metodi implementati

	# metodo get/set per la razza
	def razza(self, razza = None):
		if (razza != None):
			self.__razza = razza
		return self.__razza

	def info(self):
		return "razza " + self.__razza

	def parla(self):
		return "abbaia"

	def si_muove(self):
		return "corre"

	

	

	
	


