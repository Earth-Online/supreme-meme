from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINE_SMOOTH)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    glEnd()

    glBegin(GL_LINE_STRIP)
    for x in (i * 0.01 for i in range(-50, 50)):
        glVertex2f(x, x*x)
    glEnd()
    
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_RGBA|GLUT_SINGLE)
glutInitWindowSize(400, 400)
glutCreateWindow(b"Sencond")

glutDisplayFunc(drawFunc)
init()
glutMainLoop()