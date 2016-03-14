import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd
from firebase import firebase

firebase=firebase.FirebaseApplication('https://letsparkiot.firebaseIO.com',None)

button1=grove.GroveButton(2)
button2=grove.GroveButton(6)


counter=20

id_zone="A"

firebase.put('/Zona'+" "+id_zone,"Capacidad",counter)

myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

myLcd.setCursor(0,0)

myLcd.write(str(counter))

while True:
	if(button1.value()==1):
		if(counter>0):
			counter-=1
			myLcd.clear()
			myLcd.write(str(counter))
			firebase.put('/Zona'+" "+id_zone,"Capacidad",counter)
			print counter
			time.sleep(0.1)
	elif(button2.value()==1):
		if(counter<20):
			counter+=1
			myLcd.clear()
			myLcd.write(str(counter))
			firebase.put('/Zona'+" "+id_zone,"Capacidad",counter)
			print counter
			time.sleep(0.1)