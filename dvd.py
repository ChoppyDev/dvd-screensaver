
import sys, pygame, random
pygame.init()
size = w,h = 1920, 1080
black = 0, 0,0


speed =  [1,1]

screen = pygame.display.set_mode(size)

dvdimg = pygame.image.load("dvd_logo.png")
dvdimg = pygame.transform.scale(dvdimg, (200, 100) )
dvdhitbox = dvdimg.get_rect()
dvdhitbox2 = dvdimg.convert_alpha()

print(dvdhitbox2)

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tintimg = dvdimg.convert_alpha()
    color = r,g,b,100
    print(r,g,b)
    dvdimg.fill(color,None, special_flags=pygame.BLEND_RGB_MAX)

randomColor()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()

    if dvdhitbox.left + dvdhitbox.width >= w or dvdhitbox.left < 0: 
        speed[0] = -speed[0]
        randomColor()

    if dvdhitbox.top + dvdhitbox.height >= h or dvdhitbox.top < 0: 
        speed[1] = -speed[1]
        randomColor()

    dvdhitbox = dvdhitbox.move(speed)
    screen.fill(black)
    screen.blit(dvdimg, dvdhitbox)
    pygame.display.flip()