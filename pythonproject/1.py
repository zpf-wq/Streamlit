#import turtle

#bob=turtle.Turtle()
#def polygon(t,length,n):
    #for i in range(n):
        #t=turtle.fd(length)
        #t=turtle.lt(360/n)

#length=eval(input('输入长度'))
#n=eval(input('输入角度'))
#polygon(bob,length,n)
#工具和游戏主控
import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode(800,600)
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
                self.screen.fill(random.randint(0,255), random.randint(1,255), random.randint(0,255))
                pygame.display.update()
                self.clock.tick(60)


def main():
    game = tools.Game()
    game.run()


if __name__ == '_main_':
    main()
