class Hero: #template
	#class variabel
	jumlah = 0

	def __init__(self,inputName,inputHealth,inputPower,inputArmor): #init akan dieksekusi saat pertama kali objek dibuat
		#print("hallo", x)
		#instances variabel
		self.name = inputName #self mlik objek hero1,hero2,hero3
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputPower
		Hero.jumlah += 1
		print('membuat Hero dengan nama ' + inputName)

hero1 = Hero('snipper', 100, 10, 4) #ini objek
print(Hero.jumlah)
hero2 = Hero('mirana', 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero('ucup', 1000, 100, 0)
print(Hero.jumlah)

