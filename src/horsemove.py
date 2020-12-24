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
        self.moveHorse(self.startSquare)
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
        # if currentSquare:
        #     currentSquare.
        targetSquare.drawHorse()
        self.screen.blit(targetSquare.surface, (targetSquare.idx * self.draw.sizeX, targetSquare.idy * self.draw.sizeY))
        pygame.display.update()

    def makeMove(self, square):
        raise NotImplementedError
