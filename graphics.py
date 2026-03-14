#not important dont prioritize

from OpenGL.GL import *
from OpenGL.GLUT import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(0.5,0)
    glEnd()

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Test")

glutDisplayFunc(draw)
glutMainLoop()