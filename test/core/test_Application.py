from hex.core.Application import Application
from hex.core.Color import Color
from hex.core.port import ForReadingSpriteFiles, ForRenderingFrames, ForRenderingView, ForRunningGame

def test_on_tick_renders_background():
    window = SpyWindow()
    game: ForRunningGame = Application(window, dummy_file_system())
    game.tick()
    assert window.background == Color(30, 31, 34)

def test_on_first_tick_renders_first_frame():
    spy = SpyWindow()
    game: ForRunningGame = Application(
        spy,
        FakeFileSystem(['frame1.png', 'frame2.png']))
    game.tick()
    assert '/root/obstacle/lightning/frame1.png' in spy.frames
    assert '/root/collect/castle/arrow/frame2.png' in spy.frames

def test_on_click_initiated_the_animation():
    spy = SpyWindow()
    game: ForRunningGame = Application(
        spy,
        FakeFileSystem(['frame1.png', 'frame2.png']))
    game.click()
    game.tick()
    assert '/root/obstacle/lightning/frame2.png' in spy.frames
    assert '/root/collect/castle/arrow/frame2.png' in spy.frames

def test_application_notifies_window_about_finishing():
    spy = SpyWindow()
    game: ForRunningGame = Application(
        spy,
        dummy_file_system())
    game.tick()
    assert spy.renders == 1

class SpyWindow(ForRenderingView):
    def __init__(self):
        self.background = None
        self.renders = 0
        self.frames = []

    def fill_background(self, color: Color):
        self.background = color
        self.frames = []

    def draw_frame(self, path: str, x: int, y: int) -> None:
        self.frames.append(path)

    def render_finish(self):
        self.renders += 1

def dummy_file_system() -> ForReadingSpriteFiles:
    return FakeFileSystem(['dummy1.png'])

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
