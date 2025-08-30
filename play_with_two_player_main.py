import pygame
from player1_design import Player1Paddle
from player2_design import Player2Paddle
from ball_design import Ball

def run_two_player():
    pygame.init()

    # ------------------ Window setup ------------------
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Ping Pong Two Player")

    # ------------------ Sounds ------------------
    hit_sound = pygame.mixer.Sound("ball_hit_sound.mp3")
    bounce_sound = pygame.mixer.Sound("boing-sound.mp3")
    player1_win_sound = pygame.mixer.Sound("victory_sound.mp3")
    player2_win_sound = pygame.mixer.Sound("lose_sound.mp3")
    background_music = pygame.mixer.Sound("background_music.mp3")
    background_music.play(-1)

    # ------------------ Clock, font, colors ------------------
    FPS = 60
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    WHITE = (255, 255, 255)

    # ------------------ Ball speed ------------------
    ball_vel_x, ball_vel_y = 5, -5

    # ------------------ Create objects ------------------
    player1 = Player1Paddle(30, WINDOW_HEIGHT // 2)
    player2 = Player2Paddle(WINDOW_WIDTH - 30, WINDOW_HEIGHT // 2)
    ball = Ball(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, ball_vel_x, ball_vel_y)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1, player2, ball)

    running = True
    player1_won = False
    player2_won = False

    # ------------------ Main game loop ------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update paddles and ball
        player1.update()
        player2.update()
        ball.update()

        # Ball collision with paddles
        if pygame.sprite.collide_rect(ball, player1):
            bounce_sound.play()
            ball.rect.left = player1.rect.right
            ball.velocity_x *= -1

        if pygame.sprite.collide_rect(ball, player2):
            bounce_sound.play()
            ball.rect.right = player2.rect.left
            ball.velocity_x *= -1

        # Ball goes off screen -> update scores
        if ball.rect.left <= 0:
            player2.score += 1
            ball.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            ball.velocity_x *= -1
        if ball.rect.right >= WINDOW_WIDTH:
            player1.score += 1
            ball.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            ball.velocity_x *= -1

        # Check for game over
        if player1.score >= 5:
            player1_won = True
            running = False
        elif player2.score >= 5:
            player2_won = True
            running = False

        # Draw everything
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        # Draw scores
        p1_score_text = font.render(f"P1 Score: {player1.score}", True, WHITE)
        screen.blit(p1_score_text, (10, 10))
        p2_score_text = font.render(f"P2 Score: {player2.score}", True, WHITE)
        screen.blit(p2_score_text, (WINDOW_WIDTH - 220, 10))

        pygame.display.update()
        clock.tick(FPS)

    # ------------------ Win/Lose screens ------------------
    background_music.stop()

    if player1_won:
        player1_win_sound.play()
        screen.fill((0, 0, 0))
        lose_text = font.render("Player 2 Lost!", True, WHITE)
        lose_rect = lose_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        screen.fill("black")
        screen.blit(lose_text, lose_rect)

        win_text = font.render("Player 1 Wins!", True, WHITE)
        win_rect = win_text.get_rect(center=(WINDOW_WIDTH // 2, 2 * WINDOW_HEIGHT // 3))
        screen.blit(win_text, win_rect)

        pygame.display.update()
        pygame.time.delay(2000)
        print("Player 1 Wins!")

    if player2_won:
        player2_win_sound.play()
        screen.fill((0, 0, 0))
        lose_text = font.render("Player 1 Lost!", True, WHITE)
        screen.fill("black")
        lose_rect = lose_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        screen.blit(lose_text, lose_rect)

        win_text = font.render("Player 2 Wins!", True, WHITE)
        win_rect = win_text.get_rect(center=(WINDOW_WIDTH // 2, 2 * WINDOW_HEIGHT // 3))
        screen.blit(win_text, win_rect)

        pygame.display.update()
        pygame.time.delay(2000)
        print("Player 2 Wins!")

    pygame.quit()
    exit()
