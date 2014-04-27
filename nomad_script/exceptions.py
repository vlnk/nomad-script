class ArgsException(Exception):
	"""
		ArgsException is an Exception for invalid arguments.
	"""
	def __init__(self, value):
		self.value = value

class InvalidPathException(Exception):
	"""
		InvalidPathException is an Exception for invalid path.
	"""
	def __init__(self, value):
		self.value = value

class NoneException(Exception):
	"""
		NoneException is an Exception for required parameters for NOMAD.
	"""
	def __init__(self, value):
		self.value = value

class BlackBoxException(Exception):
	"""
		BlackBoxException is an Exception raised if the blackbox doesn't 
		provide good information with the command "-param". 
	"""
	def __init__(self, value):
		self.value = value