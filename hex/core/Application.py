from hex.core.Color import Color
from hex.core.port import ForReadingSpriteFiles, ForRenderingFrames, ForRenderingView, ForRunningGame
from hex.core.SpriteLoader import SpriteLoader

class Application(ForRunningGame):
    def __init__(
            self,
            window: ForRenderingView,
            fs: ForReadingSpriteFiles,
            frames: ForRenderingFrames):
        self.__window = window
        self.__loader = SpriteLoader(fs)
        self.__frames = frames

    def tick(self):
        self.__window.fill_background(Color(30, 31, 34))
        self.__frames.render_frames([
            self.__loader.abs_path(frame)
            for frame
            in self.__sprite_frames()
        ])

    def click(self):
        pass

    def __sprite_frames(self) -> list[str]:
        return self.__loader.sprite('lightning').frames
