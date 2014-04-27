import os, platform
from src.xml_manager import xmlParser

class NomadManager(object):
	"""
		NomadManager will find the NOMAD path from the system variables and
		configure it with the file "param.txt".
		
		It contains the following methods:
			*) __init__(self, xml_file, txt_file, path)
		Initialize the configuration of the "param.txt" required by NOMAD
		by inctiantiating the XML parser.

			*) find_nomad(self)
		This function find the NOMAD path.
	"""
	def __init__(self, xml_file, txt_file, path):
		self.file_param = txt_file
		self.path = path
		self.nomad_bin = self.find_nomad()

		xml_parser = xmlParser(xml_file, path)
		xml_parser.parsetotxt(self.file_param)

	def find_nomad(self):
		nomad_bin = ""

		if (platform.system() == 'Windows'):
			print("Sorry, but Windows environment is not implemented yet.")
		else:
			nomad_home = os.environ["NOMAD_HOME"]
			if nomad_home:
				nomad_bin = "{0}/bin/nomad {1}".format(
					nomad_home, self.path + self.file_param)
			else:
				print("You don't install the $NOMAD_HOME")

		return nomad_bin


