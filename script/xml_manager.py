from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom

class xmlParser:
	"""
		xmlParser analyses the XML file to convert it in a "param.txt"
		file required by NOMAD.
	"""
	
	column_size = 20 

	def __init__(self, xml_file, path):
		self.xml_parse = minidom.parse(path + xml_file)
		self.path = path

	def parsetotxt(self, txt_file):
		txt_file = open(self.path + txt_file, 'w')

		root = self.xml_parse.documentElement

		for param in root.childNodes:
			attr_name = param.getAttribute('name')
			real_colum_size = xmlParser.column_size-len(attr_name)
			txt_file.write(attr_name + " "*real_colum_size)
			if (attr_name == "X0" or
				attr_name == "LOWER_BOUND" or
				attr_name == "UPPER_BOUND" or
				attr_name == "BB_INPUT_TYPE"):
				txt_file.write("( ")


			for arg in param.childNodes:
				attr_value = arg.getAttribute('value')
				txt_file.write(attr_value + " ")

			if (attr_name == "X0" or
				attr_name == "LOWER_BOUND" or
				attr_name == "UPPER_BOUND" or
				attr_name == "BB_INPUT_TYPE"):
				txt_file.write(")")

			txt_file.write("\n")

		txt_file.close()

class xmlCreator:
	"""
		xmlCreator create an well-formated XML file from the blackbox
		information and the configuration file. 
	"""
	def __init__(self):
		self.root = minidom.Document()
		self.nomad = self.root.createElement('nomad_parameters')

		self.root.appendChild(self.nomad)

	def addParameter(self, name, arg_type, args):
		param_element = self.root.createElement('param')

		param_type = self.root.createAttribute('type')
		param_name = self.root.createAttribute('name')

		param_type.nodeValue = arg_type
		param_name.nodeValue = name

		param_element.setAttributeNode(param_type)
		param_element.setAttributeNode(param_name)

		for value in args:
			arg_element = self.root.createElement('arg')

			arg_value = self.root.createAttribute('value')
			arg_value.nodeValue = str(value)

			arg_element.setAttributeNode(arg_value)

			param_element.appendChild(arg_element)
			self.nomad.appendChild(param_element)

	def __str__(self):
		"""Return a pretty-printed XML string for the Element."""
		return self.root.toprettyxml()

	def writexml(self, file_name):
		file_xml = open(file_name,"w")
		self.root.writexml(file_xml)
		#file_xml.write(self.root.toprettyxml())
		file_xml.close()

