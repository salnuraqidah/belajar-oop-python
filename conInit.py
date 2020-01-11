class Hero:
	#class variabel
	jumlah = 0

	def __init__(self,inputName,inputHealth,inputPower,inputArmor): #init akan dieksekusi saat pertama kali objek dibuat
		#print("hallo", x)
		#instances variabel
		self.name = inputName #self mlik objek hero1,hero2,hero3
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputPower

hero1 = Hero('snipper', 100, 10, 4) #ini objek
hero2 = Hero('mirana', 100, 15, 1)
hero3 = Hero('ucup', 1000, 100, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero2.__dict__)
print(Hero.__dict__) #ini ga ada atributnya, coba tambahin class variabel diatas "jumlah"
