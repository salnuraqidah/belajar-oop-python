class Hero:
	#class variabel
	jumlah_hero = 0

	def __init__(self, inputName, inputHealth, inputPower, inputArmor):
		#instance variabel
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor
		Hero.jumlah_hero += 1

	#method tanpa return dan argumen
	def siapa(self):
		print('namaku adalah ' + self.name)

	#method dengan argumen
	def healthUp(self,up):
		self.health += up

	#method dengan return
	def getHealth(self):
		return self.health

hero1 = Hero('snipper',100,10,5)
hero2 = Hero('fatih',200,6,3)

#print(hero1.__dict__)
#print(hero2.__dict__)

hero1.healthUp(20)
hero1.siapa()
print(hero1.health)
print(hero1.getHealth())