from random import Random
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def drawBoldPoint(x1,y1,x2,y2):
    glBegin(GL_POINTS)
    while y1<=y2:
        glVertex2f(x1,y1)
        y1+=1
    glEnd()

def drawDashedPoint(x1,y1,x2,y2):
    glBegin(GL_POINTS)
    while x1<=x2:
        glVertex2f(x1,y1)
        x1+=1
        if x1%10==0:
            x1+=5
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    #draw_points(0, 500)
    drawBoldPoint(200,100,200,350)
    drawDashedPoint(100,350,300,350)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Dashed_Lines") #window name
glutDisplayFunc(showScreen)

glutMainLoop()