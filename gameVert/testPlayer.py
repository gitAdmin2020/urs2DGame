from ursina import *

from random import randint

fDir='data/v5_1.png'
vert=Sprite(fDir, filtering=False, collider='box')


def vertIni():
	vert.texture=fDir
	vert.rotation_x=90
	#vert.scale_x=4
	#vert.scale_y=2
	#vert.y=5


s=[]
s.append('data/v5_1.png')
s.append('data/v5_2.png')


vertIni()


dly=10
idx=0

def animVert():
	global idx
	global dly
	if dly<0:
		#s[idx].rotation_x=0
		idx=idx+1
		if (idx>1):
			idx=0
			#vert.x=randint(-5, 5)
			#vert.z=randint(-2, 2)
		dly=5
	vert.texture=s[idx]
	dly=dly-1
