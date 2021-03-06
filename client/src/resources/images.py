
from resources.util import load_image

class Image:
    def __init__(self, name, size, image):
        self.name = name
        self.size = size
        self.image = image

class Images:

    def __init__(self):
        self.at_symbol = Image("at_symbol", (32, 32), load_image("at_symbol.png"))
