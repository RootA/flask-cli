import optparse
import os, time
import shutil
import colorama

from os import listdir, sep
from os.path import abspath, basename, isdir
from sys import argv

version = '0.1.1'

colorama.init(autoreset=True)

def createProjectDir(name):
	if not os.path.isdir(name):
		os.makedirs(name)
		os.chdir(name)
		shutil.copytree('../flaskcli/base_templates/default/app', 'app', symlinks=False, ignore=None)
	else:
		print('Name seems to already be taken in the current dir')
		new_name = input()
		createProjectDir(new_name)


def createVersionedProjectDir(name):
	if not os.path.isdir(name):
		os.makedirs(name)
		os.chdir(name)
		shutil.copytree('../flaskcli/base_templates/versioned/app', 'app', symlinks=False, ignore=None)
	else:
		print('Name seems to already be taken in the current dir')
		new_name = input()
		createProjectDir(new_name)


def tree(dir, padding, print_files=True):
	print(padding[:-1] + '+-' + basename(abspath(dir)) + '/')
	padding = padding + ' '
	files = []
	if print_files:
		files = listdir(dir)
	else:
		files = [x for x in listdir(dir) if isdir(dir + sep + x)]
	count = 0
	for file in files:
		count += 1
		print(padding + '|')
		path = dir + sep + file
		if isdir(path):
			if count == len(files):
				tree(path, padding + ' ', print_files)
			else:
				tree(path, padding + '|', print_files)
		else:
			print(padding + '+-' + file)

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
	print('				Python : '+ colorama.Fore.YELLOW +  '3')

	p = optparse.OptionParser()
	p.add_option('--name', '-p', default="default")
	options, arguments = p.parse_args()
	print(colorama.Fore.GREEN + 'Project Name : ' + colorama.Fore.WHITE + '{}'.format(options.name))
	print('How would like to set up the project : ')
	print(colorama.Fore.RED + '       1. Default')
	print(colorama.Fore.BLUE + '       2. Versioned (recommended)')
	get_option = input()
	if int(get_option) == 1:
		print(colorama.Fore.MAGENTA + "No fancy stuff needed")
		createProjectDir(options.name)
		print(colorama.Fore.CYAN + '{} is been created : listing the directory structure'.format(options.name))
		time.sleep(3)
		tree('.', '')
		print(colorama.Fore.GREEN + 'Project creation complete : ' + colorama.Fore.LIGHTYELLOW_EX + 'HAPPY CODING !!!')
	elif int(get_option) == 2:
		print('------------ ' + colorama.Fore.RED + 'The Urls will obey the following formart : ' + colorama.Fore.GREEN + ' ------------')
		print('------------ ' + colorama.Fore.MAGENTA + 'http://address:port/version_number/endpoint_name' + colorama.Fore.GREEN + ' ------------')
		print('------------ ' + colorama.Fore.WHITE + 'http://127.0.0.1:5000/v1/users' + colorama.Fore.GREEN + ' ------------')
		createVersionedProjectDir(options.name)
		print(colorama.Fore.CYAN + ('{} has been created'.format(options.name)))
		time.sleep(4)
		tree('.', '')
		print(colorama.Fore.GREEN + 'Project creation complete : ' + colorama.Fore.LIGHTYELLOW_EX + 'HAPPY CODING !!!')


if __name__ == '__main__':
	main()
