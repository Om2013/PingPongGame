import pygame
from play_with_computer_main import run_play_with_computer
from play_with_two_player_main import run_two_player

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Select Game Mode")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
font = pygame.font.Font(None, 36)

# Buttons
button_cp = pygame.Rect(50, 100, 180, 50)
button_2p = pygame.Rect(270, 100, 180, 50)

running = True
while running:
    screen.fill(WHITE)
    
    # Draw buttons
    pygame.draw.rect(screen, GRAY, button_cp)
    pygame.draw.rect(screen, GRAY, button_2p)
    
    # Render text
    text_cp = font.render("Computer", True, BLACK)
    text_2p = font.render("Two Players", True, BLACK)
    
    # Center text inside buttons
    screen.blit(text_cp, (button_cp.x + (button_cp.width - text_cp.get_width()) // 2,
                          button_cp.y + (button_cp.height - text_cp.get_height()) // 2))
    screen.blit(text_2p, (button_2p.x + (button_2p.width - text_2p.get_width()) // 2,
                           button_2p.y + (button_2p.height - text_2p.get_height()) // 2))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_cp.collidepoint(event.pos):
                pygame.quit()
                run_play_with_computer()
            elif button_2p.collidepoint(event.pos):
                pygame.quit()
                run_two_player()
