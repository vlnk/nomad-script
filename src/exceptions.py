class ArgsException(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return "Invalid argument : {}".format(repr(self.value))

class InvalidPathException(Exception):
	def __init__(self, value):
		self.value = value

class NoneException(Exception):
	def __init__(self, value):
		self.value = value

class BlackBoxException(Exception):
	def __init__(self, value):
		self.value = value