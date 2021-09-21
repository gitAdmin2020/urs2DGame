from ursina import *

from random import randint

fDir='data/rr2.png'
eRocket=Sprite(fDir, filtering=False, collider='box')

rocketX=6

eRocket.x=5


def eRocketIni():
	eRocket.texture=fDir
	eRocket.rotation_x=90
	#vert.scale_x=4
	#vert.scale_y=2
	#vert.y=5


s=[]
s.append('data/rr2.png')
s.append('data/rr3.png')
s.append('data/rr4.png')


eRocketIni()


dly=10
idx=0

def animeRocket():
	global idx
	global dly
	if dly<0:
		#s[idx].rotation_x=0
		idx=idx+1
		if (idx>2):
			idx=0
			#vert.x=randint(-5, 5)
			#vert.z=randint(-2, 2)
		dly=5
	eRocket.texture=s[idx]
	eRocket.x=eRocket.x-0.05
	

		
	if (eRocket.x<-6):
		eRocket.x=randint(6, 10)
		eRocket.z=randint(-2, 2)
	#rocketX=rocketX+0.01
	dly=dly-1
