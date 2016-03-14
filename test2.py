import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd
from firebase import firebase

firebase=firebase.FirebaseApplication('https://4loop.firebaseIO.com',None)

button=grove.GroveButton(2)

counter=40

myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

myLcd.setCursor(0,0)

myLcd.write(counter)

while True:
	if(button.value()==1):
		counter-=1
		firebase.put('/Counter',"count", counter) 
		print counter
		time.sleep(0.5)

print 'yay'