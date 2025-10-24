from typing import Generator

from pytest import fixture

from hex.core.port import ForControlling
from hex.PygameController import PygameController
from hex.PygameEngine import PygameEngine

@fixture
def engine() -> Generator[PygameEngine]:
    engine = PygameEngine()
    yield engine
    engine.stop()

class Test_PygameController:
    def test_not_direct_click_when_mouse_is_not_down(self, engine: PygameEngine):
        game = ClickCountingGame()
        PygameController(engine, game).send_controls()
        assert game.clicks == 0

    def test_direct_click__when_mouse_is_down(self, engine: PygameEngine):
        game = ClickCountingGame()
        controller = PygameController(engine, game)
        engine.click()
        controller.send_controls()
        assert game.clicks == 1

class ClickCountingGame(ForControlling):
    def __init__(self):
        self.clicks = 0

    def click(self) -> None:
        self.clicks += 1

    def frames(self) -> list[str]:
        return []
