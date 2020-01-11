class A:

	def method_A(self):
		print('ini adalah method A')

class B:
	def method_B(self):
		print('ini adalah method B')

class sesuatu(A,B): # inheritance multiple
	pass


objek = sesuatu()

objek.method_A()	
objek.method_B()
