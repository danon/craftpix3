from hex.core.Application import Application
from hex.core.Color import Color
from hex.core.port import ForReadingSpriteFiles, ForRenderingFrames, ForRenderingView, ForRunningGame
from hex.NoRender import NoRender

def test_on_tick_renders_background():
    window = SpyWindow()
    game: ForRunningGame = Application(window, FakeFileSystem([]), NoRender())
    game.tick()
    assert window.background == Color(30, 31, 34)

def test_on_tick_renders_frame():
    spy = SpyRender()
    game: ForRunningGame = Application(
        SpyWindow(),
        FakeFileSystem(['frame1.png', 'frame2.png']),
        spy)
    game.tick()
    assert spy.frames == ['resource/frame1.png', 'resource/frame2.png']

class SpyWindow(ForRenderingView):
    def __init__(self):
        self.background = None

    def fill_background(self, color: Color):
        self.background = color

class FakeFileSystem(ForReadingSpriteFiles):
    def __init__(self, files: list[str]):
        self.__files = files

    def list_files(self, path: str) -> list[str]:
        return self.__files

    def root(self) -> str:
        return '/root'

class SpyRender(ForRenderingFrames):
    def __init__(self):
        self.frames = None

    def render_frames(self, frames: list[str]):
        self.frames = frames
