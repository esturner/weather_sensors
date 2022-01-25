# -*- coding: utf-8 -*-
"""
analyze.py
By Ethan Turner
analyze data from soil sensors

Created on Wed Dec  8 21:31:45 2021

@author: etran
"""
import matplotlib.pyplot as plt
import numpy as np
import datetime
import os
import sys
from dateutil import parser

def getFileType(filename):
    '''returns file type string'''
    return filename.split('.')[-1]

def csv_to_data(filename, contains_time = True):
    '''converts csv to data array
    returns data dictionary'''
    data_dict = {}
    with open(filename, 'r') as f:
        categories = f.readline().strip().split(',')
        for x in range(len(categories)):
            categories[x] = categories[x].strip()
            data_dict[categories[x]] = []
        #print(categories)
        for line in f:
            line_data = line.strip().split(',')
            if len(line_data) == len(categories):
                for x in range(len(line_data)):
                    #append datetime objects for times
                    if categories[x] == 'Time':
                        t = convert_to_datetime(line_data[x]) 
                        data_dict[categories[x]].append(t)
                    elif categories[x].split(' ')[0].strip() == 'Soil':
                        cleaned_data = float(line_data[x].strip())
                        scaled = scale_soil(cleaned_data)
                        data_dict[categories[x]].append(scaled)
                    else:
                        cleaned_data = float(line_data[x].strip())
                        data_dict[categories[x]].append(cleaned_data)
    return data_dict

def convert_to_datetime(time_string):
    time = parser.parse(time_string)
    return time

def scale_soil(soil_reading, bias = 3.3):
    n_bits = 10
    bit_scale = bias/(2**n_bits)
    scaled = soil_reading*bit_scale
    return scaled

#plot formatting
import matplotlib.pyplot as plt
import numpy as np
import analysis
import datetime
#helpter functions num2date() and date2num to convert to/from
from matplotlib import dates as mPlotDATEs
from matplotlib.dates   import  DateFormatter,  \\ 
                                AutoDateLocator,   \\
                                HourLocator,        \\
                                MinuteLocator,       \\
                                epoch2num

    "t = []\n",
    "start_date = datetime.datetime(2021, 12, 6)\n",
    "for time in data['Time']:\n",
    "    t.append(time)\n",
    "\n",
    "#prep data    \n",
    "soil1 = data['Soil 1']\n",
    "soil2 = data['Soil 2']\n",
    "soil3 = data['Soil 3']\n",
    "temp = data['temperature']\n",
    "press = data['pressure']\n",
    "hum = data['humidity']\n",
    "#print(soil1)\n",
    "\n",
    "#start plot\n",
    "fig, ax = plt.subplots(2,2, figsize = (10,8))\n",
    "label_size = 14\n",
    "#plot of soil\n",
    "ax[0,0].plot(t, soil1, '.-')\n",
    "ax[0,0].plot(t, soil2, '.-')\n",
    "ax[0,0].plot(t, soil3, '.-')\n",
    "ax[0,0].set_xlim(start_date, t[-1])\n",
    "ax[0,0].set_ylim(0,2)\n",
    "ax[0,0].set_xlabel('Date (Day-Hour)', size = label_size)\n",
    "ax[0,0].set_ylabel('Soil Reading (V)', size = label_size)\n",
    "legend = ['Sensor Depth: 3\"', 'Sensor Depth: 8\"', 'Sensor Depth: 12\"']\n",
    "ax[0,0].legend(legend)\n",
    "#plot of temperature\n",
    "ax[0,1].plot(t, temp, 'k.-')\n",
    "ax[0,1].set_xlim(start_date, t[-1])\n",
    "ax[0,1].set_xlabel('Date (Day-Hour)', size = label_size)\n",
    "ax[0,1].set_ylabel('Temperature (C)', size = label_size)\n",
    "#plot of humidity\n",
    "ax[1,0].plot(t, hum, 'b.-')\n",
    "ax[1,0].set_xlim(start_date, t[-1])\n",
    "ax[1,0].set_xlabel('Date (Day-Hour)', size = label_size)\n",
    "ax[1,0].set_ylabel('Relative Humidity (%)', size = label_size)\n",
    "#plot of pressure\n",
    "ax[1,1].plot(t, press, 'g.-')\n",
    "ax[1,1].set_xlim(start_date, t[-1])\n",
    "ax[1,1].set_xlabel('Date (Day-Hour)', size = label_size)\n",
    "ax[1,1].set_ylabel('Pressure (hPa)', size = label_size)\n",
    "ax[1,1].set_ylim(995, 1012)\n",
    "\n",
    "#format date\n",
    "for i in range(len(ax)):\n",
    "    for j in range(len(ax[i])):\n",
    "        ax[i,j].xaxis.set_major_locator(   AutoDateLocator() )\n",
    "        ax[i,j].xaxis.set_major_formatter( DateFormatter( '%d -%H' ));\n",
    "        #ax[i,j].xaxis.set_minor_formatter( DateFormatter( '%h' ));\n",
    "    # Rotates and right-aligns the x labels so they don't crowd each other.\n",
    "        for label in ax[i,j].get_xticklabels(which='major'):\n",
    "            label.set(rotation=30, horizontalalignment='right')\n",
    "#ax[0,0].setp(plt.gca().get_xticklabels(),rotation= 90, horizontalalignment = 'right');\n",
    "plt.tight_layout()\n",
    "plt.savefig('prelimary_data.png', transparent = False)\n",
def time_plot(time_start , time_stop, y_axis = 'Soil 1'):
    fig, ax = plt.subplots(1,1 )

def main():
    #data = csv_to_data('data_soil_depth.csv')
    #t0 = data['Time'][0]
    #print(data.keys())
    return
    
    
if __name__ == '__main__':
    main()
