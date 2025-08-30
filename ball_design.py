import pygame
WINDOW_HEIGHT=600

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__()
        self.image = pygame.image.load("ball_image.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def update(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # Bounce off top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.velocity_y *= -1
