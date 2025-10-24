from abc import ABC, abstractmethod

class ForControlling(ABC):
    @abstractmethod
    def resource_root(self) -> str:
        pass

class ForReadingSpriteFiles(ABC):
    @abstractmethod
    def root(self) -> str:
        pass

    @abstractmethod
    def list_files(self, path: str) -> list[str]:
        pass

class Application(ForControlling):
    def __init__(self, fs: ForReadingSpriteFiles):
        self.__fs = fs

    def resource_root(self) -> str:
        return self.__fs.root()
