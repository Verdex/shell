
from resources.util import load_image
import resources.sizes as sizes

class Image:
    def __init__(self, name, size, image):
        self.name = name
        self.size = size
        self.image = image

class Images:

    def __init__(self):
        self.at_symbol = Image("at_symbol", sizes.Normal, load_image("at_symbol.png"))
