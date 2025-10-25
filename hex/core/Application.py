from hex.core.Color import Color
from hex.core.port import ForControlling, ForReadingSpriteFiles, ForRenderingView
from hex.core.SpriteLoader import SpriteLoader

class Application(ForControlling):
    def __init__(self, window: ForRenderingView, fs: ForReadingSpriteFiles):
        self.__window = window
        self.__loader = SpriteLoader(fs)

    def click(self):
        self.__window.fill_background(Color(30, 31, 34))

    def frames(self) -> list[str]:
        return self.__loader.sprite('resource').frames
