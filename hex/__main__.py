from hex.CliTerminal import CliTerminal
from hex.core.Application import Application
from hex.FakeFileSystem import FakeFileSystem

def main():
    app = Application(FakeFileSystem())
    CliTerminal(app).print()

if __name__ == '__main__':
    main()

# TODO
# - OsFs loads returns paths in folder
# - pygame accepts mouse click and directs it to the game,
#     to initiate the game element
# - game ticks and updates the element
# - pygame renders background and the frame of the element
# - quit game
