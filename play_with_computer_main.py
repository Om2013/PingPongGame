def run_play_with_computer():
    # ------------------ Difficulty at the very start ------------------
    difficulty = input("Select difficulty (E=Easy, M=Medium, H=Hard, R=Random): ").strip().upper()
    if difficulty == "R":
        import random 
        difficulty = random.choice(["E", "M", "H"])
        print(f"Random difficulty chosen: {difficulty}")

    if difficulty == "E":
        ball_vel_x, ball_vel_y = 3, -3
        comp_speed = 2
    elif difficulty == "M":
        ball_vel_x, ball_vel_y = 5, -5
        comp_speed = 4
    elif difficulty == "H":
        ball_vel_x, ball_vel_y = 7, -7
        comp_speed = 6
    else:
        ball_vel_x, ball_vel_y = 5, -5
        comp_speed = 4

    print(f"Difficulty: {difficulty}")
    print(f"Ball speed: {ball_vel_x}")
    print(f"Computer paddle speed: {comp_speed}")

    # ------------------ Pygame initialization ------------------
    import pygame 
    from computer_paddle_design import ComputerPaddle
    from ball_design import Ball
    from player1_design import Player1Paddle
    

    pygame.init()
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Ping Pong Game")

    hit_sound = pygame.mixer.Sound("ball_hit_sound.mp3")
    bounce_sound = pygame.mixer.Sound("boing-sound.mp3")
    player_win_sound = pygame.mixer.Sound("victory_sound.mp3")
    lose_sound = pygame.mixer.Sound("lose_sound.mp3")
    background_music = pygame.mixer.Sound("background_music.mp3")
    background_music.play(-1)

    FPS = 60
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    WHITE = (255, 255, 255)

    # ------------------ Create objects ------------------
    player_paddle = Player1Paddle(30, WINDOW_HEIGHT // 2)
    computer_paddle = ComputerPaddle(WINDOW_WIDTH - 30, WINDOW_HEIGHT // 2, comp_speed)
    ball = Ball(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, ball_vel_x, ball_vel_y)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player_paddle, computer_paddle, ball)

    # ------------------ Main game loop ------------------
    running = True
    gamewin = False
    gamelost = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player_paddle.update()
        computer_paddle.update(ball)
        ball.update()

        # Ball collision with paddles
        if pygame.sprite.collide_rect(ball, player_paddle):
            bounce_sound.play()
            ball.rect.left = player_paddle.rect.right
            ball.velocity_x *= -1

        if pygame.sprite.collide_rect(ball, computer_paddle):
            bounce_sound.play()
            ball.rect.right = computer_paddle.rect.left
            ball.velocity_x *= -1

        # Ball goes off screen -> update scores
        if ball.rect.left <= 0:
            computer_paddle.score += 1
            ball.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            ball.velocity_x *= -1
        if ball.rect.right >= WINDOW_WIDTH:
            player_paddle.score += 1
            ball.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            ball.velocity_x *= -1

        # Check for game over
        if player_paddle.score >= 5:
            gamewin = True
            running = False
        elif computer_paddle.score >= 5:
            gamelost = True
            running = False

        # Draw everything
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        # Draw scores
        player_score_text = font.render(f"Player Score: {player_paddle.score}", True, WHITE)
        screen.blit(player_score_text, (10, 10))
        computer_score_text = font.render(f"Computer Score: {computer_paddle.score}", True, WHITE)
        screen.blit(computer_score_text, (WINDOW_WIDTH - 220, 10))

        pygame.display.update()
        clock.tick(FPS)

    # ------------------ Win/Lose screens ------------------
    background_music.stop()

    if gamewin:
        player_win_sound.play()
        screen.fill((0, 0, 0))
        gamewin_text = font.render("You Win!", True, WHITE)
        gamewin_rect = gamewin_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        screen.blit(gamewin_text, gamewin_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        print("Run to play again!")

    if gamelost:
        lose_sound.play()
        screen.fill((0, 0, 0))
        defeat_text = font.render("You Lose!", True, WHITE)
        defeat_rect = defeat_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        screen.blit(defeat_text, defeat_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        print("Run to play again")

    pygame.quit()
    exit()


