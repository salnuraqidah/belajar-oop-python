class Hero:

	#private class variabel
	__jumlah = 0

	def __init__(self, name):
		self.__name = name
		Hero.__jumlah += 1

	#getter -- method ini hanya berlaku untuk objek
	def getJumlah(self):
		return Hero.__jumlah

	# method ini tidak belaku untuk objek tapi berlaku untuk kelas	
	def getJumlah1():
		return Hero.__jumlah

	# method static (decorator) -- nempel objek dan class
	@staticmethod
	def getJumlah2():
		return Hero.__jumlah

	@classmethod
	def getJumlah3(cls):
		return cls.__jumlah



fatih = Hero("fatih")
syafiq = Hero("syafiq")
ghumi = Hero("ghumi")

print(fatih.getJumlah())
print(Hero.getJumlah1())
print(Hero.getJumlah2())
print(fatih.getJumlah2())
print(Hero.getJumlah3())
print(fatih.getJumlah3())	

