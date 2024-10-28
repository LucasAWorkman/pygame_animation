import pygame, random, time

def main():
    pygame.init()

    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Charlie!")

    #Entities
    #yellow background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("black")

    #load an image
    cardinal = pygame.image.load("Charlie.jpg")
    cardinal = cardinal.convert_alpha()
    cardinal = pygame.transform.scale(cardinal, (100, 100))

    # set up some cardinal variables
    cardinal_x = 0
    cardinal_y = 200

    #ACTION

        #Assign
    clock = pygame.time.Clock()
    keepGoing = True

        #Loop
    move = False
    while keepGoing:

        #Time
        clock.tick(75) ## changing this made the img move faster

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    move = not move
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    move = not move

        if move:
            cardinal_y += random.randint(-100,100)
            cardinal_x += random.randint(-100, 100)
            time.sleep(0.1)
        #check boundaries
        if cardinal_x > screen.get_width():
            cardinal_x = 320
        if cardinal_y > screen.get_width():
            cardinal_y = 240
        if cardinal_y < 0:
            cardinal_y = 240
        if cardinal_x < 0:
            cardinal_x = 320
        

        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(cardinal, (cardinal_x, cardinal_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
