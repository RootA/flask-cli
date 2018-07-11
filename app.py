import optparse
import os
import shutil
import colorama

from os import listdir, sep
from os.path import abspath, basename, isdir
from sys import argv

version = '1.0.1'

colorama.init(autoreset=True)

def createProjectDir(name):
	if not os.path.isdir(name):
		os.makedirs(name, mode=0777)
		os.chdir(name)

		readme = open('ReadMe.md', 'w+')
		readme.write(name)
		readme.close()
		dev_Dockerfile = open('dev.Dockerfile', 'w+')
		dev_Dockerfile.close()
		prod_Dockerfile = open('prod.Dockerfile', 'w+')
		prod_Dockerfile.close()
		compose_file = open('docker-compose.yml', 'w+')
		compose_file.close()

		requiremets_file = open('requirements.txt', 'w+')
		requiremets_file.close()

		os.makedirs('app', mode=0777)
		os.chdir('app')
		os.makedirs('database')
		os.makedirs('routes')
		shutil.copyfile('../../base_templates/config.py', 'config.py')
		shutil.copyfile('../../base_templates/run.py', 'run.py')
		shutil.copyfile('../../base_templates/models.py', 'models.py')
		shutil.copyfile('../../base_templates/manage.py', 'manage.py')
		os.chdir('routes')
		os.makedirs('v1')
		os.chdir('v1')
		shutil.copyfile('../../../../base_templates/__init__.py', '__init__.py')
		shutil.copyfile('../../../../base_templates/base_urls.py', 'base_urls.py')
		os.chdir('../../')
	else:
		print('Name seems to already be taken in the current dir')
		new_name = raw_input()
		createProjectDir(new_name)


def tree(dir, padding, print_files=True):
	print padding[:-1] + '+-' + basename(abspath(dir)) + '/'
	padding = padding + ' '
	files = []
	if print_files:
		files = listdir(dir)
	else:
		files = [x for x in listdir(dir) if isdir(dir + sep + x)]
	count = 0
	for file in files:
		count += 1
		print padding + '|'
		path = dir + sep + file
		if isdir(path):
			if count == len(files):
				tree(path, padding + ' ', print_files)
			else:
				tree(path, padding + '|', print_files)
		else:
			print padding + '+-' + file

def main():
	print(colorama.Fore.YELLOW + '''
			.---. .-.    .--.  .--. .-..-.        .--. .-.   .-.
			: .--': :   : .; :: .--': :' ;       : .--': :   : :
			: `;  : :   :    :`. `. :   '  _____ : :   : :   : :
			: :   : :__ : :: : _`, :: :.`.:_____:: :__ : :__ : :
			:_;   :___.':_;:_;`.__.':_;:_;       `.__.':___.':_;                                         
 		''')
	print('				Developer :' + colorama.Fore.YELLOW + ' Antony Mwathi')
	print('				Property of : '+ colorama.Fore.YELLOW +  'FluidTech Global')
	print('				Version : '+ colorama.Fore.YELLOW +  version)

	p = optparse.OptionParser()
	p.add_option('--name', '-p', default="default")
	options, arguments = p.parse_args()
	print(colorama.Fore.GREEN + 'Project Name : ' + colorama.Fore.WHITE + '{}'.format(options.name))
	print('How would like to set up the project : ')
	print(colorama.Fore.RED + '       1. Default')
	print(colorama.Fore.BLUE + '       2. Versioned (recommended)')
	get_option = raw_input()
	if int(get_option) == 1:
		print(colorama.Fore.MAGENTA + "No fancy stuff needed")
		createProjectDir(options.name)
		print(colorama.Fore.CYAN + '{} has been created'.format(options.name))
		tree('../', '')
	elif int(get_option) == 2:
		print('------------ ' + colorama.Fore.RED + 'The Urls will obey the following formart : ' + colorama.Fore.GREEN + ' ------------')
		print('------------ ' + colorama.Fore.MAGENTA + 'http://address:port/version_number/endpoint_name' + colorama.Fore.GREEN + ' ------------')
		print('------------ ' + colorama.Fore.WHITE + 'http://127.0.0.1:5000/v1/users' + colorama.Fore.GREEN + ' ------------')
		createProjectDir(options.name)
		print(colorama.Fore.CYAN + ('{} has been created'.format(options.name)))
		tree('../', '')


if __name__ == '__main__':
	main()
