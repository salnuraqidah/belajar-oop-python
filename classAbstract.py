# class biasa --> instancenya objek, class biasa blueprint dari objek
# class Abstract --> instancenya class, class abstrack bluprintnya class, akan memaksa class untuk mengimplementasikan methodnya

# membuat class abstrack
# abc = abstract base class

from abc import ABC,abstractmethod

class Button(ABC):

	@abstractmethod # decorator
	def click(self):
		pass
		#print("ini adalah button click")

class pushButton(Button):	

	def click(self):
		print('push button click')

class radioButton(Button):	

	def click(self):
		print('radio button click')

tombol1 = pushButton()
tombol2 = radioButton()
tombol1.click()
tombol2.click()

help(tombol1)