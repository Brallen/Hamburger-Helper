class card:
	def __init__(self, name, value):
		self.name = name
		self.value = value
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.__str__()
	def get_name(self):
		return self.name
	def get_value(self):
		return self.value
