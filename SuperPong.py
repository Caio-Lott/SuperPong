import pygame 

screen = pygame.display.set_mode((600, 800))
UpperY = 10
LowerY = 780
width = 100
height = 10

def CreateWindow():
    x = 250
    z = 250
    # set title
    pygame.display.set_caption('Super Pong')

    #set logo
    Icon = pygame.image.load('logo.webp')
    pygame.display.set_icon(Icon)
    
    CreateUpperBar(x)
    CreateLowerBar(x)
    CreateBall()
    pygame.display.update()

    # run window
    running = True
    while running:
        for event in pygame.event.get():
         
            if event.type == pygame.QUIT:
                running = False

        pygame.time.delay(10)
        screen.fill((0, 0, 0))
        Ukey = pygame.key.get_pressed()
        Bkey = pygame.key.get_pressed()
        x = MoveUpperBar(x, Ukey)
        z = MoveLowerBar(z, Bkey)
        pygame.display.update()
    # quit pygame after closing window
    pygame.quit()

def CreateUpperBar(x):
    # Using draw.rect module of
    # pygame to draw the solid rectangle
    pygame.draw.rect(screen, (0,   255, 255),
                    [x, UpperY, width, height])

def CreateLowerBar(x):
    # Using draw.rect module of
    # pygame to draw the solid rectangle
    pygame.draw.rect(screen, (0,   0, 255),
                    [x, LowerY, width, height], 0)

def CreateBall():
    # Using draw.rect module of
    #pygame to draw the solid circle
    pygame.draw.circle(screen, (0, 255, 0),
                   [300, 400], 10, 0)

def MoveUpperBar(x, Ukey):
    speed = 1

    if Ukey[pygame.K_LEFT] and x>0:
        x -= speed

    if Ukey[pygame.K_RIGHT] and x<600-width:
        x += speed

    CreateUpperBar(x)
    return x

def MoveLowerBar(z, Bkey):
    speed = 1

    if Bkey[pygame.K_a] and z>0:
        z -= speed

    if Bkey[pygame.K_d] and z<600-width:
        z += speed

    CreateLowerBar(z)
    return z

def main():
    CreateWindow()

if __name__ == "__main__":
    main()
