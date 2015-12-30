
#########
# this section is only to test the SoftRx_ICU code
#########

import SoftRx

def threadFct2():
    
    while True:
        #testing
        sleep(10) # give the buffer time to fill

        if len(RxBuffer)>9:
            print(RxBuffer)
            RxBuffer = []

sleep(1000)
print("starting")
sleep(500)
thread(SoftRx.SoftRx_startICU,D4.ICU,400) #start listening on the SoftSerial port

thread(threadFct2)
