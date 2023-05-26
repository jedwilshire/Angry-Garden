## COLORS
#                 R   G   B
BLACK         = (  0,  0,  0)
BLUE          = (  0,  0,255)
BROWN         = (165, 42, 42)
CORNSILK      = (255,248,220)
CRIMSON       = (220, 20, 60)
CYAN          = (  0,255,255)
DARKGREEN     = (  0,100,  0)
DARKSLATEGRAY = ( 47, 79, 79)
DIMGRAY       = (105,105,105)
FIREBRICK     = (178, 34, 34)
GOLD          = (255,215,  0)
GRAY          = (100,100,100)
GREEN         = (  0,128,  0)
HOTPINK       = (255,105,180)
INDIGO        = ( 75,  0,130)
IVORY         = (255,255,240)
MAGENTA       = (255,  0,255)
MAROON        = (128,  0,  0)
MIDNIGHTBLUE  = ( 25, 25,112)
NAVY          = (  0,  0,128)
LIGHTCORAL    = (240,128,128)
LIME          = (  0,255,  0)
OLIVE         = (128,128,128)
ORANGE        = (255,128,  0)
PINK          = (255,192,203)
PURPLE        = (128,  0,128)
RED           = (255,  0,  0)
ROYALBLUE     = ( 65,105,225)
SADDLEBROWN   = (139, 69, 19)
SIENNA        = (160, 82, 45)
SILVER        = (192,192,192)
SLATEGRAY     = (169,169,169)
VIOLET        = (238,130,238)
WHEAT         = (245,222,179)
WHITE         = (255,255,255)
YELLOW        = (255,255,  0)

def main():
    import pygame
    colors = {'black':BLACK,
              'blue':BLUE,
              'brown':BROWN,
              'cornsilk':CORNSILK,
              'crimson':CRIMSON,
              'cyan':CYAN,
              'darkgreen':DARKGREEN,
              'darkslategray':DARKSLATEGRAY,
              'dimgray':DIMGRAY,
              'firebrick':FIREBRICK,
              'gold':GOLD,
              'gray':GRAY,
              'green':GREEN,
              'hotpink':HOTPINK,
              'indigo':INDIGO,
              'ivory':IVORY,
              'magenta':MAGENTA,
              'maroon':MAROON,
              'midnightblue':MIDNIGHTBLUE,
              'navy':NAVY,
              'lightcoral':LIGHTCORAL,
              'lime':LIME,
              'olive':OLIVE,
              'orange':ORANGE,
              'pink':PINK,
              'purple':PURPLE,
              'red':RED,
              'royalblue':ROYALBLUE,
              'saddlebrown':SADDLEBROWN,
              'sienna':SIENNA,
              'slategray':SLATEGRAY,
              'voilet':VIOLET,
              'wheat':WHEAT,
              'yellow':YELLOW}
    pygame.init()
    running = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    size = 80
    cnames = list(colors.keys())
    cnames.sort()
    print(len(cnames))
    rect = pygame.Rect(0, 0, size, size)
    index = 0
    for r in range(7):
        for c in range(10):
            if index < len(cnames):
                rect.x = size * c
                rect.y = size * r
                pygame.draw.rect(screen, colors[cnames[index]], rect)
                index += 1
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        clock.tick(30)
if __name__=='__main__':
    main()