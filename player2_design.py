import pygame 
class Player2Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("player_ping_pong_bat.png")
        new_player2_image_size=100,100
        self.image=pygame.transform.scale(self.image,new_player2_image_size)
        self.rect = self.image.get_rect(center=(x, y))
        self.score = 0
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

        # Keep paddle on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:  # WINDOW_HEIGHT
            self.rect.bottom = 600