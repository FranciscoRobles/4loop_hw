import time
import pyupm_grove as grove
from firebase import firebase
firebase=firebase.FirebaseApplication('https://4loop.firebaseIO.com',None)

button=grove.GroveButton(2)

counter=40

while True:
	if(button.value()==1):
		counter-=1
		firebase.put('/Counter',"count", counter) 
		print counter
		time.sleep(0.5)

print 'yay'