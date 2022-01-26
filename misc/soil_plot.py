import smbus2
from time import sleep
import time
from datetime import datetime
import os
import matplotlib.pyplot as plt


filewrite=open("data_soil_plot.csv","a")
if os.stat("data_soil_plot.csv").st_size ==0:
	filewrite.write("Time, Soil Reading\n")


port = 1
address = 0x28 # soil sensor default address
bus = smbus2.SMBus(port)
command = 0x05 #reading command for I2C comm

#initialize data arrays
fig= plt.figure()
dataTimer=[]
dataSoil=[]


interval = 10 #minutes
duration = 5*60 #minutes

#display on screen 40 values seperated by 1 seconds (humidity, pressure, temp)
i = 0
while (interval*i) < duration:
	now=datetime.now()  #get current time
	soil = bus.read_word_data(address, command)
	dataTimer.append(i)
	dataSoil.append(soil)
	filewrite.write(str(now) + ",  " + str(soil) + "\n")
	print(time, soil)
	sleep(interval*60) #sleep for interval*60 seconds
	i += 1

#Create plot, save and display
plt.title('Soil Reading of Office Plant for 1 Day')
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Soil Reading')
plt.plot(dataTimer,dataSoil,color='black',marker='o',markerfacecolor='red')
plt.savefig("soilplot.png")
plt.show()

filewrite.close()
