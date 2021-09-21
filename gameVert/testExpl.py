from ursina import *

from random import randint

fDir='data/e1.png'
expl=Sprite(fDir, filtering=False)


def explIni():
	expl.texture=fDir
	expl.rotation_x=90


s=[]
s.append('data/e1.png')
s.append('data/e3.png')
s.append('data/e5.png')
s.append('data/e8.png')
s.append('data/e13.png')
s.append('data/e18.png')
s.append('data/e22.png')
'''
for i in range(8):
	s.append('a3/a'+str(i+1))
'''



''' ///////////////////////////////////////////////// '''

explIni()

expl.x=randint(-5, 5)
expl.z=randint(-2, 2)


dly=10
idx=0

def animExpl():
	global idx
	global dly
	if dly<0:
		#s[idx].rotation_x=0
		idx=idx+1
		if (idx>6):
			idx=0
			expl.x=randint(-5, 5)
			expl.z=randint(-2, 2)
		dly=5
	expl.texture=s[idx]
	dly=dly-1
