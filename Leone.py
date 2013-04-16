#!/usr/bin/python

# importa tutti i simboli da Animale
from Animale import *

# sottoclasse di Animale
class Leone(Animale):

	# costruttore
	def __init__(self, nome, eta, peso):
		super(Leone, self).__init__(nome, eta)
		self.__peso = peso

	# metodi implementati

	# metodo get/set per il peso
	def peso(self, peso = None):
		if (peso != None):
			self.__peso = peso
		return self.__peso

	def info(self):
		return "peso " + str(self.__peso)

	def parla(self):
		return "ruggisce"

	def si_muove(self):
		return "va a caccia"

	def mangia(self):
		return "divora"

	

	
