# inheritance -- pewarisan
# misal kita punya class 1(super class) trus di turunkan ke class 2(sub class)
class Hero:

	def __init__(self, name, health):
		self.name = name
		self.health = health

class Hero_inteligent(Hero):
	pass

class Hero_strength(Hero):
	pass


fatih = Hero("fatih",100)
syafiq = Hero_inteligent("syafiq",50)
ghumi = Hero_strength("ghumi",100)
print(fatih.name)
print(syafiq.name)
print(ghumi.name)
