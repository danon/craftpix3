from hex.core.Color import Color
from hex.core.Point import Point
from hex.core.port import ForRenderingView

class SpyWindow(ForRenderingView):
    def __init__(self):
        self.background = None
        self.renders = 0
        self.frames = []

    def fill_background(self, color: Color):
        self.background = color
        self.frames = []

    def draw_frame(self, path: str, pos: Point) -> None:
        self.frames.append(path)

    def render_finish(self):
        self.renders += 1
