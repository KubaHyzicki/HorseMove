import logging
import random
import time
import pygame

from src.draw import Draw

class HorseMove():
    title = 'Ruche(a)m Konia'
    X = 5
    Y = 7
    res = (720,720)

    def __init__(self):
        logging.debug("Setuping pygame module")
        pygame.init()
        self.screen = pygame.display.set_mode(self.res)
        self.screen.fill((153,255,51))
        pygame.display.set_caption(self.title)
        self.draw = Draw(self.screen)
        self.squares = self.draw.generateBoard()
        self.currentSquare = None
        self.moveHorse(self.startSquare)
        self.availableMoves = self.getAvailableMoves()
        self.draw.markAvailables(self.availableMoves)
        self.run()

    def run(self):
        logging.info("Listening")
        while True:
            try:
                for ev in pygame.event.get():
                    # Commented out as this generates too much output
                    # logging.debug("Event: {}".format(ev.type))
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                        logging.debug("Detected QUIT event, exiting...")
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        square = self.draw.mapSquare(pygame.mouse.get_pos())
                        self.makeMove(square)
            except KeyboardInterrupt:
                logging.info("Interrupted, exiting...")
                pygame.quit()
                break

    @property
    def startSquare(self):
        if self.X % 2 == 0 or self.Y % 2 == 0:
            logging.error("Board size should have odd parameters!")
            exit(1)
        if not self.squares:
            logging.error("Squares are not yet defined!")
            exit(1)
        return self.squares[int((self.Y - 1) / 2)][int((self.X - 1) / 2)]

    def moveHorse(self, targetSquare, currentSquare = None):
        if currentSquare:
            currentSquare.changeColour(self.draw.colour__already_used)
            currentSquare.redraw()
        targetSquare.changeColour(self.draw.colour__current)
        targetSquare.drawHorse()
        self.currentSquare = targetSquare

    def makeMove(self, square):
        for move in self.availableMoves:
            if square.id_x == move[0] and square.id_y == move[1]:
                break
        else:
            logging.warning("Move ({},{}) not available!".format(square.id_x, square.id_y))
            return False
        self.draw.unmarkAvailables(self.availableMoves)
        self.moveHorse(square, self.currentSquare)
        self.availableMoves = self.getAvailableMoves()
        self.draw.markAvailables(self.availableMoves)


    def getAvailableMoves(self):
        availableMoves = []
        combinations = [[1,2],[-1,2],[-1,-2],[1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]
        X = self.currentSquare.id_x
        Y = self.currentSquare.id_y
        for combinationin in combinations:
            x = X + combinationin[0]
            y = Y + combinationin[1]
            if x < 0 or y < 0 or x >= self.X or y >= self.Y:
                continue
            if self.squares[y][x].used:
                continue
            availableMoves.append([x,y])
            # logging.debug("Adding available move ({},{})".format(x,y))
        logging.info("Available moves: {}".format(availableMoves))
        return availableMoves
