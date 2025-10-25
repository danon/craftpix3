from hex.core.Application import Application
from hex.core.Color import Color
from hex.core.port import ForControlling, ForReadingSpriteFiles, ForRenderingView

def test():
    application: ForControlling = Application(SpyWindow(), FakeFileSystem([
        'frame1.png', 'frame2.png'
    ]))
    assert application.frames() == [
        'resource/frame1.png',
        'resource/frame2.png',
    ]

def test_clicking_renders_background():
    window = SpyWindow()
    application: ForControlling = Application(window, FakeFileSystem([]))
    application.click()
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
