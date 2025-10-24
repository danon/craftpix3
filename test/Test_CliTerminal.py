from contextlib import redirect_stdout
from io import StringIO

from hex.CliTerminal import CliTerminal
from test.FakeControls import FakeControls

class Test_CliTerminal:
    def test_prints_to_standard_output(self):
        terminal = CliTerminal(FakeControls('/fake'))
        assert captured_output(terminal) == '/fake'

def captured_output(terminal: CliTerminal) -> str:
    buffer = StringIO()
    with redirect_stdout(buffer):
        terminal.print()
    return buffer.getvalue().strip()
