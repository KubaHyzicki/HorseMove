import pygame
import os
from time import sleep

class Button():

    def __init__(self, sizeX, sizeY, init_colour, idx, idy):
        self.idx = idx
        self.idy = idy
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.surface = pygame.Surface((sizeX, sizeY))
        self.changeColour(init_colour)
        self.drawBorder()
        # #graphic square - alternative for manual border drawing
        # self.loadSquare()

    def changeColour(self, colour):
        self.colour = colour
        self.surface.fill(colour)

    def drawBorder(self):
        pygame.draw.rect(self.surface, (0,0,0), (0,0,self.sizeX,self.sizeY), 3)

    def loadSquare(self):
        image = pygame.image.load(os.path.abspath("resources/square.jpg"))
        image = pygame.transform.scale(image, (self.sizeX, self.sizeY))
        charImage = image.convert(image)
        charRect = pygame.Rect((0,0),(self.sizeX, self.sizeY))
        self.surface.blit(charImage, charRect)

class Draw():
    colour__possible_moves = (255,255,102)
    colour__current = (51,255,255)
    colour__already_used = (160,160,160)
    colour__default = (255,255,255)
    colour__blocks = (64,64,64)
    colour__goal_area = (153,255,51)
    colour__background = (204,229,255)
    X = 5
    Y = 7
    def __init__(self, screen, X = None, Y = None):
        self.screen = screen
        self.screen.fill(self.colour__background)
        if X:
            self.X = X
        if Y:
            self.Y = Y
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.sizeX = int(self.width / self.X)
        self.sizeY = int(self.height / self.Y)


    def generateBoard(self):
        self.buttons = []
        for idy, y in enumerate(range(0, self.height, self.sizeY)):
            line = []
            for idx, x in enumerate(range(0, self.width, self.sizeX)):
                button = Button(self.sizeX, self.sizeY, self.colour__default, idx, idy)
                line.append(button)
                self.screen.blit(button.surface, (x, y))
        self.buttons.append(line)
        pygame.display.update()
        return self.buttons
