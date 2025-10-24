from abc import ABC, abstractmethod
from enum import Enum

class WindowEvent(Enum):
    Close = 1
    Click = 2

class Window(ABC):
    @abstractmethod
    def poll_events(self) -> list[WindowEvent]:
        pass

class Game(ABC):
    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def click(self):
        pass

class GameLoop:
    def __init__(self, game: Game, window: Window):
        self.__game = game
        self.__window = window
        self.__running = True

    def start(self):
        while self.__running:
            self.tick()

    def tick(self):
        self.__game.tick()
        for event in self.__window.poll_events():
            if event == WindowEvent.Click:
                self.__game.click()
            if event == WindowEvent.Close:
                self.__running = False
