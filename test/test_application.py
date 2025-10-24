from pix.application import Application, Game, Window, WindowEvent

def test_application_directs_clicks_from_window_to_game():
    game = ClickCountingGame()
    engine = PollEventWindow()
    application = Application(game, engine)
    engine.mouse_click()
    application.tick()
    assert game.clicks == 1

class PollEventWindow(Window):
    def __init__(self):
        self.__events: list[WindowEvent] = []

    def mouse_click(self):
        self.__events.append(WindowEvent.Click)

    def poll_events(self) -> list[WindowEvent]:
        events = self.__events
        self.__events = []
        return events

class ClickCountingGame(Game):
    def __init__(self):
        self.clicks = 0

    def click(self):
        self.clicks += 1
