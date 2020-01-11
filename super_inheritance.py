class Hero:
	def __init__(self,name,helath):
		self.name = name
		self.helath = helath

	def showInfo(self):
		print("{} dengan helath: {}".format(self.name, self.helath))


# class Hero_inteligent(Hero): -- malah jadi perulangan
# 	def __init__(self, name):
# 		self.name = name
# 		self.helath = 100

class Hero_inteligent(Hero):
	def __init__(self, name):
		#Hero.__init__(self, name, 100)
		super().__init__(name, 100) #memanggil super class
		super().showInfo()

# class Hero_strength(Hero):
# 	def __init__(self,name):
# 		self.name = name
# 		self.helath = 200

class Hero_strength(Hero):
	def __init__(self,name):
		#Hero.__init__(self, name, 200)
		super().__init__(name, 200) #memanggil super class
		super().showInfo()


fatih = Hero_inteligent('fatih')
syafiq = Hero_strength('syafiq')

print(fatih.name, " " , fatih.helath)
print(syafiq.name, " " , syafiq.helath)		


