import random
import time
import pygame
pygame.font.init()

WIN_WIDTH = 1400
WIN_HEIGHT = 750
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("No Brainer 2.0")

BG_IMG = pygame.image.load("C:\Users\ASUS\OneDrive - NSBM\Programming\Python prg\Py Gamesbg_2.png")
BG_IMG = pygame.transform.scale(BG_IMG, (WIN_WIDTH, WIN_HEIGHT))

PLAYER_WIDTH = 110
PLAYER_HEIGHT = 110 
HIT_BOX = pygame.image.load("C:\Users\ASUS\OneDrive - NSBM\Programming\Python prg\Py Games")
HIT_BOX = pygame.transform.scale(HIT_BOX, (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_IMG = pygame.image.load("C:/Users/ASUS/Downloads/Python prg/Py Games/doge_spaceship.png")
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_IMG_2 = pygame.image.load("C:/Users/ASUS/Downloads/Python prg/Py Games/doge_2_spaceship.png")
PLAYER_IMG_2 = pygame.transform.scale(PLAYER_IMG_2, (PLAYER_WIDTH, PLAYER_HEIGHT))
SHIELD_PLAYER_IMG = pygame.image.load("C:/Users/ASUS/Downloads/Python prg/Py Games/doge_shield_spaceship.png")
SHIELD_PLAYER_IMG = pygame.transform.scale(SHIELD_PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))


LOST_IMG = pygame.image.load("C:/Users/ASUS/Downloads/Python prg/Py Games/cry_dog.gif")
LOST_IMG = pygame.transform.scale(LOST_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))

HEART_IMG = pygame.image.load("C:/Users/ASUS/Downloads/Python prg/Py Games/heart_icon.png")
HEART_IMG = pygame.transform.scale(HEART_IMG, (20, 20))
HEART_SHADOW_IMG = pygame.image.load("C:/Users/ASUS/Downloads/Python prg/Py Games/heart_icon_shadow.png")
HEART_SHADOW_IMG = pygame.transform.scale(HEART_SHADOW_IMG, (20, 20))

PROJ_WIDTH = 60
PROJ_HEIGHT = 60
PROJ_VEL = 3
PROJ_IMG = pygame.image.load("C:/Users/ASUS/Downloads/Python prg/Py Games/catship_1.png")
PROJ_IMG = pygame.transform.scale(PROJ_IMG, (PROJ_WIDTH, PROJ_HEIGHT))
PROJ_IMG_1 = pygame.image.load("C:/Users/ASUS/Downloads/Python prg/Py Games/catship_2.png")
PROJ_IMG_1 = pygame.transform.scale(PROJ_IMG_1, (PROJ_WIDTH, PROJ_HEIGHT))

SHIELD_IMG = pygame.image.load("C:/Users/ASUS/Downloads/Python prg/Py Games/shield_icon.png")
SHIELD_IMG = pygame.transform.scale(SHIELD_IMG, (25, 25))
SHIELD_SHADOW_IMG = pygame.image.load("C:/Users/ASUS/Downloads/Python prg/Py Games/shield_icon_shadow.png")
SHIELD_SHADOW_IMG = pygame.transform.scale(SHIELD_SHADOW_IMG, (25, 25))
SHIELD_PROJ_IMG = pygame.transform.scale(SHIELD_IMG, (60, 60))

ICON_IMG = pygame.image.load("C:/Users/ASUS/Downloads/Python prg/Py Games/kek.png")
pygame.display.set_icon(ICON_IMG)

PLAYER_VEL = 5

FONT = pygame.font.SysFont("comicsans", 30)
LFONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, stars, heart_dis, hit_count, shields):
    WIN.blit(BG_IMG, (0, 0))

    WIN.blit(SHIELD_SHADOW_IMG, (WIN_WIDTH - 38, 45))

    if hit_count == -1:
        WIN.blit(SHIELD_PLAYER_IMG, (player.x - 30, player.y))
        WIN.blit(SHIELD_IMG, (WIN_WIDTH - 38, 45))
    elif hit_count == 2:
        WIN.blit(PLAYER_IMG_2, (player.x - 30, player.y))
    else:
        WIN.blit(PLAYER_IMG, (player.x - 30, player.y))

    for star in stars:
        WIN.blit(star[1], star[0])

    for shield in shields:
        WIN.blit(shield[1], shield[0])

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    heart_x = WIN_WIDTH - 35
    for _ in range(3):
        WIN.blit(HEART_SHADOW_IMG, (heart_x, 15))
        heart_x -= 30

    heart_x = WIN_WIDTH - 35
    for _ in range(heart_dis):
        WIN.blit(HEART_IMG, (heart_x, 15))
        heart_x -= 30

    pygame.display.update()

