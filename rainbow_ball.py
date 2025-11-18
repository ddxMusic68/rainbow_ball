from physics_pygame import *
from rbg import rgb_rainbow
pygame.init()



def mainloop():
    ball1 = Ball(retention=1.01, friction=1, x_speed=-10, x_pos=1000-50)
    # ball2 = Ball(retention=.99, friction=1, x_speed=20)
    WIDTH, HEIGHT = 1000, 600
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    GRAVITY = 0.3
    FPS = 60

    clock = pygame.time.Clock()

    rgbframe = 0
    color = (255, 0, 0)

    grow = True

    run = True
    while run:
        rgbframe += 5
        rgbframe = rgbframe % 1020
        color = rgb_rainbow(rgbframe)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        
        # window.fill('black')
        
        for ball in Ball.ball_list:
            ball_bounce(ball, WIDTH, HEIGHT)
            if ball.radius >= HEIGHT//2 and grow:
                grow = False
            elif ball.radius < 5 and not grow:
                grow = True
            if grow:
                ball.radius += 0.02
            else: 
                ball.radius -= 0.02
            ball.color = color
            ball.update_gravity(GRAVITY)
            ball.update_position()
            ball.collide_mouse(mouse_pos, left_click)
            ball.draw(window)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    mainloop()