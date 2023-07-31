import pygame
import random

#Deneme yaparken chatGPT ile yaptığım ufak çaplı bir oyun

# Oyun ekranı boyutları
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Yılanın boyutu ve hızı
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Pygame başlat
pygame.init()

# Oyun ekranı oluştur
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Yılan Oyunu')

clock = pygame.time.Clock()

# Başlangıçta yılanın uzunluğu
snake_length = 3

# Yılanın başlangıç pozisyonu
snake_x = SCREEN_WIDTH // 2
snake_y = SCREEN_HEIGHT // 2

# Yılanın hareket yönü
snake_dx = 0
snake_dy = 0

# Yılanın gövdesi
snake_body = [(snake_x, snake_y) for _ in range(snake_length)]

# Elma oluştur
def yeni_elma():
    return (random.randint(0, (SCREEN_WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
            random.randint(0, (SCREEN_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)

apple_x, apple_y = yeni_elma()

# Oyuncu puanı
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -SNAKE_SIZE
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            elif event.key == pygame.K_UP:
                snake_dy = -SNAKE_SIZE
                snake_dx = 0
            elif event.key == pygame.K_DOWN:
                snake_dy = SNAKE_SIZE
                snake_dx = 0

    # Yılanın başını hareket ettir
    snake_x += snake_dx
    snake_y += snake_dy

    # Yılanın sınırları kontrol et
    if snake_x < 0 or snake_x >= SCREEN_WIDTH or snake_y < 0 or snake_y >= SCREEN_HEIGHT:
        running = False

    # Yemi yedi mi kontrol et
    if snake_x == apple_x and snake_y == apple_y:
        score += 10
        apple_x, apple_y = yeni_elma()

        # Yılanın uzunluğunu arttır
        snake_length += 1
        snake_body.append((snake_x, snake_y))

    else:
        # Yılanın kuyruğunu düzenle
        snake_body.insert(0, (snake_x, snake_y))
        snake_body.pop()

    # Ekranı temizle
    screen.fill(BLACK)

    # Yılanı çiz
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    # Elmayı çiz
    pygame.draw.rect(screen, RED, (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE))

    # Puanı çiz
    font = pygame.font.SysFont(None, 30)
    score_text = font.render(f"Puan: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Ekranı güncelle
    pygame.display.update()

    # Oyun hızı
    clock.tick(SNAKE_SPEED)

pygame.quit()


