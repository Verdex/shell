
import pygame

class Console:

    EntryHeightMargin = -15
    EntryLineOffset = -18
    HistoryLineOffset = -95
    WidthMargin = 10
    Black = [0, 0, 0]

    def __init__(self, admin):
        self._font = pygame.font.SysFont(None, 18)
        self._admin = admin
        self._history = []
        self._entry = []
        
    def entry_char(self, char):
        self._entry.append(char)

    def entry_del_char(self):
        self._entry.pop()

    def console_top(self):
        return self._admin.window_height + self.HistoryLineOffset

    def _render_at(self, screen, str, height):
        surface = self._font.render(str, True, self.Black)
        screen.blit(surface, (self.WidthMargin, height))

    def render_to_screen(self, screen):
        self._render_at(screen, ''.join(self._entry), self._admin.window_height + self.EntryHeightMargin)
        pygame.draw.line( screen \
                        , self.Black \
                        , (0, self._admin.window_height + self.EntryLineOffset) \
                        , (self._admin.window_width, self._admin.window_height + self.EntryLineOffset))
        i = 2
        for h in self._history:
            self._render_at(screen, h, self._admin.window_height + (self.EntryHeightMargin * i))
            i += 1
        pygame.draw.line( screen \
                        , self.Black \
                        , (0, self._admin.window_height + self.HistoryLineOffset) \
                        , (self._admin.window_width, self._admin.window_height + self.HistoryLineOffset))


    def entry_to_history(self):
        if len(self._history) >= 5:
            self._history.pop()
        self._history.insert(0, ''.join(self._entry))
        self._entry = []
