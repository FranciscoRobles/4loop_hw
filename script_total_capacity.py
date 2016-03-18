from firebase import firebase

counter=0

zones="ABCDEFGHIJ"

firebase=firebase.FirebaseApplication('https://letsparkiot.firebaseIO.com',None)

for s in zones:
	res_json=firebase.get("/ITESM/General/"+s+"/Capacity",None)
	for key in res_json:
		counter+=res_json[key]
firebase.put("/ITESM/General","TotalCapacity",counter)