
"""This file is part of Asphalt
  Asphalt is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
 Asphalt is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with Asphalt.  If not, see <http://www.gnu.org/licenses/>.

Copyright © 2016 4Loop """





import re
from firebase import firebase

firebase=firebase.FirebaseApplication('https://letsparkiot.firebaseIO.com',None)

counter=0
i=0
letter=None
slot=None

#good_letters="FGHIJ"

capacities={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0}

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
				#if letter in good_letters:
				line="/Parking/ITESM/General/"+letter+"/Slots/"
				firebase.put(line,slot,int(s))
				if s == "0":
					capacities[letter]+=1
				i=0

zones="ABCDEFGHIJ"
for s in zones:
	firebase.put("/ITESM/General/"+s+"/","Capacity",capacities[s])
