from ursina import *

from random import randint

app = Ursina()


import testIMPsrc
import testExpl
import testPlayer
import testRocket



EditorCamera(rotation=(90,0,0),position=(0,-5,0), move_speed = 0, zoom_speed=0, pan_speed = Vec2(0, 0), rotation_speed = 0)
#EditorCamera()


def update():
	testIMPsrc.moveBg1(-0.01)
	testIMPsrc.moveBg2(-0.003)
	testExpl.animExpl()
	testPlayer.animVert()
	testRocket.animeRocket()
	
	testPlayer.vert.z += held_keys['w'] * .01
	testPlayer.vert.z -= held_keys['s'] * .01
	
	checkCollision()


def checkCollision():
	if testRocket.eRocket.intersects(testPlayer.vert).hit:
		testExpl.idx=0
		testExpl.expl.x=testRocket.eRocket.x
		testExpl.expl.z=testRocket.eRocket.z
		
		testRocket.eRocket.x=randint(6, 10)
		testRocket.eRocket.z=randint(-2, 2)
	


app.run()
