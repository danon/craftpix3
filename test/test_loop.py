from pix.loop import Game, GameLoop, Window, WindowEvent

def test_game_loop_directs_clicks_from_window_to_game():
    game = ClickCountingGame()
    engine = PollEventWindow()
    loop = GameLoop(game, engine)
    engine.mouse_click()
    loop.tick()
    assert game.clicks == 1

def test_game_loop_ticks_until_quit():
    game = TickCountingGame()
    loop = GameLoop(game, QuitAfterPollsWindow(3))
    loop.start()
    assert game.ticks == 3

class ClickCountingGame(Game):
    def __init__(self):
        self.clicks = 0

    def tick(self):
        pass

    def click(self):
        self.clicks += 1

class TickCountingGame(Game):
    def __init__(self):
        self.ticks = 0

    def tick(self):
        self.ticks += 1

    def click(self):
        pass

class PollEventWindow(Window):
    def __init__(self):
        self.__events: list[WindowEvent] = []

    def mouse_click(self):
        self.__events.append(WindowEvent.Click)

    def poll_events(self) -> list[WindowEvent]:
        events = self.__events
        self.__events = []
        return events

class QuitAfterPollsWindow(Window):
    def __init__(self, polls: int):
        self.__polls = polls

    def poll_events(self) -> list[WindowEvent]:
        self.__polls -= 1
        if self.__polls > 0:
            return []
        return [WindowEvent.Close]
