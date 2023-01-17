from random import Random
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    counter = 0
    while counter<50:
        a=random.randint(x,y)
        b=random.randint(x,y)
        glVertex2f(a,b) #jekhane show korbe pixel
        counter +=1
    
    glEnd()

def drawTriangle(x1,y1,x2,y2,x3,y3):
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()


def drawQuad(x1,y1,x2,y2,x3,y3,x4,y4):
    glBegin(GL_QUADS)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glVertex2f(x4,y4)
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
    glColor3f(1.0, 0.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    #draw_points(0, 500)
    drawTriangle(100,250,250,250,185,350)
    glColor3f(1.0,1.0,0.0)
    drawQuad(100,100,100,250,250,250,250,100)
    glColor3f(0.0,0.0,1.0)
    drawQuad(150,100,150,150,180,150,180,100)
    drawQuad(120,200,120,230,150,230,150,200)
    drawQuad(200,200,200,230,230,230,230,200)

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lets make our own HOMe!!") #window name
glutDisplayFunc(showScreen)

glutMainLoop()