from hex.core.GameLoop import GameLoop
from hex.core.port import ForReadingUserInput, ForRunningGame, WindowEvent
from hex.QuitAfterPolls import QuitAfterPolls

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

class TickCountingGame(ForRunningGame):
    def __init__(self):
        self.ticks = 0

    def tick(self):
        self.ticks += 1

    def frames(self) -> list[str]:
        return []

class FakeInput(ForReadingUserInput):
    def poll_events(self) -> list[WindowEvent]:
        return []
