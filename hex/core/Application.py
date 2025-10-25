from hex.core.Color import Color
from hex.core.port import ForReadingSpriteFiles, ForRenderingView, ForRunningGame
from hex.core.SpriteLoader import SpriteLoader

class Application(ForRunningGame):
    def __init__(self, window: ForRenderingView, fs: ForReadingSpriteFiles):
        self.__window = window
        self.__loader = SpriteLoader(fs)
        self.__ticks = 0

    def tick(self):
        self.__window.fill_background(Color(30, 31, 34))
        frames = [self.__loader.abs_path(frame) for frame in self.__sprite_frames()]
        self.__window.draw_frame(frames[self.__ticks % len(frames)])
        self.__window.render_finish()
        self.__ticks += 1

    def click(self):
        pass

    def __sprite_frames(self) -> list[str]:
        return self.__loader.sprite('lightning').frames
