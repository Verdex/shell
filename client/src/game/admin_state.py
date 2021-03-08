
class AdminState:
    Game = "game"
    Console = "console"

    def __init__(self, window_width, window_height):
        self.active = True
        self.event_loop_delta = 0
        self.window_height = window_height
        self.window_width = window_width
        self.game_window_width = 0
        self.game_window_height = 0
        self.console_window_width = 0
        self.console_window_height = 0
        self.mode = self.Game 
    