import os.path

from hex.CliTerminal import CliTerminal
from hex.core.Application import Application
from hex.core.GameLoop import GameLoop
from hex.OsFileSystem import OsFileSystem
from hex.PygameController import PygameController
from hex.PygameEngine import PygameEngine
from hex.PygameWindow import PygameWindow
from hex.QuitAfterPolls import QuitAfterPolls

def main():
    root = os.path.dirname(os.path.dirname(__file__))
    engine = PygameEngine()
    app = Application(
        PygameWindow(engine),
        OsFileSystem(root),
        PygameController(engine),
        CliTerminal())
    GameLoop(QuitAfterPolls(50), app).start()

if __name__ == '__main__':
    main()

# TODO
# - game updates the element
# - actually render a window
