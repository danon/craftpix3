from contextlib import redirect_stdout
from io import StringIO

from hex.CliTerminal import CliTerminal
from hex.core.port import ForControlling

class Test_CliTerminal:
    def test_prints_to_standard_output(self):
        terminal = CliTerminal(FakeControls(['frame1.png']))
        assert captured_output(terminal) == "['frame1.png']"

class FakeControls(ForControlling):
    def __init__(self, frames: list[str]):
        self.__frames = frames

    def frames(self) -> list[str]:
        return self.__frames

def captured_output(terminal: CliTerminal) -> str:
    buffer = StringIO()
    with redirect_stdout(buffer):
        terminal.print()
    return buffer.getvalue().strip()
