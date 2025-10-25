from typing import Generator

from pytest import fixture

from hex.PygameEngine import PygameEngine

@fixture
def engine() -> Generator[PygameEngine]:
    engine = PygameEngine(300, 300, True)
    yield engine
    engine.stop()
