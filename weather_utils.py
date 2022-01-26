'''
weather_utils.py
by Ethan Turner
started 12/03/2021

script holds functions commonly used for weather sensors
'''

import numpy as np
import matplotlib.pyplot as plt

def write_to_csv(file, message, mode = 'a'):
	'''write a csv line in 'file.csv'.
	file = file name to write to
	message = what to write
	mode = what permissions for file
	'''
	with open(file + '.csv', mode) as f:
		f.write(message)

def gen_plot(x_data, y_data, filename,x_title = '', y_title= ''):
	fig, ax = plt.subplots(1,1, figsize = (6,5))
	ax.plot(x_data, y_data)
	ax.set_xlabel(x_title)
	ax.set_ylabel(y_title)
	fig.savefig(filename, transparent = True)
	fig.show()
	
