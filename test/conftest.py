from typing import Generator

from pytest import fixture

from hex.PygameEngine import PygameEngine

@fixture
def engine() -> Generator[PygameEngine]:
    engine = PygameEngine()
    yield engine
    engine.stop()
