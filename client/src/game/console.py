
import pygame

class Console:

    EntryHeightMargin = -15
    EntryLineOffset = -20
    WidthMargin = 10
    Black = [0, 0, 0]

    def __init__(self, admin):
        self._font = pygame.font.SysFont(None, 18)
        self._admin = admin
        self._history = ["blah", "ikky", "nope"]
        self._entry = "line" 
        
    def add_line(self, line):
        pass

    def entry_char(self, char):
        pass

    def entry_del_char(self):
        pass

    def _render_at(self, screen, str, height):
        surface = self._font.render(str, True, self.Black)
        screen.blit(surface, (self.WidthMargin, height))

    def render_to_screen(self, screen):
        self._render_at(screen, self._entry, self._admin.window_height + self.EntryHeightMargin)
        pygame.draw.line(screen \
                        , self.Black \
                        , (0, self._admin.window_height + self.EntryLineOffset) \
                        , (self._admin.window_width, self._admin.window_height + self.EntryLineOffset))


    def entry_to_history(self):
        pass

    #font = pygame.font.SysFont(None, 18)
    
    #blarg = font.render('blah', True, [0,0,0])
    #screen.blit(blarg, (500, 100))