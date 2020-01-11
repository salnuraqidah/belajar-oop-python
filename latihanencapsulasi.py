class Hero:

	#private class variabel
	__jumlah = 0

	def __init__(self, name, health, power, armor):
		self.__name = name
		self.__healthStandar = health
		self.__powerStandar = power
		self.__armorStandar = armor
		self.__level = 1
		self.__exp = 0

		self.__helathMax = self.__healthStandar * self.__level
		self.__power = self.__powerStandar * self.__level
		self.__armor = self.__armorStandar * self.__level

		self.__health = self.__helathMax

		Hero.__jumlah += 1

	@property
	def info(self):
		return "{} level {}: \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,self.__level, self.__health,self.__helathMax, self.__power,self.__armor)

	@property
	def gainExp(self):
		pass

	@gainExp.setter
	def gainExp(self, addExp):
		self.__exp += addExp
		if(self.__exp >= 100):
			print(self.__name, 'level up')
			self.__level += 1
			self.__exp -= 100

			self.__helathMax = self.__healthStandar * self.__level
			self.__power = self.__powerStandar * self.__level
			self.__armor = self.__armorStandar * self.__level

	def attack(self, musuh):
		self.gainExp = 50
			

fatih = Hero("fatih",100, 5, 10)
syafiq = Hero("syafiq",100, 5, 10)
print(fatih.info)		

# fatih.gainExp = 50
# fatih.gainExp = 80

fatih.attack(syafiq)
fatih.attack(syafiq)
fatih.attack(syafiq)
print(fatih.info)
print(fatih.gainExp)