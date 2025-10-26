from dataclasses import dataclass

from hex.core.Color import Color
from hex.core.Point import Point
from hex.core.port import ForRenderingView

@dataclass
class RenderedFrame:
    path: str
    pos: Point
    flipped: bool

class SpyWindow(ForRenderingView):
    def __init__(self):
        self.background = None
        self.renders = 0
        self.__rendered_frames = []

    def fill_background(self, color: Color):
        self.background = color
        self.__rendered_frames = []

    def draw_frame(self, path: str, pos: Point, flipped: bool) -> None:
        self.__rendered_frames.append(RenderedFrame(path, pos, flipped))

    @property
    def frames(self) -> list[str]:
        return [frame.path for frame in self.__rendered_frames]

    @property
    def frames_pos(self) -> list[Point]:
        return [frame.pos for frame in self.__rendered_frames]

    @property
    def last_frame(self) -> RenderedFrame:
        return self.__rendered_frames[-1]

    def draw_text(self, text: str, pos: Point):
        pass

    def render_finish(self):
        self.renders += 1
