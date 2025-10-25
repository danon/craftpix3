from hex.core.Color import DARK_GRAY
from hex.core.port import ForRunningGame
from hex.core.SpritePreview import SpritePreview
from test.core.render_helper.FakeFileSystem import FakeFileSystem
from test.core.render_helper.helper import dummy_file_system
from test.core.render_helper.SpyWindow import SpyWindow

def test_on_tick_renders_background():
    window = SpyWindow()
    game: ForRunningGame = SpritePreview(window, dummy_file_system())
    game.tick()
    assert window.background == DARK_GRAY

def test_on_first_tick_renders_first_frame():
    spy = SpyWindow()
    game: ForRunningGame = SpritePreview(
        spy,
        FakeFileSystem(['frame1.png', 'frame2.png']))
    game.tick()
    assert '/root/obstacle/lightning/frame1.png' in spy.frames
    assert '/root/collect/castle/arrow/frame2.png' in spy.frames

def test_on_click_initiated_the_animation():
    spy = SpyWindow()
    game: ForRunningGame = SpritePreview(
        spy,
        FakeFileSystem(['frame1.png', 'frame2.png']))
    game.click()
    game.tick()
    assert '/root/obstacle/lightning/frame2.png' in spy.frames
    assert '/root/collect/castle/arrow/frame2.png' in spy.frames

def test_application_notifies_window_about_finishing():
    spy = SpyWindow()
    game: ForRunningGame = SpritePreview(
        spy,
        dummy_file_system())
    game.tick()
    assert spy.renders == 1
