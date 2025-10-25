from hex.core.Application import Application
from hex.core.Color import DARK_GRAY
from hex.core.port import ForRunningGame
from test.core.render_helper.helper import dummy_file_system
from test.core.render_helper.SpyWindow import SpyWindow

def test_on_tick_renders_background():
    window = SpyWindow()
    game: ForRunningGame = Application(window, dummy_file_system())
    game.tick()
    assert window.background == DARK_GRAY

def test_application_notifies_window_about_finishing():
    spy = SpyWindow()
    game: ForRunningGame = Application(
        spy,
        dummy_file_system())
    game.tick()
    assert spy.renders == 1
