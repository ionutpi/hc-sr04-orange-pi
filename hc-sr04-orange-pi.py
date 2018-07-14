from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
import time

#initialize the gpio module
gpio.init()

#setup the ports
gpio.setcfg(port.PC4, gpio.OUTPUT)
gpio.setcfg(port.PC7, gpio.INPUT)

#set trig to low
gpio.output(port.PC4, gpio.LOW)
sleep(0.5)

while True:
    #send pulse
    gpio.output(port.PC4, gpio.HIGH)
    sleep(0.3)
    gpio.output(port.PC4, gpio.LOW)

    #wait for echo to start
    while (gpio.input(port.PC7) == 0):
        pass
    start = time.time()

    #wait for echo to end
    while (gpio.input(port.PC7) == 1):
        pass
    end = time.time()
    
    #get distance in cm
    print((end - start)/58.0*1000000)
    sleep(1)

