
class Entity:
    def __init__(self, surface, loc):
        self.surface = surface
        self.loc = loc

class EntityManager:

    def __init__(self):
        self.entities = {}

    def add(self, id, entity):
        self.entities[id] = entity
    
    def remove(self, id):
        del self.entities[id]

    def all_entities(self):
        return self.entities.items()