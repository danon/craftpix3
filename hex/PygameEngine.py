from typing import Iterable

import pygame
from pygame import Surface
from pygame.event import Event

from hex.core.Color import Color

class PygameEngine:
    def __init__(self, test_mode: bool):
        self.__test_mode = test_mode
        pygame.init()
        if test_mode:
            self.screen = Surface((640, 480))
        else:
            self.screen = pygame.display.set_mode((640, 480))

    def flip(self):
        if not self.__test_mode:
            pygame.display.flip()

    def pixel_color(self, x: int, y: int) -> Color:
        color = self.screen.get_at((x, y))
        return Color(color.r, color.g, color.b)

    def click(self):
        pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))

    def close(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    def poll_events(self) -> Iterable[Event]:
        return pygame.event.get()

    def capture(self, filename: str):
        pygame.image.save(self.screen, filename)

    def stop(self):
        pygame.quit()
