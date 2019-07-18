class Animal:
	def __init__(self, kind):
		self.kind = kind

	def print_kind(self):
		print(self.kind)

		#instance method
Animal1 = Animal("domestic")
Animal1.print_kind()

	#class method
	@classmethod
	def sound(cls, x):
	print(x)
Animal.sound ("woof")

