from hex.core.Color import DARK_GRAY
from hex.core.port import ForReadingSpriteFiles, ForRenderingView, ForRunningGame

class Application(ForRunningGame):
    def __init__(
            self,
            window: ForRenderingView,
            fs: ForReadingSpriteFiles):
        self.__window = window
        self.__fs = fs

    def right(self):
        pass

    def left(self):
        pass

    def click(self):
        pass

    def tick(self):
        self.__window.fill_background(DARK_GRAY)
        self.__window.render_finish()
