from pygame import K_LEFT, K_RIGHT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, QUIT

from hex.core.port import ForReadingUserInput, WindowEvent
from hex.infra.PygameEngine import PygameEngine

class PygameController(ForReadingUserInput):
    def __init__(self, engine: PygameEngine):
        self.__engine = engine

    def poll_events(self) -> list[WindowEvent]:
        events = []
        for event in self.__engine.poll_events():
            if event.type == MOUSEBUTTONDOWN:
                events.append(WindowEvent.Click)
            if event.type == QUIT:
                events.append(WindowEvent.Close)
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    events.append(WindowEvent.RightDown)
                if event.key == K_LEFT:
                    events.append(WindowEvent.LeftDown)
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    events.append(WindowEvent.RightUp)
                if event.key == K_LEFT:
                    events.append(WindowEvent.LeftUp)
        return events
