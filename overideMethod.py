class Hero:
	def __init__(self,name,health):
		self.name = name
		self.health = health

	def showInfo(self):
		print("{} dengan health: {}". format(self.name,self.health))


class Hero_inteligent(Hero):
	def __init__(self,name):
		super().__init__(name,100)

	# overide method	
	def showInfo(self): #overide method --> menimpa method yang ada di super class
		print("{} \n\tTipe: Inteligent, \n\thealth: {}". format(self.name,self.health))
	
class Hero_strength(Hero):
	def __init__(self,name):
		super().__init__(name,200)

fatih = Hero_inteligent('fatih')
syafiq = Hero_strength('syafiq')		

fatih.showInfo()
syafiq.showInfo()



