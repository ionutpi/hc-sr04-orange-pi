from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
import time




#initialize the gpio module
gpio.init()

#setup the port (same as raspberry pi's gpio.setup() function)
gpio.setcfg(port.PC4, gpio.OUTPUT)
gpio.setcfg(port.PC7, gpio.INPUT)

gpio.output(port.PC4, gpio.LOW)
sleep(0.5)

while True:
    gpio.output(port.PC4, gpio.HIGH)
    sleep(0.3)
    gpio.output(port.PC4, gpio.LOW)
    #state=gpio.input(port.PC7)
    while (gpio.input(port.PC7) == 0):
        pass
    start = time.time()
    while (gpio.input(port.PC7) == 1):
        pass
    end = time.time()

    print((end - start)/58.0*1000000)
    sleep(1)
#print state
