# 4loop_hw
+Synopsis
+
+This is the repository for the hardware of Asphalt, an application of the Team Four Loop during the Vertical Workshop 2016 ITESM & Intel. The hardware was implemented using Python Language. 
+
+Motivation
+
+We were asked to create a solution anf to optimize a private parking lot. We could choose from the lot at Intel Guadalajara or the ITESM Campus Guadalajara. 
+
+Installation
+
+while True:
+	if(counter[0]>0):
+		led_disp.write(1)
+		led_not_disp.write(0)
+	else:
+		led_disp.write(0)
+		led_not_disp.write(1)
+	if(button1.value()==1):
+		if(counter[0]>0):
+			counter[0]-=1
+			myLcd.clear()
+			myLcd.write("Available : "+str(counter[0]))
+			firebase.put('/Parking/ITESM/General/'+id_zone+"/","Capacity",counter[0])
+			print counter[0]
+			time.sleep(0.1)
+	elif(button2.value()==1):
+		if(counter[0]<counter[1] or counter[1]==0):
+			counter[0]+=1
+			myLcd.clear()
+			myLcd.write("Available : "+str(counter[0]))
+			firebase.put('/Parking/ITESM/General/'+id_zone+"/","Capacity",counter[0])
+			print counter[0]
+			time.sleep(0.1)
+	here we can observe a part of the code for the sensors.
+	
+API Reference
+
+there are not API references for the Hardware of the app.
+
+Tests
+
+The project was tested several times using texts as input values.
+
+Contributors
+
+Toatzin Padilla
+Diego Yáñez
+Ney González
+Alejandro Carrillo
+Alma González
+José Robles
+Hugo Michel
+Gerardo Velasco
+Vladimir Rodríguez
+Carlos Martell
+Dafne Medina
+
+License
+
+This file is part of Asphalt
+  Asphalt is free software: you can redistribute it and/or modify
+    it under the terms of the GNU General Public License as published by
+    the Free Software Foundation, either version 3 of the License, or
+    (at your option) any later version.
+ Asphalt is distributed in the hope that it will be useful,
+    but WITHOUT ANY WARRANTY; without even the implied warranty of
+    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
+    GNU General Public License for more details.
+    You should have received a copy of the GNU General Public License
+    along with Asphalt.  If not, see <http://www.gnu.org/licenses/>.
+
+Copyright © 2016 4Loop