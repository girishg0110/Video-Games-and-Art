import pygame
import random

class Bullet():
    def __init__(self, playerObj, bulletSpeed, bulletColor):
        self.speed = bulletSpeed
        self.color = bulletColor
        self.pos = (playerObj.pos[0], playerObj.pos[1])
        self.dims = (playerObj.dims[1]//4, 2*playerObj.dims[1]//3)

    def update(self):
        self.pos = (self.pos[0], self.pos[1] - self.speed)

    def offScreen(self, screenDims):
        return self.pos[1] + self.dims[1]//2 <= 0

    def display(self, surface):
        pygame.draw.rect(surface, self.color, (self.pos[0] - self.dims[0]//2, self.pos[1] - self.dims[1]//2, self.dims[0], self.dims[1]))


class Player():
    def __init__(self, dims, windowDims, color):
        self.pos = (windowDims[0]//2, 7*windowDims[1]//8) #top vertex
        self.dims = dims #(base, height)
        self.color = color

    def update(self, xPos):
        self.pos = (xPos, self.pos[1])

    def destroyed(self, enemy):
        if (self.pos[0] + self.dims[0]//2 >= enemy.pos[0] - enemy.sideLength//2 and \
            self.pos[0] - self.dims[0]//2 <= enemy.pos[0] + enemy.sideLength//2): #X
            return (self.pos[1] - self.dims[1]//2 <= enemy.pos[1] + enemy.sideLength//2)
        return False

    def display(self, screen):
        pygame.draw.polygon(screen, self.color, (self.pos, \
            (self.pos[0] - self.dims[0]//2, self.pos[1] + self.dims[1]), \
            (self.pos[0] + self.dims[0]//2, self.pos[1] + self.dims[1])))

class Enemy():
    def __init__(self, screenDims, playerDims, maxSpeed):
        self.sideLength = playerDims[1]
        self.pos = (random.randint(self.sideLength, screenDims[0] - self.sideLength), -self.sideLength)
        self.color = randColor()
        self.dropSpeed = 0.5 + random.random() * (maxSpeed - 0.5) #refine

    def update(self):
        self.pos = (self.pos[0], self.pos[1] + self.dropSpeed)

    def destroyed(self, bullet):
        if (self.pos[0] + self.sideLength//2 >= bullet.pos[0] - bullet.dims[0]//2 and \
            self.pos[0] - self.sideLength//2 <= bullet.pos[0] + bullet.dims[0]//2): #X
            if (self.pos[1] + self.sideLength//2 >= bullet.pos[1] + bullet.dims[1]//2):
                return True

        return False

    def offScreen(self, screenDims):
        return self.pos[1] - self.sideLength >= screenDims[1]

    def display(self, surface):
        pygame.draw.rect(surface, self.color, \
            (self.pos[0] - self.sideLength//2, int(self.pos[1] - self.sideLength//2), \
            self.sideLength, self.sideLength))


def randColor(realRandom = False):
    if (realRandom == True):
        return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    x = random.randint(0,9)
    if (x == 1): #RED
        return (255,0,0)
    if (x == 2): #ORANGE
        return (255,127,0)
    if (x == 3): #YELLOW
        return (255,255,0)
    if (x == 4): #GREEN
        return (0,255,0)
    if (x == 5): #BLUE
        return (0,0,255)
    if (x == 6): #INDIGO
        return (75,0,130)
    if (x == 7): #VIOLET
        return (139,0,255)
    if (x == 8): #PINK
        return (255,20,147)
    if (x == 9): #BROWN
        return (139,69,19)
    if (x == 0): #WHITE
        return (255,255,255)
    return color

def main():
    pygame.init()
    pygame.display.set_caption("Galaxo")

    gameDims = (1000,800)
    game = pygame.display.set_mode(gameDims)

    playerDims = (60,40)
    playerColor = (255,0,0)
    lives = 15
    score = 0
    galax = Player(playerDims, gameDims, playerColor)

    enemyArray = []
    numEnemies = 10
    maxSpeed = 8
    for x in range (0, numEnemies - 1):
        enemyArray.append(Enemy(gameDims, playerDims, maxSpeed))

    bulletArray = []
    bulletSpeed = 4
    bulletColor = (255,0,0)
    numBullets = numEnemies

    paused = True
    gameOver = False
    running = True
    while running:
        pygame.time.delay(10)
        game.fill((0,0,0))
        if (gameOver):            
            font = pygame.font.SysFont('impact', min(gameDims[1],gameDims[0])//6)
            doneRect = (gameDims[0]//4,gameDims[1]//4,gameDims[0]//2,gameDims[1]//2)
            
            pygame.draw.circle(game, (255,255,255), (gameDims[0]//6,gameDims[1]//6), 1)
            pygame.draw.circle(game, (255,255,255), (5*gameDims[0]//6,5*gameDims[1]//6), 1)

            text = font.render('GAME OVER', True, (255,255,255))
            game.blit(text, doneRect)
            pygame.display.update()
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_SPACE]):
                paused = not paused
            if (paused):
                continue

            if (pygame.mouse.get_pressed()[0]):
                if (len(bulletArray) < numBullets):
                    bulletArray.append(Bullet(galax, bulletSpeed, bulletColor))
                        
        for x in enemyArray:
            if (not paused):
                x.update()
                if (x.offScreen(gameDims)):
                    enemyArray.remove(x)
                    enemyArray.append(Enemy(gameDims, playerDims, maxSpeed))
                    lives = lives - 1
                    if (lives == 0):
                        gameOver = True
                    continue
                for i in bulletArray:
                    if (x.destroyed(i)):
                        enemyArray.remove(x)
                        enemyArray.append(Enemy(gameDims, playerDims, maxSpeed))
                        bulletArray.remove(i)
                        score = score + 1
                        break
                if (galax.destroyed(x)):
                    enemyArray.remove(x)
                    enemyArray.append(Enemy(gameDims, playerDims, maxSpeed))
                    lives = lives - 1
                    if (lives == 0):
                        gameOver = True
            x.display(game)

        for x in bulletArray:
            if (not paused):
                x.update()
                if (x.offScreen(gameDims)):
                    bulletArray.remove(x)
                    continue
            x.display(game)

        galax.update(pygame.mouse.get_pos()[0])
        galax.display(game)
        pygame.display.flip()
    print(score)
    finalRun = True
    while finalRun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finalRun = False
                break

if __name__ == "__main__":
    main()