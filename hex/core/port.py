from abc import ABC, abstractmethod

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
