from hex.core.Application import Application
from hex.core.Color import Color
from hex.core.port import ForReadingSpriteFiles, ForReadingUserInput, ForRenderingView, ForRunningGame, WindowEvent

def test():
    game: ForRunningGame = Application(SpyWindow(), FakeFileSystem([
        'frame1.png', 'frame2.png'
    ]), WindowEvents([]))
    assert game.frames() == [
        'resource/frame1.png',
        'resource/frame2.png',
    ]

def test_clicking_renders_background():
    window = SpyWindow()
    game: ForRunningGame = Application(
        window,
        FakeFileSystem([]),
        WindowEvents([WindowEvent.Click]))
    game.tick()
    assert window.background == Color(30, 31, 34)

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

class WindowEvents(ForReadingUserInput):
    def __init__(self, events: list[WindowEvent]):
        self.__events = events

    def poll_events(self) -> list[WindowEvent]:
        return self.__events
