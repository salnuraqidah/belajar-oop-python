class Hero:

	def __init__(self, name, health, armor):
		self.name = name
		self.__health = health
		self.__armor = armor
	#	self.__info = "name {} : \n\thealth {}".format(self.name,self.__health)

	@property # method sebagai variabel
	def info(self):
		return "name {} : \n\thealth {}".format(self.name,self.__health)
		
	@property
	def armor(self):
		pass

	@armor.getter
	def armor(self):
		return self.__armor

	@armor.setter
	def armor(self, input):
		self.__armor = input
		
	@armor.deleter
	def armor(self):
		print("armor di delete")
		self.__armor = None
		
	def getHealth(self):
		return self.__health

fatih = Hero("fatih", 100, 10)

print("merubah info")
print(fatih.getHealth())
print(fatih.info)
fatih.name = "stafiq"
print(fatih.info)

print("\ngetter dan setter unuk __armor:")
print(fatih.armor)
#fatih.armor = 10 --> error, armor tidak dapat berubah

#setter
fatih.armor = 50
print(fatih.armor)		

print("delete armor")
del fatih.armor
print(fatih.__dict__)