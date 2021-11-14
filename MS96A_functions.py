# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 13:33:16 2021

@author: Bruger
"""

import time
import numpy as np

def getStart(OSA):
    print(' ')
    OSA.write("SAR")
    startValue=float(OSA.read("A"))
    return startValue

def setStart(OSA,wavelength):
    
    currentStop=getStop(OSA)
    if wavelength > currentStop:
        print('Specified start WL of {} um is larger than current stop WL of {} um'.format(wavelength,currentStop))
        print('Please select a lower start WL')
        return
    
    
    print(' ')
    if wavelength <0.6:    
        print("Specified start wavelength of {} um is lower than 0.6 um.".format(wavelength))
        print("Please select a larger start WL")
        return
    if wavelength >1.6:        
        print("Specified start wavelength of {} um is higher than 1.6 um.".format(wavelength))
        print("Please select a smaller start WL")
        return
        
        
    OSA.write("SA"+str(wavelength))
    
    StartValue=getStart(OSA)
    print(' ')
    print('Start Wavelength set to {} um'.format(StartValue))
    print(' ')






def getStop(OSA):

    OSA.write("SOR")
    stopValue=float(OSA.read("A"))
    return stopValue

def getSpan(OSA):
    spanValues=[1000,400,200,100,40,20,10,4,2]#Span in nm
    OSA.write("SPR")
    span =int(OSA.read("A"))
    return spanValues[span]

def setSpan(OSA,wavelength):
    print(' ')
    
    #The OSA only allows certain fixed spans once the start wavelength is chosen:
    spanValues=[1000,400,200,100,40,20,10,4,2] #Span in nm
    
    #Pick the span closes to the specified value:
    spanNumber=min(range(len(spanValues)), key=lambda i: abs(spanValues[i]-wavelength))
    
    print('Requested span = {} nm. Nearest possible span = {} nm'.format(wavelength,spanValues[spanNumber]))

        
    OSA.write("SP"+str(spanNumber))
    
    currentSpan=getSpan(OSA)
    print(' ')
    print('Span is set to {} nm'.format(currentSpan))    
    print(' ')

    
def getCenter(OSA):

    OSA.write("CTR")
    centerValue=float(OSA.read("A"))
    return centerValue

def setCenter(OSA,wavelength): 
    
    if wavelength<0.6:
        print('Center wavelegth of {} um is lower than 0.6. Set to 0.7 um instead'.format(wavelength))
        wavelength=0.7
        
    if wavelength >1.6:        
        print("Specified center wavelength of {} um is higher than 1.6. Set to 1.5 um instead".format(wavelength))
        wavelength=1.5        
    
    OSA.write("CT"+str(wavelength))
    
    centerWavelength=getStop(OSA)
    
    print(' ')
    print('Center wavelength set to {} um'.format(centerWavelength))
    print('')
    
 
def getResolution(OSA):
    resValues=[10,5,2,1,0.5,0.2,0.1] #Resolution in nm
    OSA.write("RER")
    resValue=int(OSA.read("A"))
    return resValues[resValue]
    
    
def setResolution(OSA,resolution):
    print(' ')
    
    #The OSA only allows certain fixed resolutions:
    resValues=[10,5,2,1,0.5,0.2,0.1] #Resolution in nm
    resNumber=min(range(len(resValues)), key=lambda i: abs(resValues[i]-resolution))
    
    print('Requested resolution = {} nm. Nearest possible resolution = {} nm'.format(resolution,resValues[resNumber]))
    
    OSA.write("RE"+str(resNumber))
    currentResolution=getResolution(OSA)
    
    print(' ')
    print('Resolution set to {} nm'.format(currentResolution))
    print('')   


#TODO: Add function for setting linear scale



def getLogScale(OSA):
    logValues=[10,5,2,1] #dB/div   
    OSA.write("LOR")
    logValue=int(OSA.read("A"))
    return logValues[logValue]


def setLogScale(OSA,div):
    logValues=[10,5,2,1] #dB/div 
    logNumber=min(range(len(logValues)), key=lambda i: abs(logValues[i]-div))
    
    print('Requested scale = {} dB/div. Nearest possible scale = {} dB/div'.format(div,logValues[logNumber]))
    
    OSA.write("LO"+str(logNumber))
    currentScale=getLogScale(OSA)
    
    print(' ')
    print('Log Scale set to {} dB/div'.format(currentScale))
    print('')       


def getMaxRefLevel(OSA):
    OSA.write("LVR")
    maxRef=float(OSA.read("A"))
    return maxRef

def setMaxRefLevel(OSA,ref):
    OSA.write("LV"+str(ref))
    
    
    currentMaxRef=getMaxRefLevel(OSA)
    
    print(' ')
    print('Current Max Reference Level is set to {} dB'.format(currentMaxRef))
    print(' ')
    


def setAutoScale(OSA,value):
    OSA.write("AU"+str(value)) #1=True and autoscaling is done, 0=False and autoscaling is not done
    
def setHighSens(OSA,value):
    OSA.write("HI"+str(value)) #1=True and autoscaling is done, 0=False and autoscaling is not done

def setAvgNumber(OSA,averageNumber):
    averageNumber=int(averageNumber)
    OSA.write("AV"+str(averageNumber))
    
    print("Number of averages set to {}".format(averageNumber))


def doSweep(OSA):
    start=getStart(OSA)
    stop=getStop(OSA)
    span=getSpan(OSA)
    res=getResolution(OSA)
    
    print(' ')
    print('Running Sweep with:')
    print('Start WL = {} um'.format(start))
    print('Span = {} nm'.format(span))    
    print('Stop WL = {} um'.format(stop))
    print('Resolution = {} nm'.format(res))

    if span/res<10:
        print('Note: Span/Res<10. Consider increasing this ratio for a better result')
    
    OSA.write("SI")
    waitForSweepToFinish(OSA)
    
def getSweepStatus(OSA):
    OSA.write("STR")
    status=int(OSA.read("A"))
    return status
    
def waitForSweepToFinish(OSA):
    
    print(' ')
    print('Waiting for sweep to finish')
    print(' ')
    
    status=getSweepStatus(OSA)
    startTime=time.time()
    while status==1:
        time.sleep(0.5)
        status=getSweepStatus(OSA)
        currentTime=time.time()
        print('T= {:.2f} s'.format(currentTime-startTime))
        
    endTime=time.time()    
    print('Sweep finished after {:.2f} s !'.format(endTime-startTime))
        
        
  
def getData(OSA,memoryNumber):
    #The OSA can keep 4 traces in memory:
    #memoryNumber=1=DATA 1
    #memoryNumber=2=DATA 2
    #memoryNumber=3=DATA 3
    #memoryNumber=4=DATA 4
    
    
    #NOTE: 
    
    if type(memoryNumber)!=int:
        print("Error! Specified memory channel is not an integer!")
        print("Please select 1, 2, 3 or 4.")
        return
    
    if abs(memoryNumber)>4:
        print("Error! Specified memory channel greater than 4!")
        print("Please select 1, 2, 3 or 4.")
        return
    
    if abs(memoryNumber)<1:
        print("Error! Specified memory channel smaller than 1!")
        print("Please select 1, 2, 3 or 4.")
        return
    print(' ')
    print('Extracting graph data')
    data=np.array([])   
    memoryNumber=3
    for i in range(10000):
        try:
            OSA.write("DMR"+str(memoryNumber))
            dummy=OSA.read("D"+str(memoryNumber))
    
            dummy=dummy.replace('+','')
    
            dummy=dummy.replace('\n','')
    
            dummy=np.array(dummy.split(','))
    
            dummy=dummy.astype(float)
    
            data=np.append(data,dummy)
        except:
            break
    WL=np.linspace(getStart(OSA),getStop(OSA),len(data))
    print('  ')
    print('Graph data successfully extracted!')
    print('  ')
    return WL,data
    
    
def setDataMemory(OSA,memoryNumber):
    #The OSA can keep 4 traces in memory:
    #memoryNumber=1=DATA 1
    #memoryNumber=2=DATA 2
    #memoryNumber=3=DATA 3
    #memoryNumber=4=DATA 4
    
    if type(memoryNumber)!=int:
        print("Error! Specified memory channel is not an integer!")
        print("Please select 1, 2, 3 or 4.")
        return
    
    if abs(memoryNumber)>4:
        print("Error! Specified memory channel greater than 4!")
        print("Please select 1, 2, 3 or 4.")
        return
    
    if abs(memoryNumber)<1:
        print("Error! Specified memory channel smaller than 1!")
        print("Please select 1, 2, 3 or 4.")
        return
   
    OSA.write("DM"+str(memoryNumber))
    print('DATA memory set to {} '.format(memoryNumber))
    
    
    
    
    
    