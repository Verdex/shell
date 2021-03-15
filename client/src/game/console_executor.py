
import pygame
import sys

class ConsoleExecutor:
    def __init__(self, server, console):
        self._server = server
        self._console = console
        self._exit = False

    def execute(self, entry):
        words = entry.split()

        if len(words) == 0:
            pass
        elif words[0] == "connect":
            # todo ip parse and port (any number?)
            #self._server.connect(words[1], words[2])
            pass
        elif words[0] == "exit":
            self._exit = True
            self._console.to_history("Are you sure you want to quit?  [yes/no]")
        elif words[0] == "yes":
            if self._exit == True:
                pygame.quit()
                sys.exit()
        elif words[0] == "no":
            if self._exit == True:
                self._exit = False 
