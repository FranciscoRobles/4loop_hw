from firebase import firebase

firebase=firebase.FirebaseApplication('https://4loop.firebaseIO.com',None)
newcar='chevy'
result=firebase.push('/carros',newcar, {'placas':'123'})
print 'yay'
