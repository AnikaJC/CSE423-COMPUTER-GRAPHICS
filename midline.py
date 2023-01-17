from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



def init():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def midpoint_line(x1, y1, x2, y2):
    glBegin(GL_POINTS)
    dy = y2-y1
    dx = x2-x1
    if (dy<=dx):
        d = dy-(dx/2)
        x = x1
        y = y1
        glVertex2f(x, y)
        while (x<x2):
            x = x+1
            if (d<0):
                d = d+dy
            else:
                d = d+dy-dx
                y = y+1
            glVertex2f(x,y)
    elif (dx<=dy):
        d = dx-(dy/2)
        x = x1
        y = y1
        glVertex2f(x, y)
        while (y<y2):
            y = y+1
            if (d<0):
                d = d+dx
            else:
                d = d+dx-dy
                x = x+1
            glVertex2f(x, y)
    glEnd()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    init()
    glColor3f(1, 0, 1)
    glPointSize(10)
    # call the draw methods here
    #one
    midpoint_line(150, 100, 150, 400)

    #six

    midpoint_line(300, 100, 300, 400)
    midpoint_line(450, 100, 450, 250)
    midpoint_line(300, 250, 450, 250)
    midpoint_line(300, 400, 450, 400)
    midpoint_line(300, 100, 450, 100)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow('Anika Jahan Choudhury_16')
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
