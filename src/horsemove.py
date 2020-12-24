import logging
import random
import time
import pygame

from src.draw import Draw

class HorseMove():
    title = 'Ruche(a)m Konia'
    x = 5
    y = 7
    res = (720,720)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.res)
        self.screen.fill((153,255,51))
        self.draw = Draw(self.screen)
        self.buttons = self.draw.generateBoard()
        self.run()

    def run(self):
        while True:
            try:
                for ev in pygame.event.get():
                    print('asd')
                    print(ev.type)
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        button = self.mapButton(pygame.mouse.get_pos())
                        self.makeMove(button)
            except KeyboardInterrupt:
                logging.info("Exiting")
                pygame.quit()

    def getButton(self, mouse):
        raise NotImplementedError
        x = mouse[0]
        y = mouse[1]
        for line in self.buttons:
            

    def makeMove(self, button):
        raise NotImplementedError
