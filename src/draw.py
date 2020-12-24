import logging
import pygame
import os
from time import sleep

class Square():
    square_image_path = "resources/square.jpg"
    horse_image_path = "resources/horse.jpg"
    def __init__(self, sizeX, sizeY, init_colour, idx, idy):
        self.idx = idx
        self.idy = idy
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.surface = pygame.Surface((sizeX, sizeY))
        self.changeColour(init_colour)
        # self.drawBorder()
        # Graphic square - alternative for manual border drawing
        self.loadSquareImage()

    def changeColour(self, colour):
        self.colour = colour
        self.surface.fill(colour)

    def drawBorder(self):
        pygame.draw.rect(self.surface, (0,0,0), (0,0,self.sizeX,self.sizeY), 3)

    def loadImage(self, imagePath):
        image = pygame.image.load(os.path.abspath(imagePath))
        image = pygame.transform.scale(image, (self.sizeX, self.sizeY))
        charImage = image.convert(image)
        charRect = pygame.Rect((0,0),(self.sizeX, self.sizeY))
        self.surface.blit(charImage, charRect)

    def loadSquareImage(self):
        self.loadImage(self.square_image_path)

    def drawHorse(self):
        self.loadImage(self.horse_image_path)


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
        logging.info("Generating board")
        self.squares = []
        for idy, y in enumerate(range(0, self.height, self.sizeY)):
            line = []
            for idx, x in enumerate(range(0, self.width, self.sizeX)):
                square = Square(self.sizeX, self.sizeY, self.colour__default, idx, idy)
                line.append(square)
                self.screen.blit(square.surface, (x, y))
            self.squares.append(line)
        pygame.display.update()
        logging.info("Board generated")
        return self.squares

    def mapSquare(self, mousePos):
        x = mousePos[0]
        y = mousePos[1]
        min = 0
        max = 0
        logging.info("Mapping mouse pos ({},{}) to square".format(x,y))
        for Y in range(self.Y):
            max += self.sizeY
            if y < max and y > min:
                logging.debug("Mapped Y={}".format(Y))
                min = 0
                max = 0
                for X in range(self.X):
                    max += self.sizeX
                    if x < max and x > min:
                        logging.debug("Mapped X={}".format(X))
                        logging.info("Returning square ({},{})".format(X,Y))
                        return self.squares[Y][X]
                    min += self.sizeX
            min += self.sizeY
        logging.warning("Mouse pos ({},{}) could not be mapped to any square!".format(x,y))
        return False
