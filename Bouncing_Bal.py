import pygame
import time

pygame.init()

WIDTH, HEIGHT = 400, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
SURFACE = pygame.Rect(0,0,WIDTH,HEIGHT)
BLACK = 0, 0, 0

pygame.display.set_caption("Bounce that Ball")

BALL = pygame.transform.scale(
    pygame.image.load('assets/Red-Ball.png'), (50, 50))

class Ball:
    def __init__(self, size, weight, elastisity):
        self.size = size
        self.weight = weight
        self.elastisity = elastisity

def draw_window(ball):

    pygame.draw.rect(WIN, BLACK, SURFACE)
    WIN.blit(BALL, (ball.x, ball.y))







        

def main():

    

    ball = pygame.Rect(WIDTH/2 - 25, 10, 50,50)
    
    ball_movment = 0

    clock = pygame.time.Clock()
    run = True

    while run:
        t = pygame.time.get_ticks()/1000
        gravity = (9.81*t**2/2)

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                 

        ball_movment += gravity
        ball.bottom += ball_movment

        if ball.bottom >= HEIGHT:
            ball_movment = -ball_movment
            t = 0
            gravity = 0
       
        print(gravity)


        draw_window(ball)
        pygame.display.update()


    


        


if __name__ == "__main__":
    main()
