from hex.core.Color import Color
from hex.core.GameState import Element, GameState
from hex.core.port import ForReadingSpriteFiles, ForRenderingView, ForRunningGame
from hex.core.SpriteLoader import SpriteLoader

class Application(ForRunningGame):
    def __init__(self, window: ForRenderingView, fs: ForReadingSpriteFiles):
        self.__window = window
        self.__loader = SpriteLoader(fs)
        self.__ticks = 0
        self.__state = GameState()
        self.__state.element = Element(self.__loader.sprite('lightning'))

    def tick(self):
        self.__state.element.tick()
        self.__window.fill_background(Color(30, 31, 34))
        self.__window.draw_frame(
            self.__loader.abs_path(self.__state.element.frame())
        )
        self.__window.render_finish()
        self.__ticks += 1

    def click(self):
        self.__state.element.initiate()
