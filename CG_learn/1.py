from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

g = 9.8
t = 0
dt = 0.0001
class obj:
	def __init__(self, h=10, v=0):
		self.h = h
		self.v = v

world = [obj(h=60), obj(v=-12)]
needdraw = obj()

def init():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	gluOrtho2D(-20.0, 20.0, 0.0, 40.0)

def drawFunc():
	global needdraw
	
	glClear(GL_COLOR_BUFFER_BIT)

	glBegin(GL_POINTS)
	glVertex2f(0.0, needdraw.h)
	glVertex2f(0.0, 0.0)
	glEnd()

	glFlush()

def idleFunc():
	global world, g, t, dt, needdraw

	for obj in world:
		if obj.h > 0:
			obj.h = obj.h - obj.v*dt
			obj.v = obj.v + g*dt
			needdraw = obj
			drawFunc()
	t = t + dt

glutInit()
glutInitDisplayMode(GLUT_RGBA|GLUT_SINGLE)
glutInitWindowSize(400, 400)
glutCreateWindow(b"Sencond")

glutDisplayFunc(drawFunc)
glutIdleFunc(idleFunc)
init()
glutMainLoop()