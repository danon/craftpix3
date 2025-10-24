from hex.CliTerminal import CliTerminal
from hex.core.port import ForControlling
from test.helper.captured_output import captured_output

class Test_CliTerminal:
    def test_prints_to_standard_output(self):
        terminal = CliTerminal(FakeControls(['frame1.png']))
        assert captured_output(lambda: terminal.print()) == "['frame1.png']"

class FakeControls(ForControlling):
    def __init__(self, frames: list[str]):
        self.__frames = frames

    def click(self):
        pass

    def frames(self) -> list[str]:
        return self.__frames
