from ursina import *


pic=[]

pic.append(Entity(model='plane'))
pic.append(Entity(model='plane'))
pic.append(Entity(model='plane'))
pic.append(Entity(model='plane'))
#pic2 = Entity(model='plane')

picUrl1='data/grass.png'
picUrl2='data/trees2.png'


sky=Entity(model='plane', scale=20, color=color.blue)
sky.y=-2

sun = Entity(model='plane', texture='data/sun.png', scale=4)
sun.y=-0.2
sun.z=3


def scaledBGIni(pic1,pic2,tx,x,y,z,sx,sz,scZ):
	#global pic1
	#global picUrl1
	pic1.texture=tx
	pic1.scale=1
	pic1.scale_x=12
	pic1.x=x
	pic1.z=z
	pic1.y=y
	pic1.texture_scale=(sx,sz)
	pic1.scale_z=scZ
	
	pic2.texture=tx
	pic2.scale=1
	pic2.scale_x=12
	pic2.x=12
	pic2.y=y
	pic2.z=z
	pic2.texture_scale=(sx,sz)
	pic2.scale_z=scZ


scaledBGIni(pic1=pic[0],pic2=pic[1],tx=picUrl1,x=0,z=-2.7,y=-0.1,sx=6,sz=1,scZ=0.5)

scaledBGIni(pic1=pic[2],pic2=pic[3],tx=picUrl2,x=0,z=-2, y=-0.2,sx=2,sz=1,scZ=2)

def moveBg1(spd):
	
	pic[0].x+=spd
	pic[1].x+=spd
	if (pic[0].x<-12):
		pic[0].x=0
		pic[1].x=12

def moveBg2(spd):
	pic[2].x+=spd
	pic[3].x+=spd
	if (pic[2].x<-12):
		pic[3].x=0
		pic[4].x=12

