from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def midPoint(x1, y1, x2, y2):
    dy=abs(y2-y1)
    dx=abs(x2-x1)
    flag = dy > dx
    if flag:
        x1,y1=y1,x1
        x2,y2=y2,x2

    if x1 > x2:
        x1,x2=x2,x1
        y1,y2=y2,y1
    dx = x2 - x1
    dy=abs(y2-y1)
    e = dx / 2
    y = y1
    step= 1 if y1<y2 else -1
    if y1 < y2:
        step = 1
    else:
        step = -1

    glBegin(GL_POINTS)
    for x in range(x1, x2+1):
        if flag:
            glVertex2f(y, x)
        else:
            glVertex2f(x, y)
        e -= dy
        if e < 0:
            y += step
            e += dx
    glEnd()



def showScreen():
    glColor3f(1, 0, 1)
    glPointSize(10)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #call the draw methods here
    init()
    #one
    midPoint(180, 180, 300, 180)
    midPoint(240, 180, 240, 340)
    midPoint(240, 340, 200, 300)
    #six
    
    midPoint(400, 340, 500, 340) # 
    midPoint(400, 180, 400, 340) # |
    midPoint(400, 180, 500, 180) # _ 3
    midPoint(500, 180, 500, 260) # '
    midPoint(400, 260, 500, 260) # _ 2 



    glutSwapBuffers()

# put your drawing codes inside this 'draw' function


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("Anika Jahan Choudhury- 16")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
