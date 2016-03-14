import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd
from firebase import firebase

firebase=firebase.FirebaseApplication('https://4loop.firebaseIO.com',None)

button1=grove.GroveButton(2)
button2=grove.GroveButton(6)


counter=40

id_edison=1

firebase.put('/Counter'+str(id_edison),"count",counter)

myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

myLcd.setCursor(0,0)

myLcd.write(str(counter))

while True:
	if(button1.value()==1):
		counter-=1
		myLcd.clear()
		myLcd.write(str(counter))
		firebase.put('/Counter'+str(id_edison),"count", counter) 
		print counter
		time.sleep(0.1)
	elif(button2.value()==1):
		counter+=1
		myLcd.clear()
		myLcd.write(str(counter))
		firebase.put('/Counter'+str(id_edison),"count",counter)
		print counter
		time.sleep(0.1)
