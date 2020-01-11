class Mangga:

	# megic method -- keyword yang sudah ada di python
	def __init__(self,name,jumlah):
		self.name = name
		self.jumlah = jumlah

	#untuk debug	
	def __repr__(self):
		return "Debug - Mangga : {} dengan jumlah {}".format(self.name, self.jumlah)
	
	#untuk produksi	
	def __str__(self):
		return "Mangga : {} dengan jumlah {}".format(self.name, self.jumlah)

	def __add__(self,objek):
		return self.jumlah + objek.jumlah
	
	@property	
	def __dict__(self):
		return "objek ini mempunyai nama dan jumlah"
		

belanja1 = Mangga('arumanis',10)
belanja2 = Mangga('manis',5)
print(belanja1)		
print(belanja2)
print(belanja1+belanja2)
print(belanja1.__dict__)