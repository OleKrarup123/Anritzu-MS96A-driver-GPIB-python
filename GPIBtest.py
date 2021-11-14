# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 13:02:36 2021

@author: Bruger
"""
import pyvisa as pv
import time
from MS96A_functions import *
import warnings
warnings.simplefilter("ignore", UserWarning)


GPIBname=pv.ResourceManager().list_resources()[0]
print(GPIBname)
OSA=pv.ResourceManager().open_resource(GPIBname)

time.sleep(1)
setStart(OSA,0.7)


setSpan(OSA,500)

setSpan(OSA,2)


setSpan(OSA,15)

setSpan(OSA,35)
print(getSpan(OSA))


setCenter(OSA,0.55)
setCenter(OSA,0.97)
setCenter(OSA,1.23456789)
setCenter(OSA,1.67)

setStart(OSA,1.337)
print(getStart(OSA))

setCenter(OSA,1.337)
print(getCenter(OSA))

setResolution(OSA,0.3)
print(getResolution(OSA))


setCenter(OSA,0.80)
setSpan(OSA,2)
doSweep(OSA)




setCenter(OSA,1.548)
setSpan(OSA,0.0001)
setResolution(OSA,555.4)
setMaxRefLevel(OSA,15)

setAutoScale(OSA,1)
setHighSens(OSA,1)
setDataMemory(OSA,3)

time.sleep(1)
doSweep(OSA)

WL,data=getData(OSA,3)


plt.figure()

plt.locator_params(axis='x',nbins=5)
plt.plot(WL,10*np.log10(data))
plt.xlabel('Wavelength [um]')
plt.ylabel('Pow [dB]')
plt.show()



setCenter(OSA,1.548)
setSpan(OSA,0.0001)
setResolution(OSA,0.001)
setMaxRefLevel(OSA,15)

setAutoScale(OSA,1)
setHighSens(OSA,1)
setDataMemory(OSA,3)

time.sleep(1)
doSweep(OSA)

WL,data=getData(OSA,3)


plt.figure()

plt.locator_params(axis='x',nbins=5)
plt.plot(WL,10*np.log10(data))
plt.xlabel('Wavelength [um]')
plt.ylabel('Pow [dB]')
plt.show()





setCenter(OSA,1.548)
setSpan(OSA,10)
setResolution(OSA,0.001)
setMaxRefLevel(OSA,15)

setAutoScale(OSA,1)
setHighSens(OSA,1)
setDataMemory(OSA,3)

time.sleep(1)
doSweep(OSA)

WL,data=getData(OSA,3)
plt.figure()
plt.locator_params(axis='x',nbins=5)
plt.plot(WL,10*np.log10(data))
plt.xlabel('Wavelength [um]')
plt.ylabel('Pow [dB]')
plt.show()



setCenter(OSA,1.548)
setSpan(OSA,10)
setResolution(OSA,0.5)
setMaxRefLevel(OSA,15)

setAutoScale(OSA,1)
setHighSens(OSA,1)
setDataMemory(OSA,3)

time.sleep(1)
doSweep(OSA)

WL,data=getData(OSA,3)
plt.figure()
plt.locator_params(axis='x',nbins=5)
plt.plot(WL,10*np.log10(data))
plt.xlabel('Wavelength [um]')
plt.ylabel('Pow [dB]')
plt.show()


#[10,5,2,1,0.5,0.2,0.1]
setResolution(OSA,10)
doSweep(OSA)
WL1,data1=getData(OSA,3)

setResolution(OSA,5)
doSweep(OSA)
WL2,data2=getData(OSA,3)

setResolution(OSA,2)
doSweep(OSA)
WL3,data3=getData(OSA,3)

setResolution(OSA,1)
doSweep(OSA)
WL4,data4=getData(OSA,3)

setResolution(OSA,0.5)
doSweep(OSA)
WL5,data5=getData(OSA,3)

setResolution(OSA,0.2)
doSweep(OSA)
WL6,data6=getData(OSA,3)

setResolution(OSA,0.1)
doSweep(OSA)
WL7,data7=getData(OSA,3)


plt.figure()
plt.plot(WL1,10*np.log10(data1),label='10nm')
plt.plot(WL2,10*np.log10(data2),label='5nm')
plt.plot(WL3,10*np.log10(data3),label='2nm')
plt.plot(WL4,10*np.log10(data4),label='1nm')
plt.plot(WL5,10*np.log10(data5),label='0.5nm')
plt.plot(WL6,10*np.log10(data6),label='0.2nm')
plt.plot(WL7,10*np.log10(data7),label='0.1nm')
plt.xlabel('Wavelength [um]')
plt.ylabel('Pow [dB]')
plt.legend(bbox_to_anchor=(1.05,0.75))
plt.show()