def check_collision(new_star, stars):
    for star in stars:
        if new_star.colliderect(star[0]):
            return True
    return False

def main():
    run = True

    player = pygame.Rect((WIN_WIDTH / 2) - 48/ 2, (WIN_HEIGHT / 2) - PLAYER_HEIGHT / 2, 48, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    start_time = time.time()

    star_add_increment = 2000
    star_count = 0
    stars = []
    shields = []

    proj_count = 1
    
    hit_count = 0
    last_shield_time = 0

    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count >= star_add_increment:
            for _ in range(2):
                while True:
                    star_x = random.randint(0, WIN_WIDTH - PROJ_WIDTH)
                    new_star = pygame.Rect(star_x, -PROJ_HEIGHT, PROJ_WIDTH, PROJ_HEIGHT)
                    if not check_collision(new_star, stars):
                        stars.append((new_star, PROJ_IMG))
                        break

            if elapsed_time >= 20:
                proj_count = 2

            for _ in range(proj_count):
                while True:
                    star_1_x = random.randint(0, WIN_WIDTH - PROJ_WIDTH)
                    new_star_1 = pygame.Rect(star_1_x, -PROJ_HEIGHT, PROJ_WIDTH, PROJ_HEIGHT)
                    if not check_collision(new_star_1, stars):
                        stars.append((new_star_1, PROJ_IMG_1))
                        break

            if elapsed_time - last_shield_time >= 5:
                while True:
                    shield_dis_x = random.randint(0, WIN_WIDTH - PROJ_WIDTH)
                    shield_dis = pygame.Rect(shield_dis_x, -PROJ_HEIGHT, PROJ_WIDTH, PROJ_HEIGHT)
                    if not check_collision(shield_dis, stars):
                        shields.append((shield_dis, SHIELD_PROJ_IMG))
                        last_shield_time = elapsed_time
                        break

            star_add_increment = max(1000, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIN_WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + PLAYER_HEIGHT <= WIN_HEIGHT:
            player.y += PLAYER_VEL
        
        hit = False
        for star in stars[:]:
            star[0].y += PROJ_VEL
            if star[0].y > WIN_HEIGHT:
                stars.remove(star)
            elif star[0].colliderect(player):
                stars.remove(star)
                hit = True
                break

        for shield in shields[:]:
            shield[0].y += PROJ_VEL
            if shield[0].y > WIN_HEIGHT:
                shields.remove(shield)
            elif shield[0].colliderect(player):
                shields.remove(shield)
                hit_count -= 1
                break
        
        if hit_count <=-1:
            hit_count = -1

        if hit:
            hit_count += 1

        if hit_count == 0:
            heart_dis = 3

        if hit_count == 1:
            heart_dis = 2

        elif hit_count == 2:
            heart_dis = 1

        elif hit_count == 3:
            lost_text = LFONT.render(f"GAME OVER!", 1, "white")
            score_text = LFONT.render(f"Time Survived: {round(elapsed_time)}s", 1, "white")
            pygame.draw.rect(WIN, (6, 57, 112), (WIN_WIDTH / 2 - 200, WIN_HEIGHT / 2 - 125, 400, 200))
            pygame.draw.rect(WIN, "black", (WIN_WIDTH / 2 - 195, WIN_HEIGHT / 2 - 120, 390, 190))
            WIN.blit(LOST_IMG, (WIN_WIDTH / 2 - PLAYER_WIDTH / 2, 200))
            WIN.blit(lost_text, (WIN_WIDTH / 2 - lost_text.get_width() / 2, WIN_HEIGHT / 2 - (lost_text.get_height())))
            WIN.blit(score_text, (WIN_WIDTH / 2 - score_text.get_width() / 2, WIN_HEIGHT / 2))
            pygame.display.update()
            pygame.time.delay(3000)
            break

        draw(player, elapsed_time, stars, heart_dis, hit_count, shields)

    pygame.quit()

if __name__ == "__main__":
    main()