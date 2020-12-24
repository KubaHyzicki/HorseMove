import os
import pygame

class Square():
    colour__empty = (0,0,0,0)
    square_image_path = "resources/square.jpg"
    horse_image_path = "resources/horse.jpg"

    def __init__(self, screen, x, y, sizeX, sizeY, init_colour):
        self.screen = screen
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.colour = init_colour
        self.surface = pygame.Surface((sizeX, sizeY))
        self.redraw()

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
        pygame.display.update()

    def loadSquareImage(self):
        self.loadImage(self.square_image_path)

    def drawHorse(self):
        self.redraw()
        self.loadImage(self.horse_image_path)
        self.update()

    def redraw(self):
        self.changeColour(self.colour)
        # Graphic square - alternative for manual border drawing
        # self.loadSquareImage()
        self.drawBorder()
        self.update()

    def update(self, reload = False):
        self.screen.blit(self.surface, (self.x, self.y))
        if reload:
            pygame.display.update()
