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
    game = EventStoringGame()
    GameLoop(WindowEvents([WindowEvent.Click]), game).tick()
    assert game.events == ['click']

def test_game_loop_directs_arrows_to_game():
    game = EventStoringGame()
    user_input = WindowEvents([
        WindowEvent.RightDown,
        WindowEvent.LeftDown,
        WindowEvent.RightUp,
        WindowEvent.LeftUp,
    ])
    GameLoop(user_input, game).tick()
    assert game.events == [
        'right down', 'left down',
        'right up', 'left up'
    ]

class EventStoringGame(ForRunningGame):
    def __init__(self):
        self.events = []

    def left(self, active: bool):
        self.events.append('left down' if active else 'left up')

    def right(self, active: bool):
        self.events.append('right down' if active else 'right up')

    def click(self):
        self.events.append('click')

    def tick(self):
        pass

class TickCountingGame(ForRunningGame):
    def __init__(self):
        self.ticks = 0

    def tick(self):
        self.ticks += 1

    def click(self):
        pass

    def left(self, active: bool):
        pass

    def right(self, active: bool):
        pass

class FakeInput(ForReadingUserInput):
    def poll_events(self) -> list[WindowEvent]:
        return []

class WindowEvents(ForReadingUserInput):
    def __init__(self, events: list[WindowEvent]):
        self.__events = events

    def poll_events(self) -> list[WindowEvent]:
        return self.__events
