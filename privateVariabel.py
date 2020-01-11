class Hero:

	# class variabel
	jumlah = 0
	__privateJumlah = 0

	def __init__(self, name, health):
		self.name = name
		self.health = health

		# varibel instance private
		self.__private = "private"

		# variabel instance protected
		self._protected = "protected"


lina = Hero("Lina", 100)

print(lina.__dict__)
#lina.__private = "testing" #objek baru
print(lina._protected)
lina._protected = "testing" # perlakuannya sama kaya public namun hanya dipakai dalam class
print(lina.__dict__)
print(lina._protected)
print(Hero.__dict__)
print(Hero.__privateJumlah)

	