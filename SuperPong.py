import pygame 

def CreateWindow():
    # Form screen with 600x600 size
    # and with resizable
    screen = pygame.display.set_mode((600, 800))
    
    # set title
    pygame.display.set_caption('Super Pong')

    #set logo
    Icon = pygame.image.load('logo.webp')
    pygame.display.set_icon(Icon)
    
    # run window
    running = True
    while running:
        for event in pygame.event.get():
            
            CreateUpperBar(screen)
            CreateLowerBar(screen)
            CreateBall(screen)

            pygame.display.update()
            
            if event.type == pygame.QUIT:
                running = False

    # quit pygame after closing window
    pygame.quit()

def CreateUpperBar(screen):
    # Using draw.rect module of
    # pygame to draw the solid rectangle
    pygame.draw.rect(screen, (0,   255, 255),
                    [250, 10, 100, 10], 0)

def CreateLowerBar(screen):
    # Using draw.rect module of
    # pygame to draw the solid rectangle
    pygame.draw.rect(screen, (0,   0, 255),
                    [250, 780, 100, 10], 0)

def CreateBall(screen):
    # Using draw.rect module of
    #pygame to draw the solid circle
    pygame.draw.circle(screen, (0, 255, 0),
                   [300, 400], 10, 0)

def MoveBars():
    print("teste")

def main():
    CreateWindow()

if __name__ == "__main__":
    main()

