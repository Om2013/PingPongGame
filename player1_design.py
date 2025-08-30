import pygame
class Player1Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("player_ping_pong_bat.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 6
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Wrap around top/bottom
        if self.rect.top > 600:  # WINDOW_HEIGHT
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = 600
