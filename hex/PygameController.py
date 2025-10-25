import pygame

from hex.core.port import ForReadingUserInput, WindowEvent
from hex.PygameEngine import PygameEngine

class PygameController(ForReadingUserInput):
    def __init__(self, engine: PygameEngine):
        self.__engine = engine

    def poll_events(self) -> list[WindowEvent]:
        events = []
        for event in self.__engine.poll_events():
            if event.type == pygame.MOUSEBUTTONDOWN:
                events.append(WindowEvent.Click)
            if event.type == pygame.QUIT:
                events.append(WindowEvent.Close)
        return events
