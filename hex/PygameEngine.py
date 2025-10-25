from typing import Iterable

import pygame
from pygame import Surface
from pygame.event import Event

class PygameEngine:
    def __init__(self):
        pygame.init()
        self.screen = Surface((640, 480))

    def pixel_color(self, x: int, y: int) -> tuple[int, int, int]:
        color = self.screen.get_at((x, y))
        return color.r, color.g, color.b

    def click(self):
        pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))

    def poll_events(self) -> Iterable[Event]:
        return pygame.event.get()

    def stop(self):
        pygame.quit()
