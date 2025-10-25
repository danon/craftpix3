from abc import ABC, abstractmethod

from hex.core.Color import Color

class ForControlling(ABC):
    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def frames(self) -> list[str]:
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
