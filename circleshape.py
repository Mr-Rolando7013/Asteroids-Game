import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collide(self, target):
        #distance1 = self.position.distance_to()
        distance = self.position.distance_to(target.position)
        #print("DISTANCE: ", distance, "TARGET RADIUS:", target.radius, "SELF RADIUS: ", self.radius)
        if distance <= (self.radius + target.radius):
            return True

        else:
            return False
