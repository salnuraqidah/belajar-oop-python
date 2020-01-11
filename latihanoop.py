class Hero:

	def __init__(self, name, health, power, armor):
		self.name = name
		self.health = health
		self.power = power
		self.armor = armor

	def serang(self, lawan):
		print(self.name + ' menyerang ' + lawan.name) #interaksi antar objek, self milik fatih, lawan milik syafiq		
		lawan.diserang(self, self.power)

	def diserang(self, lawan, power_lawan):
		print(self.name + ' diserang ' + lawan.name)
		power_diterima = power_lawan/self.armor
		print('attack terasa : ' + str(power_diterima))
		self.health -= power_diterima
		print('darah ' + self.name + ' tersisa ' + str(self.health))

fatih = Hero('fatih', 100, 10, 5)
syafiq = Hero('syafiq', 200, 5, 2)

fatih.serang(syafiq) #fatih objek self
print('\n')
syafiq.serang(fatih)	#syafiq objek self
fatih.serang(syafiq)
print('\n')
syafiq.serang(fatih)	
fatih.serang(syafiq)
print('\n')
syafiq.serang(fatih)	
fatih.serang(syafiq)
print('\n')
syafiq.serang(fatih)	
fatih.serang(syafiq)
print('\n')
syafiq.serang(fatih)	
		
		