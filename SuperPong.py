import pygame 

screen = pygame.display.set_mode((600, 800))
UpperY = 10
LowerY = 780
width = 100
height = 10

def CreateWindow():
    x = 250
    z = 250
    control = 0
    aux = 1
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
        x, control = MoveUpperBar(x, control)
        z, aux = MoveLowerBar(z, aux)
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

def MoveUpperBar(x, control):
    speed = 1

    if x==0:
        control = 1
    if x==600-width:
        control = 0

    if control == 0:
        x -= speed

    if control == 1:
        x += speed

    CreateUpperBar(x)
    return x, control

def MoveLowerBar(z, aux):
    speed = 1

    if z==0:
        aux = 1
    if z==600-width:
        aux = 0

    if aux == 0:
        z -= speed

    if aux == 1:
        z += speed

    CreateLowerBar(z)
    return z, aux

def main():
    CreateWindow()

if __name__ == "__main__":
    main()
