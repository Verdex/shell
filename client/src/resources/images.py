
from resources.util import load_image
import resources.sizes as sizes

class Image:
    def __init__(self, id, name, size, image):
        self.id = id
        self.name = name
        self.size = size
        self.image = image

class Images:
    def __init__(self):
        self.at_symbol = Image(0, "at_symbol", sizes.Normal, load_image("at_symbol.png"))
