from setuptools import setup
setup(
	name = 'flaskcli',
	version = '0.1.0',
	packages = ['flaskcli'],
	entry_points = {
		'console_scripts': [
			'flaskcli = flaskcli.app:main'
		]
	})