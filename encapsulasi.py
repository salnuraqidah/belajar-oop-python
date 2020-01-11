# encapsulasi
# 1. membuat semua variabel private
# 2. membuat getter dan setter
# getter mengambil variabel
# setter menset variabel

class Hero:		
 	
 	def __init__(self, name, health, power):
 		self.__name = name
 		self.__health = health
 		self.__power = power

 	# getter	
 	def getName(self):
 		return self.__name

 	def getHealth(self):
 		return self.__health	

 	# setter 
 	def diserang(self,serangPower):
 		self.__health -= serangPower

 	def setPower(self, nilaibaru):
 		self.__setPower = nilaibaru
 		

#awal dari game
fatih = Hero("Fatih", 50, 5)

print(fatih.__dict__) 		
# print(fatih.__name) --> akan error, fungsi encapsulasi memprotect nama

#game berjalan
print(fatih.getName())
print(fatih.getHealth())
fatih.diserang(5)
print(fatih.getHealth())

