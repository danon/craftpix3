from hex.core.Color import Color
from hex.core.port import ForReadingSpriteFiles, ForReadingUserInput, ForRenderingFrames, ForRenderingView, ForRunningGame, WindowEvent
from hex.core.SpriteLoader import SpriteLoader

class Application(ForRunningGame):
    def __init__(
            self,
            window: ForRenderingView,
            fs: ForReadingSpriteFiles,
            input: ForReadingUserInput,
            frames: ForRenderingFrames):
        self.__window = window
        self.__loader = SpriteLoader(fs)
        self.__input = input
        self.__frames = frames

    def tick(self):
        for event in self.__input.poll_events():
            if event == WindowEvent.Click:
                self.__click()
        self.__frames.render_frames(self.frames())

    def __click(self):
        self.__window.fill_background(Color(30, 31, 34))

    def frames(self) -> list[str]:
        return self.__loader.sprite('resource').frames
