import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adding Mario and Luigi as sprites")

background_image = pygame.transform.scale(
    pygame.image.load('Background.jpg').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

mario_image = pygame.transform.scale(
    pygame.image.load('').convert_alpha(),
    (200, 200)
)
mario_rect = mario_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-30))


luigi_image = pygame.transform.scale(
    pygame.image.load('').convert_alpha(),
    (200, 200)
)
luigi_rect = luigi_image.get_rect(center=(SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2-30))

text = pygame.font.Font(None, 36).render("Mario And Luigi", True, pygame.Color('red'))

text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT + 110))

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            display_surface.blit(background_image, (0, 0))
        display_surface.blit(mario_image, mario_rect)
        display_surface.blit(luigi_image, luigi_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    game_loop()