from contextlib import redirect_stdout
from io import StringIO
from typing import Callable

def captured_output(block: Callable) -> str:
    buffer = StringIO()
    with redirect_stdout(buffer):
        block()
    return buffer.getvalue().strip()
