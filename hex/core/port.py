from abc import ABC, abstractmethod
from enum import Enum

from hex.core.Color import Color
from hex.core.Point import Point

class ForRunningGame(ABC):
    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def right(self, active: bool):
        pass

    @abstractmethod
    def left(self, active: bool):
        pass

class WindowEvent(Enum):
    Close = 1
    Click = 2
    RightDown = 3
    LeftDown = 4
    RightUp = 5
    LeftUp = 6

class ForReadingUserInput(ABC):
    @abstractmethod
    def poll_events(self) -> list[WindowEvent]:
        pass

class ForReadingSpriteFiles(ABC):
    @abstractmethod
    def root(self) -> str:
        pass

    @abstractmethod
    def list_files(self, path: str) -> list[str]:
        pass

class ForRenderingView(ABC):
    @abstractmethod
    def fill_background(self, color: Color):
        pass

    @abstractmethod
    def draw_frame(self, path: str, pos: Point, flipped: bool) -> None:
        pass

    @abstractmethod
    def draw_text(self, text: str, pos: Point):
        pass

    @abstractmethod
    def render_finish(self):
        pass

class ForRenderingFrames(ABC):
    @abstractmethod
    def render_frames(self, frames: list[str]):
        pass
