import time
import pypupm_grove as grove

button=grove.GroveButton(2)

counter=0

while True:
	if(button.value()==1):
		counter+=1
		print counter
