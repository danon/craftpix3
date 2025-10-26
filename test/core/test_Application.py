from hex.core.Application import Application
from hex.core.Color import DARK_GRAY
from hex.core.Point import Point
from hex.core.port import ForReadingSpriteFiles, ForRunningGame
from test.core.render_helper.FakeFileSystem import FakeFileSystem
from test.core.render_helper.helper import dummy_file_system
from test.core.render_helper.SpyWindow import SpyWindow

def test_on_tick_renders_background():
    window = SpyWindow()
    game: ForRunningGame = Application(window, dummy_file_system())
    game.tick()
    assert window.background == DARK_GRAY

def test_application_notifies_window_about_finishing():
    spy = SpyWindow()
    game: ForRunningGame = Application(spy, dummy_file_system())
    game.tick()
    assert spy.renders == 1

def test_idle_hero_is_rendered():
    spy = SpyWindow()
    game: ForRunningGame = Application(spy, dummy_fs())
    game.tick()
    assert '/root/hero/knight1/idle/frame1.png' in spy.frames

def test_hero_has_moved_right():
    spy = SpyWindow()
    game: ForRunningGame = Application(spy, dummy_fs())
    game.right(True)
    game.tick()
    assert Point(1, 0) in spy.frames_pos

def test_hero_has_moved_left():
    spy = SpyWindow()
    game: ForRunningGame = Application(spy, dummy_fs())
    game.left(True)
    game.tick()
    assert Point(-1, 0) in spy.frames_pos

def test_hero_stops_moving_left_when_key_is_not_active():
    spy = SpyWindow()
    game: ForRunningGame = Application(spy, dummy_fs())
    game.left(True)
    game.left(False)
    game.tick()
    assert Point(0, 0) in spy.frames_pos

def test_hero_stops_moving_right_when_key_is_not_active():
    spy = SpyWindow()
    game: ForRunningGame = Application(spy, dummy_fs())
    game.right(True)
    game.right(False)
    game.tick()
    assert Point(0, 0) in spy.frames_pos

def dummy_fs() -> ForReadingSpriteFiles:
    return FakeFileSystem(['frame1.png'])
