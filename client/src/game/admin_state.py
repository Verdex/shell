
class AdminState:
    def __init__(self, window_width, window_height):
        self.active = True
        self.event_loop_delta = 0
        self.window_height = window_height
        self.window_width = window_width