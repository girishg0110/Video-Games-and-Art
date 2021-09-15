import pygame, random

class Player:
    def __init__(self, windowWidth, windowHeight, x, pColor):
        self.dims = (windowWidth//25, windowHeight//5)
        self.pos = (windowWidth//8 if x == 1 else windowWidth - windowWidth//8, windowHeight//2)
        self.color = pColor


    def update(self, screen, speed):
        self.pos = (self.pos[0], self.pos[1] + speed if self.pos[1] + speed < screen.get_height() - self.dims[1]//2 and self.pos[1] + speed> self.dims[1]//2 \
                                 else self.pos[1])

    def display(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos[0] - self.dims[0]//2, \
            self.pos[1] - self.dims[1]//2, self.dims[0], self.dims[1]))

class Ball:
    def __init__(self, surface, speed, radius, color = (255,255,255)):
        self.pos = (surface.get_width()//2, surface.get_height()//2)
        self.speed = ((2 + random.random() * speed), \
                        (2 + random.random() * speed))
        print(self.speed)
        self.radius = radius
        self.color = color

    def collisionDetected(self, surface, borderWidth, p1, p2):
        #Wall Collisions
        if (self.pos[0] + self.radius >= surface.get_width() - borderWidth or \
            self.pos[0] - self.radius <= borderWidth): #LR Walls
            self.speed = (-self.speed[0], self.speed[1])
        if (self.pos[1] + self.radius >= surface.get_height() - borderWidth or \
            self.pos[1] - self.radius <= borderWidth): #TB Walls
            self.speed = (self.speed[0], -self.speed[1])

        #P1 Collisions
        if (self.pos[1] + self.radius >= p1.pos[1] - p1.dims[1]//2 and \
            self.pos[1] - self.radius <= p1.pos[1] + p1.dims[1]//2): #Y
            if (self.pos[0] - self.radius <= p1.pos[0] + p1.dims[0]//2 and \
                self.pos[0] - self.radius >= p1.pos[0]): #X
                if (self.speed[0] < 0): #only change if moving towards P1
                    self.speed = (-self.speed[0], self.speed[0])

        #P2 Collisions
        if (self.pos[1] + self.radius >= p2.pos[1] - p2.dims[1]//2 and \
            self.pos[1] - self.radius <= p2.pos[1] + p2.dims[1]//2): #Y
            if (self.pos[0] + self.radius >= p2.pos[0] - p2.dims[0]//2 and \
                self.pos[0] + self.radius <= p2.pos[0]): #X
                if (self.speed[0] > 0): #only change if moving towards P2
                    self.speed = (-self.speed[0], self.speed[0])
    
    def update(self):
        self.pos = (int(self.pos[0] + self.speed[0]), \
                    int(self.pos[1] + self.speed[1]))

    def display(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

def main():
    pygame.init()
    pygame.display.set_caption("Pong")


    width = 1200#1500
    height = 800#900
    game = pygame.display.set_mode((width, height))
    
    #setup game
    borderThick = 10
    borderColor = (255,20,147)

    #P1 is controlled by WS, P2 controlled by UpDown
    p1color = (0,206,209)
    p2color = (255,69,0)
    ballColor = (255,255,255)
    speed = 4

    p1 = Player(width, height, 1, p1color)
    p2 = Player(width, height, 2, p2color)
    b = Ball(game, speed, 10, ballColor)

    running = True
    while running:
        pygame.time.delay(10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.fill((0,0,0))
        pygame.draw.line(game, borderColor, (0, 0), (width, 0), borderThick)
        pygame.draw.line(game, borderColor, (0, height), (width, height), borderThick)
        pygame.draw.line(game, borderColor, (0, 0), (0, height), borderThick)
        pygame.draw.line(game, borderColor, (width, 0), (width, height), borderThick)

        b.update()
        b.collisionDetected(game, borderThick, p1, p2)

        keys = pygame.key.get_pressed();
        if (keys[pygame.K_w]):
            p1.update(game, -speed)
        if (keys[pygame.K_s]):
            p1.update(game, speed)
        if (keys[pygame.K_UP]):
            p2.update(game, -speed)
        if (keys[pygame.K_DOWN]):
            p2.update(game, speed)
        if (keys[pygame.K_SPACE]):
            p1 = Player(width, height, 1, p1color)
            p2 = Player(width, height, 2, p2color)
            b = Ball(game, speed, 10, ballColor)


        b.display(game)
        p1.display(game)
        p2.display(game)
        pygame.display.update()

if __name__ == "__main__":
    main()