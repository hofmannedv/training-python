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
        pygame.display.flip()

main()
