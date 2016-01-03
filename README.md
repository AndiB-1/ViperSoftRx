# ViperSoftRx
Capture a serial stream on any digital pin of MCUs running VIPER 

This software creates a serial code receiver on any digital pin of an MCU running VIPER python.
It was developed and tested on a viperized Photon board (Particle Photon).

To use it, import the library and call SoftRx.Rx_1byte_ICU(_rxpin,_baudrate), where _rxpin should be something like D3.ICU and _baudrate is an integer.
The example in main.py continuously polls serial data and prints it 
