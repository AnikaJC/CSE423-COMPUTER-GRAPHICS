from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math 

def convert_to_zone0(x, y, zone):
    if zone == '1':
        return (y, x)
    elif zone == '2':
        return (y, -x)
    elif zone == '3':
        return (-x, y)
    elif zone == '4':
        return (-x, -y)
    elif zone == '5':
        return (-y, -x)
    elif zone == '6':
        return (-y, x)
    elif zone == '7':
        return (x, -y)
    


def convert_to_original(x, y, Nzone):
    if Nzone == '1':
        return (y, x)
    elif Nzone == '2':
        return (-y, x)
    elif Nzone == '3':
        return (-x, y)
    elif Nzone == '4':
        return (-x, -y)
    elif Nzone == '5':
        return (-y, -x)
    elif Nzone == '6':
        return (y, -x)
    elif Nzone == '7':
        return (x, -y)

def mid_point_circle(r):
    x = 0
    y = r
    d_init = 1 - r
    d = d_init
    pixel = []
    while x < y:
        pixel.append((x, y))
        if d >= 0:
            d += (2 * x) - (2 * y) + 5
            x += 1
            y -= 1
        else:
            d += (2 * x) + 3
            x += 1
    return pixel
    

def draw_circle(x, y, r):
    glPointSize(3)
    glBegin(GL_POINTS)

    zone_0 = []
    zone_1 = mid_point_circle(r)
    zone_2 = []
    zone_3 = []
    zone_4 = []
    zone_5 = []
    zone_6 = []
    zone_7 = []

    for (i, j) in zone_1:
        zone_0.append(convert_to_zone0(i, j, '1'))

    for (i, j) in zone_0:
        zone_2.append(convert_to_original(i, j, '2'))
        zone_3.append(convert_to_original(i, j, '3'))
        zone_4.append(convert_to_original(i, j, '4'))
        zone_5.append(convert_to_original(i, j, '5'))
        zone_6.append(convert_to_original(i, j, '6'))
        zone_7.append(convert_to_original(i, j, '7'))

    for (i, j) in zone_0:
        glVertex2f(x+i, y+j)
    for (i, j) in zone_1:
        glVertex2f(x+i, y+j)
    for (i, j) in zone_2:
        glVertex2f(x+i, y+j)
    for (i, j) in zone_3:
        glVertex2f(x+i, y+j)
    for (i, j) in zone_4:
        glVertex2f(x+i, y+j)
    for (i, j) in zone_5:
        glVertex2f(x+i, y+j)
    for (i, j) in zone_6:
        glVertex2f(x+i, y+j)
    for (i, j) in zone_7:
        glVertex2f(x+i, y+j)

    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 1.0)

    draw_circle(350, 350, 100)

    draw_circle(400, 350, 50)
    draw_circle(300, 350, 50)
    draw_circle(350, 400, 50)
    draw_circle(350, 300, 50)

    draw_circle((350 + (50/1.4142)), (350 + (50/1.4142)), 50)
    draw_circle((350 - (50/1.4142)), (350 + (50/1.4142)), 50)
    draw_circle((350 - (50/1.4142)), (350 - (50/1.4142)), 50)
    draw_circle((350 + (50/1.4142)), (350 - (50/1.4142)), 50)


    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Midpoint Circle")
glutDisplayFunc(showScreen)

glutMainLoop()