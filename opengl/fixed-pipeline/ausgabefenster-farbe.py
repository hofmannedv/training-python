# Python OpenGL examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# display the skeleton of a moving cube
# based on the tutorial from Harrison at Pythonprogramming.net
# https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/

# hide PyGame welcome message
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# import required Python libraries -- pygame, and OpenGL
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def point(x, y, z, colour="white"):
    glPointSize(10)
    setColour(colour)
    glBegin(GL_POINTS)
    glVertex3d(x, y, z)
    glEnd()
    return

def line(point1, point2, colour="white"):
    setColour(colour)
    glBegin(GL_LINES)
    glVertex3fv(point1)
    glVertex3fv(point2)
    glEnd()
    return

def triangle(point1, point2, point3, colour="white"):
    setColour(colour)
    glBegin(GL_TRIANGLES)
    glVertex3fv(point1)
    glVertex3fv(point2)
    glVertex3fv(point3)
    glEnd()
    return

def square(point1, point2, point3, point4, colour="white"):
    setColour(colour)
    glBegin(GL_QUADS)
    glVertex3fv(point1)
    glVertex3fv(point2)
    glVertex3fv(point3)
    glVertex3fv(point4)
    glEnd()
    return

def polygon(pointList, colour="white"):
    setColour(colour)
    glBegin(GL_POLYGON)
    for p in pointList:
        glVertex3fv(p)
    glEnd()
    return

def setColour(colour="white"):
    colourList = {
            "red"    : (1, 0, 0),
            "blue"   : (0, 0, 1),
            "green"  : (0, 1, 0),
            "yellow" : (1, 1, 0),
            "white"  : (1, 1, 1)

    }

    # set default colour to white
    colourRGBValue = colourList["white"]
    if colour in colourList.keys():
        colourRGBValue = colourList[colour]

    # enable colour
    r, g, b = colourRGBValue
    glColor3f(r, g, b)
    return

def main():
    # init PyGame
    pygame.init()

    # set output resolution
    display = (800, 600)

    # set display mode
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # perspective
    # - field of view
    # - aspect ratio
    # - znear and zfar
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # step out 5 units
    glTranslatef(0.0, 0.0, -5)

    # event loop
    while True:
        # check for keys being pressed: close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # [x] button
                print ("Beendet mit [x]-Knopf")
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                # ESC key
                if event.key == K_ESCAPE:
                    print ("Beendet mit ESC-Taste")
                    pygame.quit()
                    quit()

                # arrow left key
                if event.key == K_LEFT:
                    print ("Pfeiltaste nach links")

                # arrow right key
                if event.key == K_RIGHT:
                    print ("Pfeiltaste nach rechts")

                # arrow up key
                if event.key == K_UP:
                    print ("Pfeiltaste nach unten")

                # arrow down key
                if event.key == K_DOWN:
                    print ("Pfeiltaste nach unten")

        # clear output/screen
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # display point in red colour
        point(0, 0, 0, "white")

        # display line in blue colour
        p1 = (1, -1, 0)
        p2 = (1, 1, 0)
        line(p1, p2, "blue")

        # display triangle in green colour
        p1 = (-0.75, 1, 0)
        p2 = (0.75, 1, 0)
        p3 = (0, 1.5, 0)
        triangle(p1, p2, p3, "green")

        # display square in yellow colour
        p1 = (1.5, 0, 0)
        p2 = (1.5, 1, 0)
        p3 = (2.5, 1, 0)
        p4 = (2.5, 0, 0)
        square(p1, p2, p3, p4, "yellow")

        # display polygon in white colour
        p1 = (-0.5, 0.5, 0)
        p2 = (0.5, 0.5, 0)
        p3 = (1.0, 0.0, 0)
        p4 = (0.5, -0.5, 0)
        p5 = (-0.5, -0.5, 0)
        p6 = (-1.0, 0.0, 0)
        polygon([p1, p2, p3, p4, p5, p6], "red")

        pygame.display.flip()

        # wait for 10 ms
        pygame.time.wait(10)

main()
