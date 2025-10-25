from hex.core.Color import Color
from hex.core.port import ForReadingSpriteFiles, ForRenderingView, ForRunningGame
from hex.core.SpriteLoader import SpriteLoader

class Application(ForRunningGame):
    def __init__(self, window: ForRenderingView, fs: ForReadingSpriteFiles):
        self.__window = window
        self.__loader = SpriteLoader(fs)

    def tick(self):
        self.__window.fill_background(Color(30, 31, 34))
        frames = [self.__loader.abs_path(frame) for frame in self.__sprite_frames()]
        for frame in frames:
            self.__window.draw_frame(frame)
        self.__window.render_finish()

    def click(self):
        pass

    def __sprite_frames(self) -> list[str]:
        return self.__loader.sprite('lightning').frames
