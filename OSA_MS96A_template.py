# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 09:32:40 2021

@author: Bruger
"""
import pyvisa as pv #Library for sending GPIB commands via python
import time           
from MS96A_functions import *  #Custom library of functions for controlling the OSA
import numpy as np
import matplotlib.pyplot as plt
import warnings   
import pandas as pd
warnings.simplefilter("ignore", UserWarning) #Ignore spurious warnings 
from datetime import datetime




savename='OSA_spectrum_'        #Base name of saved spectrum
savepath='RecordedSpectra\\'    #Default save folder
saveformat='.csv' #.xls   .xlsx #Save data in various formats

GPIBname=pv.ResourceManager().list_resources()[0] #Get list of all devices connected via GPIB (only 1)
print(GPIBname)
OSA=pv.ResourceManager().open_resource(GPIBname)  #Open connection to OSA


setCenter(OSA,1548/1000)    #Set center wavelength in um
setSpan(OSA,10)             #Set span in nm. Possible values:       [1000,400,200,100, 40, 20, 10,4,2]
setResolution(OSA,0.5)      #Set resolution in nm. Possible values: [10  ,  5,  2,  1,0.5,0.2,0.1]
setMaxRefLevel(OSA,15)      #Set max ycale value (dB)
setLogScale(OSA,10)         #Set y scale div (db/div). Possible value: [10,5,2,1]

setAutoScale(OSA,1)         #Autoscale=1 lowers the noise floor and leads to cleaner spectra. 
                            #Keep it on by default 
setHighSens(OSA,1)          #Same for high sensitivity
setDataMemory(OSA,3)        #Keep recorded trace in OSA's internal memory 1, 2, 3 or 4

time.sleep(1)               #Wait

doSweep(OSA)                #Do sweep and record trace in OSA's internal memory

WL,power=getData(OSA,3)      #Extract data from OSA's memory and save as np.array


#Plot extracted data. Note that power is saved in linear units

plt.figure()
plt.locator_params(axis='x',nbins=5)
plt.plot(WL,10*np.log10(power))
plt.xlabel('Wavelength [um]')
plt.ylabel('Pow [dB]')
plt.show()


print('Save spectrum? Y/N')
x = input()
if x.upper()=='Y':
    
    savearray=np.array([WL,power]).T

    
    df = pd.DataFrame(savearray, columns=['WL', 'power'])
    now = datetime.now()
    now = now.strftime("%d-%m-%Y-%H-%M-%S")
    finalsavestring=savepath+savename+ now +saveformat
    df.to_csv(finalsavestring)
    print('Saved data in '+finalsavestring)

elif x.upper()=='N':
    print('Data not saved')
    
    
    
    