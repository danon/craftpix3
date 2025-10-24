from abc import ABC, abstractmethod
from enum import Enum

class WindowEvent(Enum):
    Click = 1

class Window(ABC):
    @abstractmethod
    def poll_events(self) -> list[WindowEvent]:
        pass

class Game(ABC):
    @abstractmethod
    def click(self):
        pass

class Application:
    def __init__(self, game: Game, window: Window):
        self.__game = game
        self.__window = window

    def tick(self):
        for event in self.__window.poll_events():
            if event == WindowEvent.Click:
                self.__game.click()
