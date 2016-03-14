from firebase import firebase
firebase=firebase.FirebaseApplication('https://4loop.firebaseIO.com',None)
data = raw_input("Input Data: ")
firebase.put('/Carro',"data", data) 

print 'yay'
