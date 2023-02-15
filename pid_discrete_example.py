import time
import random

sample_time = 0.01

temp = 0 # temp variable for store error
u_1 = 0 # temp variable for store previous output

kp = 6
ki = 0
kd = 0

input_1 = 0 # current error
input_2 = 0 # n-1 error
input_3 = 0 # n-2 error

setPoint = 100

alpha = (2*sample_time*kp)+((ki**2)*sample_time)+2*kd 
beta = ((sample_time**2)*ki)-(4*kd)-(2*sample_time*kp)
gama = 2*kd
delta = 2*sample_time

i=0

signalArr = []
errorArr = []
outputArr = []

while(i<101):

    signal = random.randrange(0,100) # genarate random sensor data
    time.sleep(sample_time)

    signalArr.append(signal)
    errorArr.append(setPoint-signal)

    input_1 = setPoint-signal # store current sensor data to current error var
    
    out = ((alpha*input_1)+(beta*input_2)+(gama*input_3)+(delta*u_1))/delta #caculate output
    
    input_2 = input_1 # store current sensor data to n-1 error var
    input_3 = temp # n-2 error var will store a temp var 
    temp = input_2 # store n-1 error variable to temp var
    
    u_1 = out # current output will store to previous output variable

    i+=1

    # code below is map output between 0 and 255 for arduino pwm
    if(out>=255):
        out=255
    elif(out<=0):
        out=0

    outputArr.append(out)


print("error: ",errorArr)
print("\n")
print("signal: ",signalArr)
print("\n")
print("Output: ",outputArr)