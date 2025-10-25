import pygame

from hex.core.port import ForControlling
from hex.PygameEngine import PygameEngine

class PygameController:
    def __init__(self, engine: PygameEngine, controls: ForControlling):
        self.__engine = engine
        self.__controls = controls

    def send_controls(self):
        for event in self.__engine.poll_events():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__controls.click()
            if event.type == pygame.QUIT:
                self.__controls.close()
