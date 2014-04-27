import re, os
from script.exceptions import InvalidPathException

class Configuration:
	"""
		Configuration object contains all of the functions 
		to configurate the script.
		It analyses the file config.txt in the binary folder
		and parse all the configuration write by the user. If
		no config.txt was found it raises an exeption, if the
		user don't write any configuration, all these parameters 
		will not be take into account during the NOMAD implementation.

		It contains the following methods:

			*) __init__(self, config_path)
		Check if the config.txt file is in the blackbox folder and open it.

			*) checkParam(self, string)
		Check the value of each parameter for the configuration.

			*) parseConfigFile(self)
		Check all the lines of the file and put all configuration parameters
		into a variable in order to use them during the NOMAD implementation.

			*) __len__(self) [debug]
			*) __str__(self) [debug]
	"""

	def __init__(self, config_path):
		self.dic = {}
		self.path = config_path + "config.txt"

		if os.path.exists(self.path):
			self.config_file = open(self.path, 'r')
		else:
			raise InvalidPathException(self.path)

		self.parseConfigFile()

	def checkParam(self, string):
		if (string.upper() == "NONE"):
			return None
		else:
			return string

	def parseConfigFile(self):
		#regex expression
		r_param = re.compile(r'PARAMETERS_ON_COMMAND_LINE\s=\s(.*)')
		r_max_time = re.compile(r'MAX_TIME\s=\s(.*)')
		r_max_eval = re.compile(r'MAX_BB_EVAL\s=\s(.*)')
		r_tmp_dir = re.compile(r'TMP_DIR\s=\s(.*)')
		r_direction = re.compile(r'DIRECTION_TYPE\s=\s(.*)')
		r_target = re.compile(r'F_TARGET\s=\s(.*)')
		r_initial = re.compile(r'INITIAL_MESH_SIZE\s=\s(.*)')
		r_search = re.compile(r'LH_SEARCH\s=\s(.*)')
		r_cache = re.compile(r'CACHE_FILE\s=\s(.*)')
		r_display_eval = re.compile(r'DISPLAY_ALL_EVAL\s=\s(.*)')
		r_display_degree = re.compile(r'DISPLAY_DEGREE\s=\s(.*)')
		r_display_stats = re.compile(r'DISPLAY_STATS\s=\s(.*)')
		r_history = re.compile(r'HISTORY_FILE\s=\s(.*)')
		r_solution = re.compile(r'SOLUTION_FILE\s=\s(.*)')
		r_stats = re.compile(r'STATS_FILE\s=\s(.*)')
		r_instance = re.compile(r'INSTANCES_DIRECTORY\s=\s(.*)')


		for line in self.config_file.readlines():
			if not line.startswith('#'):

				self.dic['parameters_on_command_line'] = self.dic.get('parameters_on_command_line', None)
				if (r_param.match(line)):
					string = str(r_param.match(line).group(1))
					self.dic['parameters_on_command_line'] = self.checkParam(string)

				self.dic['max_time'] = self.dic.get('max_time', None)
				if (r_max_time.match(line)):
					string = str(r_max_time.match(line).group(1))
					self.dic['max_time'] = self.checkParam(string)

				self.dic['max_bb_eval'] = self.dic.get('max_bb_eval', None)
				if (r_max_eval.match(line)):
					string = str(r_max_eval.match(line).group(1))
					self.dic['max_bb_eval'] = self.checkParam(string)

				self.dic['tmp_dir'] = self.dic.get('tmp_dir', None)
				if (r_tmp_dir.match(line)):
					string = str(r_tmp_dir.match(line).group(1))
					self.dic['tmp_dir'] = self.checkParam(string)

				self.dic['direction_type'] = self.dic.get('direction_type', None)
				if (r_direction.match(line)):
					string = str(r_direction.match(line).group(1))
					self.dic['direction_type'] = self.checkParam(string)

				self.dic['f_target'] = self.dic.get('f_target', None)
				if (r_target.match(line)):
					string = str(r_target.match(line).group(1))
					self.dic['f_target'] = self.checkParam(string)

				self.dic['initial_mesh_size'] = self.dic.get('initial_mesh_size', None)
				if (r_initial.match(line)):
					string = str(r_initial.match(line).group(1))
					self.dic['initial_mesh_size'] = self.checkParam(string)

				self.dic['lh_search'] = self.dic.get('lh_search', None)
				if (r_search.match(line)):
					string = str(r_search.match(line).group(1))
					self.dic['lh_search'] = self.checkParam(string)

				self.dic['cache_file'] = self.dic.get('cache_file', None)
				if (r_cache.match(line)):
					string = str(r_cache.match(line).group(1))
					self.dic['cache_file'] = self.checkParam(string)

				self.dic['display_all_eval'] = self.dic.get('display_all_eval', None)
				if (r_display_eval.match(line)):
					string = str(r_display_eval.match(line).group(1))
					self.dic['display_all_eval'] = self.checkParam(string)

				self.dic['display_degree'] = self.dic.get('display_degree', None)
				if (r_display_degree.match(line)):
					string = str(r_display_degree.match(line).group(1))
					self.dic['display_degree'] = self.checkParam(string)

				self.dic['display_stats'] = self.dic.get('display_stats', None)
				if (r_display_stats.match(line)):
					string = str(r_display_stats.match(line).group(1))
					self.dic['display_stats'] = self.checkParam(string)

				self.dic['history_file'] = self.dic.get('history_file', None)
				if (r_history.match(line)):
					string = str(r_history.match(line).group(1))
					self.dic['history_file'] = self.checkParam(string)

				self.dic['solution_file'] = self.dic.get('solution_file', None)
				if (r_solution.match(line)):
					string = str(r_solution.match(line).group(1))
					self.dic['solution_file'] = self.checkParam(string)

				self.dic['stats_file'] = self.dic.get('stats_file', None)
				if (r_stats.match(line)):
					string = str(r_stats.match(line).group(1))
					self.dic['stats_file'] = self.checkParam(string)

				self.dic['instances_directory'] = self.dic.get('instances_directory', None)
				if (r_instance.match(line)):
					string = str(r_instance.match(line).group(1))
					self.dic['instances_directory'] = self.checkParam(string)

	def __len__(self):
		return len(self.dic)

	def __str__(self):
		string = ""
		for key, value in self.dic.items():
			string = string + "{0} = {1}\n".format(key, value)

		return string
