from abc import ABC, abstractmethod
from enum import Enum

from hex.core.Color import Color

class ForRunningGame(ABC):
    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def frames(self) -> list[str]:
        pass

class WindowEvent(Enum):
    Close = 1
    Click = 2

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

class ForRenderingFrames(ABC):
    @abstractmethod
    def render_frames(self, frames: list[str]):
        pass
