import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd
from firebase import firebase
import mraa

firebase=firebase.FirebaseApplication('https://letsparkiot.firebaseIO.com',None)

button1=grove.GroveButton(2)
button2=grove.GroveButton(6)


id_zone="A"

#counter=int(firebase.get("/ITESM/General/"+id_zone+"/Capacity",None))

res_json=firebase.get("/Parking/ITESM/General/"+id_zone+"/Capacity",None)

counter=[0,0]

for x in res_json:
	counter[0]=int(res_json[x])
	counter[1]=int(res_json)



#firebase.put('/ITESM/General/'+id_zone,"Capacity",counter)

myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

myLcd.setCursor(0,0)

myLcd.write("Available : "+str(counter))


led_disp=mraa.Gpio(7)
led_disp.dir(mraa.DIR_OUT)

led_not_disp=mraa.Gpio(3)
led_not_disp.dir(mraa.DIR_OUT)

while True:
	if(counter[0]>0):
		led_disp.write(1)
		led_not_disp.write(0)
	else:
		led_disp.write(0)
		led_not_disp.write(1)
	if(button1.value()==1):
		if(counter[0]>0):
			counter[0]-=1
			myLcd.clear()
			myLcd.write("Available : "+str(counter))
			firebase.put('/Parking/ITESM/General/'+id_zone+"/Capacity","Capacity",counter)
			print counter[0]
			time.sleep(0.1)
	elif(button2.value()==1):
		if(counter[0]<counter[1]):
			counter[0]+=1
			myLcd.clear()
			myLcd.write("Available : "+str(counter))
			firebase.put('/Parking/ITESM/General/'+id_zone+"/Capacity", "Capacity",counter)
			print counter[0]
			time.sleep(0.1)
		else:
			print "nel"
			time.sleep(0.1)