import sys, os, re
from src.exceptions import InvalidPathException, NoneException, BlackBoxException
from src.config import *
from src.bb_parser import *
from src.nomad import *
from src.instances import *

def main():
	"""
		Title: NomadScript
		Description: A tool for automatic NOMAD managment from a well
		configurated blackbox.
		Author: Valentin Laurent (@vlnk)
		URL: https://github.com/vlnk/nomad-script

		Notes:  Please note this tool may contain errors, and
		    is provided "as it is". There is no guarantee
		    that it will work on your target systems(s), as
		    the code may have to be adapted. 
		    This is to avoid script kiddie abuse as well.
	"""
	
	if (len(sys.argv) != 2):
		print("USAGE : {} <blackbox_path>".format(sys.argv[0]))

	else:
		regex = '^(.*/)?(?:$|(.+?)(?:(\.[^.]*$)|$))'
		args = re.compile(regex).search(sys.argv[1])

		try:
			bb_path = args.group(1)
			bb_name = args.group(2)

			if not os.access(bb_path + bb_name, os.W_OK):
				raise InvalidPathException(sys.argv[0])
			else:
				print("--> LOAD CONFIGURATIONS")
				xml_file = "param.xml"
				txt_file = "param.txt"
				config = Configuration(bb_path)

				print("--> PARSE BLACKBOX")
				new_bb = BlackBoxParser(bb_path,bb_name, config)
				new_bb.toxml(xml_file)

				print("--> IMPLEMENT NOMAD")
				nomad = NomadManager(xml_file, txt_file, bb_path)
				manager = InstancesManager(new_bb.instance_path, config.dic['instances_directory'], nomad.nomad_bin, bb_path)
				manager.run()

		except InvalidPathException as e:
			print("Invalid path : {}".format(e.value))

		except NoneException as e:
			print("The {} is not found !".format(e.value))

		except BlackBoxException as e:
			print("The blackbox is incomplete !")
			print("Please, {} field must be completed.".format(e.value))

		except TypeError:
			print("Invalid argument !")

if __name__ == "__main__":
	main()

