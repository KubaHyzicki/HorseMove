import logging
import pygame

from src.square import Square

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
        for id_y, y in enumerate(range(0, self.height, self.sizeY)):
            line = []
            for id_x, x in enumerate(range(0, self.width, self.sizeX)):
                square = Square(self.screen, id_x, id_y, x, y, self.sizeX, self.sizeY, self.colour__default)
                line.append(square)
                square.update()
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

    def markAvailables(self, availableMoves):
        if len(availableMoves) == 0:
            return
        for availableMove in availableMoves:
            square = self.squares[availableMove[1]][availableMove[0]]
            square.changeColour(self.colour__possible_moves)
            square.update()
        pygame.display.update()

    def unmarkAvailables(self, availableMoves):
        if len(availableMoves) == 0:
            return
        for availableMove in availableMoves:
            square = self.squares[availableMove[1]][availableMove[0]]
            square.changeColour(self.colour__default)
            square.update()