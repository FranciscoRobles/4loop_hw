import time
import pyupm_grove as grove

button=grove.GroveButton(2)

counter=0

while True:
	if(button.value()==1):
		counter+=1
		print counter
		time.sleep(0.5)
