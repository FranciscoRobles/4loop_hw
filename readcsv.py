import re
from firebase import firebase

firebase=firebase.FirebaseApplication('https://letsparkiot.firebaseIO.com',None)

counter=0
i=0
letter=None
slot=None

good_letters="FGHIJ"

with open("OcupacionEstacionamientoIndividual.csv","r") as f:
	for row in f:
		separated_lines=row.split(",")
		for s in separated_lines:
			s=re.sub("[\r\n]","",s)
			if i==0:
				letter=s
				i+=1
			elif i==1:
				slot=s
				i+=1
			elif i==2:
				if letter in good_letters:
					line="/ITESM/General/"+letter+"/Slots/"+slot
					firebase.post(line,int(s))
				i=0