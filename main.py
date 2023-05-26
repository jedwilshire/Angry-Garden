import pygame
from settings import *
from random import randrange

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
#centi = pygame.sprite.Group()
centi = []
mushrooms = pygame.sprite.Group()
bullets = pygame.sprite.Group()
centiDelay = 50

player = pygame.sprite.Sprite()
player.image = pygame.Surface((TILESIZE, TILESIZE))
player.rect = player.image.get_rect()
player.rect.y = HEIGHT- TILESIZE
player.rect.x = WIDTH // 2




def update(dt):
    global centiDelay
    centiDelay -= dt
    if centiDelay <= 0:
        centiDelay = 100
        updateCenti()
    updateBullets()

def updateBullets():
    for bullet in bullets:
        bullet.rect.y += bullet.dy
        if bullet.rect.bottom <= 0:
            bullet.kill()
        mush = pygame.sprite.spritecollideany(bullet, mushrooms)
        if mush != None:
            mush.hitCount += 1
            if mush.hitCount == 4:
                mush.kill()
            elif mush.hitCount == 1:
                mush.image = pygame.Surface((TILESIZE, TILESIZE // 4 * 3))
                mush.image.fill(BROWN)
            elif mush.hitCount == 2:
                mush.image = pygame.Surface((TILESIZE, TILESIZE // 4 * 2))
                mush.image.fill(BROWN)
            elif mush.hitCount == 3:
                mush.image = pygame.Surface((TILESIZE, TILESIZE // 4))
                mush.image.fill(BROWN)   
            bullet.kill()
        else:
            for i in range(len(centi)):
                seg = centi[i]
                if seg != None:
                    collided = pygame.sprite.collide_rect(bullet, seg)
                    if collided == True:
                        rect = seg.rect
                        mush = pygame.sprite.Sprite(mushrooms)
                        mush.image = pygame.Surface((TILESIZE, TILESIZE))
                        mush.image.fill(BROWN)
                        mush.rect = rect
                        mush.hitCount = 0
                        centi[i] = None
                        bullet.kill()
                        if i < len(centi) - 1:
                            nextSeg = centi[i + 1]
                            if nextSeg != None:
                                nextSeg.isHead = True
                                pygame.draw.circle(nextSeg.image, DARKGREEN, (TILESIZE // 2, TILESIZE // 2),
                                   TILESIZE // 2)
                        break
def updateCenti():
    for i in range(len(centi)):
        segment = centi[i]
        if segment != None:
            if segment.rect.y < 0:
                segment.rect.y += segment.dy * TILESIZE
            else:
                segment.rect.x += segment.dx * TILESIZE
                if (pygame.sprite.spritecollideany(segment, mushrooms) or
                    segment.rect.left < 0 or segment.rect.right > NUMCOLS * TILESIZE):
                    segment.rect.x -= segment.dx * TILESIZE
                    segment.rect.y += segment.dy * TILESIZE
                    segment.dx *= -1
                    if segment.rect.bottom >= HEIGHT:
                        segment.dy = -1
                    elif segment.rect.top == 0:
                        segment.dy = 1
                
                
        

def draw():
    screen.fill(BGCOLOR)
    for segment in centi:
        if segment != None:
            screen.blit(segment.image, segment.rect)
    mushrooms.draw(screen)
    bullets.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.update()

def onMousePress(x, y):
    bullet = pygame.sprite.Sprite(bullets)
    bullet.image = pygame.Surface((5, 20))
    bullet.image.fill(WHITE)
    bullet.rect = bullet.image.get_rect()
    bullet.rect.centerx = player.rect.centerx
    bullet.rect.bottom = player.rect.top
    bullet.dy = -BULLETSPEED
    # testing mechanics
#     for seg in centi:
#         if seg.rect.collidepoint(x, y):
#             rect = seg.rect
#             mush = pygame.sprite.Sprite(mushrooms)
#             mush.image = pygame.Surface((TILESIZE, TILESIZE))
#             mush.image.fill(BROWN)
#             mush.rect = rect
#             seg.kill()
def onMouseMove(x, y):
    player.rect.centerx = x
    player.rect.bottom = max(HEIGHT - 4 * TILESIZE, y)
    

def onMouseRelease(x, y):
    pass

def onKeyPress(key):
    pass

def onKeyRelease(key):
    pass
def createMushrooms():
   for i in range(30):
    mush = pygame.sprite.Sprite()
    mush.image = pygame.Surface((TILESIZE, TILESIZE))
    mush.image.fill(BROWN)
    mush.rect = mush.image.get_rect()
    mush.rect.x = randrange(0, NUMCOLS) * TILESIZE
    mush.rect.y = randrange(1, NUMROWS - 2) * TILESIZE
    while pygame.sprite.spritecollideany(mush, mushrooms) != None:
        mush.rect.x = randrange(0, NUMCOLS) * TILESIZE
        mush.rect.y = randrange(0, NUMROWS - 2) * TILESIZE
    mush.hitCount = 0
    mushrooms.add(mush)

def createCenti():
    for i in range(13):
        segment = pygame.sprite.Sprite()
        segment.image = pygame.Surface((TILESIZE, TILESIZE))
        segment.rect = segment.image.get_rect()
        segment.rect.x = WIDTH// 2 
        segment.rect.y = 0 - TILESIZE * i
        segment.dx = -1
        segment.dy = 1
        segment.image.fill(BGCOLOR)
        if i == 0:
            segment.isHead = True
            pygame.draw.circle(segment.image, PURPLE, (TILESIZE // 2, TILESIZE // 2),
                           TILESIZE // 2)
        else:
            segment.isHead = False
            pygame.draw.circle(segment.image, GREEN, (TILESIZE // 2, TILESIZE // 2),
                           TILESIZE // 2)
        centi.append(segment)
        

def mainloop():
    running = True
    clock = pygame.time.Clock()
    while running:
        update(clock.tick(FPS))
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                onMouseMove(event.pos[0], event.pos[1])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                onMousePress(event.pos[0], event.pos[1])
            elif event.type == pygame.MOUSEBUTTONUP:
                onMouseRelease(event.pos[0], event.pos[1])
            elif event.type == pygame.KEYDOWN:
                onKeyPress(event.key)
            elif event.type == pygame.KEYUP:
                onKeyRelease(event.key)
        


pygame.init()
createMushrooms()
createCenti()
mainloop()
