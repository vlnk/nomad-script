import os
from src.exceptions import InvalidPathException, NoneException

class InstancesManager:
	"""docstring for InstanceManager"""
	def __init__(self, path1, path2, nomad_bin, bb_path):

		self.solution_dir = bb_path + "solutions"

		if not os.path.exists(self.solution_dir):
			os.makedirs(self.solution_dir)

		if path1:
			self.path_file = path1
		else:
			raise NoneException("instances file")

		if path2:
			self.path_dir = path2
		else:
			raise NoneException("instances directory")

		if nomad_bin:
			self.nomad_bin = nomad_bin
		else:
			raise NoneException("nomad binary")

		self.instance_files = []
		if os.path.exists(self.path_dir):
			abr = os.walk(self.path_dir)
			for d in abr:
				for f in d[2]:
					self.instance_files.append(f)
		else:
			raise InvalidPathException(self.path_dir)

	def run(self):
		for f in self.instance_files:
			file = open(self.path_file, 'w')
			file.write(self.path_dir + "/" + f)
			file.close()
			print("\tINSTANCE: " + f)
			os.system(self.nomad_bin + "> " + self.solution_dir + '/' + f)

