from hex.core.port import ForControlling, ForReadingSpriteFiles
from hex.core.SpriteLoader import SpriteLoader

class Application(ForControlling):
    def __init__(self, fs: ForReadingSpriteFiles):
        self.__loader = SpriteLoader(fs)

    def click(self):
        pass

    def frames(self) -> list[str]:
        return self.__loader.sprite('resource').frames
