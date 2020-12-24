import logging
import random
import time
import pygame

from src.draw import Draw

# logging.basicConfig(level=logging.DEBUG)

class HorseMove():
    title = 'Ruche(a)m Konia'
    x = 5
    y = 7
    res = (720,720)

    def __init__(self):
        logging.debug("Setuping pygame module")
        pygame.init()
        self.screen = pygame.display.set_mode(self.res)
        self.screen.fill((153,255,51))
        self.draw = Draw(self.screen)
        self.squares = self.draw.generateBoard()
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

    def makeMove(self, square):
        raise NotImplementedError
