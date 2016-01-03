
#########
# example for SoftRx on Viper
#########

### import libraries
import SoftRx
# import the streams module for USB serial port.
import streams

# open the default serial port
streams.serial()

####################################
### define functions

# example code for continuous serial capture
def ReceiveData(_rxpin,_baudrate):
    global RxBuffer
    RxBuffer = []

    while True:
        RxBufferTMP = SoftRx.Rx_1byte_ICU(_rxpin,_baudrate) # now we're receiving decimal serial data
        RxBuffer.append(RxBufferTMP)

# print the RxBuffer in a separate thread
def PrintData():
    global RxBuffer
    sleep(4000)
    
    while True:        
        sleep(2000) # give the buffer time to fill
        
        if len(RxBuffer)>9:
            print(RxBuffer)
            RxBuffer = []
            
#################################
# test it all
sleep(4000)
print("starting")
sleep(500)

thread(ReceiveData,D4.ICU,400) #start listening on the SoftSerial port

thread(PrintData)




