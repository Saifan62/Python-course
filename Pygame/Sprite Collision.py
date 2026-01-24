import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 30
FONT_SIZE = 72

pygame.init()

bg = pygame.transform.scale(pygame.image.load("bg.jpg"),(SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("Cursive", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("blue"))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, 
            SCREEN_WIDTH -self.rect.width), 0)
        self.rect.y = max(
            min(self.rect.y + y_change,
            SCREEN_HEIGHT -self.rect.height), 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision Detection")
all_sprites = pygame.sprite.Group()

sp1= Sprite(pygame.Color("pink"), 20, 30)
sp1.rect.x, sp1.rect.y = random.randint(0, SCREEN_WIDTH - sp1.rect.width), random.randint(0, SCREEN_HEIGHT - sp1.rect.height)

all_sprites.add(sp1)

sp2= Sprite(pygame.Color("blue"), 20, 30)
sp2.rect.x, sp2.rect.y = random.randint(0, SCREEN_WIDTH - sp2.rect.width), random.randint(0, SCREEN_HEIGHT - sp2.rect.height)

all_sprites.add(sp2)


running,won = True,False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
                                         event.key == pygame.K_x):
            running = False

        if not won:
            keys = pygame.key.get_pressed()
            x_change = (keys[pygame.K_RIGHT] -keys[pygame.K_LEFT]) * MOVEMENT_SPEED

            keys = pygame.key.get_pressed()
            y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED

            sp1.move(x_change, y_change)

            if sp1.rect.colliderect(sp2):
                all_sprites.remove(sp2)
                won = True

        screen.blit(bg, (0, 0))
        all_sprites.draw(screen)

        if won:
            win_txt = font.render("You Win!", True, pygame.Color("black"))
            screen.blit(win_txt, ((SCREEN_WIDTH - win_txt.get_width()) // 2, (SCREEN_HEIGHT - win_txt.get_height()) // 2))

        pygame.display.flip()
    clock.tick(30)

pygame.quit()




            