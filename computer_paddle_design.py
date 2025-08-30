import pygame
class ComputerPaddle(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()  
        self.image = pygame.image.load("computer_ping_pong_bat.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed  # store it in the class
        self.score = 0

    def update(self, ball):
        if ball.rect.centery > self.rect.centery:
            self.rect.y += self.speed
        elif ball.rect.centery < self.rect.centery:
            self.rect.y -= self.speed

 