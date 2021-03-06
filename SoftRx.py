################################################################################
# SoftRx_ICU
#
# Created: 2015-11-06 16:31:10
#
# This software creates a serial receiver on any digital pin of an MCU running VIPER python.
# It was developed and tested on a viperized Photon board (Particle Photon).
#
# Copyright (c) 2015 A.C. Betz.  All right reserved. Developed using the VIPER IDE. 
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
#############################################################################################################################

#########
#
# this code is waiting for an 8bit number flanked by a 2bit start and stop signal (each a [1,0] tuple)
# so it's looking for this kind of signal:
# __                           __
#   |__--|--|--|--|--|--|--|--|  |__
#
# start| 8 bit binary         |stop
#
# as far as I'm aware the arduino SoftSerial library only sends a LOW start bit and a HIGH stop bit. 
# The start bit would be OK for this code (it's looking for a falling edge to start capture), but it doesn't cope well with just a HIGH stop bit.
#########

#import necessary libraries
import icu

global RxBuffer
global RxBufferTMP

#############################################################################################################################

############
#########
# functions
#########

#########
# convert RxBuffer to decimal
#########
def SoftRx_Bin2Dec(_BinList):
    global tmpDec
    tmpDec = 0
    for i in range(8):
        tmpDec += _BinList[i]*(2**i)
    return tmpDec
    _BinList[0:8] = []

#########
# round of values
#########
def round(_x):
    if _x - int(_x) >0.5: # int() always rounds towards zero & _x always >0
        return _x+1
    else:
        return _x

    
#########
# receive data on the software serial port using InputCaptureUnit
#########
#
# this code is waiting for an 8bit number flanked by a 2bit start and stop signal (each a [1,0] tuple)
# so it's looking for this kind of signal:
# __                           __
#   |__--|--|--|--|--|--|--|--|  |__
#
# start| 8 bit binary         |stop
#
# as far as I'm aware the arduino SoftSerial library only sends a LOW start bit and a HIGH stop bit. 
# The start bit would be OK for this code (it's looking for a falling edge to start capture), but it doesn't cope well with just a HIGH stop bit.
#########

def Rx_1byte_ICU(_receivepin,_baudrate):

    duration1bitMICROS = int(round((1/_baudrate)*(10**6))) # 1s = 10^6 microseconds, rounded to next integer

    #wait for a falling edge to start capturing
    tmpICU = icu.capture(_receivepin,LOW,8,int(10*(round(1/_baudrate))*(10**6)),time_unit=MICROS)#returns a list of microseconds
    #create binary list from tmpICU
    timeListICU = [int(round(x/duration1bitMICROS)) for x in tmpICU] #list of times in units of bit duration
    BinListICU = [] # initiate list of binary values created from the microseconds list coming from the ICU
    for i in range(len(tmpICU)):
        if i%2==0:
            for j in range(timeListICU[i]):
                BinListICU.append(0)
        else:
            for j in range(timeListICU[i]):
                BinListICU.append(1)
    BinListICU[0:1] = [] #remove start bit

    if len(BinListICU) < 8: #fill up all 8 bits
        for i in range(8-len(BinListICU)):
            BinListICU.append(0)

    Buffer = SoftRx_Bin2Dec(BinListICU)
    return Buffer    # hand the buffer back to the thread/main program


#############################################################################################################################




