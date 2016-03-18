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


import dweepy
import time

dweepy.dweet_for('Edison_1',{'ZonaA':20})

time.sleep(1)

dweepy.dweet_for('Edison_1',{'ZonaB':20})

res=dweepy.get_dweets_for('Edison_1')

for x in res:
	print x
