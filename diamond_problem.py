# diamond problem

class A:
	
	def show(self):
		print('ini adalah show A')

class B(A):
	pass
	# def show(self):
	# 	print('ini adalah show B')

class C(A):

	def show(self):
		print('ini adalah show C')

class D(B,C): # urutannya D-B-C-A
	pass

objek = D()
objek.show()
help(objek)



