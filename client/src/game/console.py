
import pygame

class Console:

    EntryHeightMargin = -15
    EntryLineOffset = -18
    HistoryLineOffset = -170
    WidthMargin = 10
    Black = [0, 0, 0]
    White = [255, 255, 255]

    def __init__(self, admin):
        self._font = pygame.font.SysFont(None, 18)
        self._admin = admin
        self._history = []
        self._entry = []
        
    def entry_char(self, char):
        self._entry.append(char)

    def entry_del_char(self):
        if len(self._entry) > 0:
            self._entry.pop()

    def height(self):
        return self.HistoryLineOffset * -1

    def _render_at(self, screen, str, height):
        surface = self._font.render(str, True, self.Black)
        screen.blit(surface, (self.WidthMargin, height))

    def render_to_screen(self, screen):
        screen.fill(self.White)
        self._render_at(screen, ''.join(self._entry), self._admin.console_window_height + self.EntryHeightMargin)
        pygame.draw.line( screen \
                        , self.Black \
                        , (0, self._admin.console_window_height + self.EntryLineOffset) \
                        , (self._admin.console_window_width, self._admin.console_window_height + self.EntryLineOffset))
        i = 2
        for h in self._history:
            self._render_at(screen, h, self._admin.console_window_height + (self.EntryHeightMargin * i))
            i += 1
        pygame.draw.line( screen \
                        , self.Black \
                        , (0, self._admin.console_window_height + self.HistoryLineOffset) \
                        , (self._admin.console_window_width, self._admin.console_window_height + self.HistoryLineOffset))


    def entry_to_history(self):
        if len(self._history) >= 10:
            self._history.pop()
        self._history.insert(0, ''.join(self._entry))
        self._entry = []

    def get_entry(self):
        return ''.join(self._entry)

    def to_history(self, line):
        if len(self._history) >= 10:
            self._history.pop()
        self._history.insert(0, line)