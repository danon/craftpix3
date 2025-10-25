from hex.core.GameLoop import GameLoop
from hex.core.port import ForReadingUserInput, ForRunningGame, WindowEvent
from test.core.QuitAfterPolls import QuitAfterPolls

def test_game_loop__does_not_tick():
    game = TickCountingGame()
    GameLoop(FakeInput(), game)
    assert game.ticks == 0

def test_game_loop_ticks_game():
    game = TickCountingGame()
    GameLoop(FakeInput(), game).tick()
    assert game.ticks == 1

def test_game_loop_ticks__until_is_quit():
    game = TickCountingGame()
    loop = GameLoop(QuitAfterPolls(3), game)
    loop.start()
    assert game.ticks == 3

def test_game_loop_directs_click_to_game():
    game = ClickCountingGame()
    GameLoop(WindowEvents([WindowEvent.Click]), game).tick()
    assert game.clicks == 1

class ClickCountingGame(ForRunningGame):
    def __init__(self):
        self.clicks = 0

    def click(self):
        self.clicks += 1

    def tick(self):
        pass

class TickCountingGame(ForRunningGame):
    def __init__(self):
        self.ticks = 0

    def tick(self):
        self.ticks += 1

    def click(self):
        pass

class FakeInput(ForReadingUserInput):
    def poll_events(self) -> list[WindowEvent]:
        return []

class WindowEvents(ForReadingUserInput):
    def __init__(self, events: list[WindowEvent]):
        self.__events = events

    def poll_events(self) -> list[WindowEvent]:
        return self.__events
