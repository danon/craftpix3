from hex.core.port import ForRenderingView
from hex.PygameEngine import PygameEngine

class PygameWindow(ForRenderingView):
    def __init__(self, engine: PygameEngine):
        self.__engine = engine

    def fill_background(self, r: int, g: int, b: int):
        self.__engine.screen.fill((r, g, b))
