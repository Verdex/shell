
import pygame

class ConsoleMode:
    def __init__(self, key_mode, console, executor):
        self._console = console
        self._executor = executor 
        self._mode = key_mode

    def key_down(self, event):
        if event.key == pygame.K_RETURN:
            entry = self._console.get_entry()
            self._console.entry_to_history()
            self._executor.execute(entry)
        elif event.key == pygame.K_BACKSPACE:
            self._console.entry_del_char()
        elif event.key == pygame.K_ESCAPE:
            self._mode.switch_to_game()
        else:
            self._console.entry_char(event.unicode) 
    
    def key_up(self, event):
        pass
    

class GameMode:
    def __init__(self, key_mode):
        self._mode = key_mode

    def key_down(self, event):
        if event.key == pygame.K_UP or event.key == pygame.K_k:
            pass
        elif event.key == pygame.K_DOWN or event.key == pygame.K_j:
            pass
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_l:
            pass
        elif event.key == pygame.K_LEFT or event.key == pygame.K_h:
            pass
        elif event.key == pygame.K_i:
            self._mode.switch_to_console()
    
    def key_up(self, event):
        pass

class KeyMode:

    def __init__(self, console, console_executor):
        self._console_mode = ConsoleMode(self, console, console_executor)
        self._game_mode = GameMode(self)
        self._mode = self._game_mode 

    def switch_to_console(self):
        self._mode = self._console_mode

    def switch_to_game(self):
        self._mode = self._game_mode

    def key_down(self, event):
        self._mode.key_down(event)

    def key_up(self, event):
        self._mode.key_up(event)


