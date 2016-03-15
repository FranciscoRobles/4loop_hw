import dweepy
import time

dweepy.dweet_for('Edison_1',{'ZonaA':20})

time.sleep(1)

dweepy.dweet_for('Edison_1',{'ZonaB':20})

res=dweepy.get_dweets_for('Edison_1')

for x in res:
	print x
