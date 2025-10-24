from typing import Iterable

import pygame
from pygame.event import Event

class PygameEngine:
    def __init__(self):
        pygame.init()

    def click(self):
        pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))

    def poll_events(self) -> Iterable[Event]:
        return pygame.event.get()

    def stop(self):
        pygame.quit()
