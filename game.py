# -- Pygame Game Template -- #

import pygame
import sys
import config  # Import the config module

# -- Initialize Function -- #
def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

# -- Events Function -- #
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

# -- Rectangle Function -- #
def draw_rectangle(screen, rect, color, thickness, border_radius):
    # --- Draw rect on window --- #
    pygame.draw.rect(screen, color, rect, thickness, border_radius)

# -- Circle Function -- #
def draw_circle(screen, center, radius, color, thickness):
    # --- Draw circle on window --- #
    pygame.draw.circle(screen, color, center, radius, thickness)

# -- Line Function -- #
def draw_line(screen, color, start_pos, end_pos, thickness):
    # --- Draw line on window --- #
    pygame.draw.line(screen, color, start_pos, end_pos, thickness)

# -- Poly Function -- #
def draw_poly(screen, color, points,thickness):
    # --- Draw polygon on window --- #
    pygame.draw.polygon(screen, color, points,thickness)

# -- Main Function -- #
def main():
    screen = init_game()
    clock = pygame.time.Clock()  # Initialize the clock here
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)  # Use color from config

        # --- Line Drawn --- #
        start_pos = [50, 50]
        end_pos = [500, 50]
        draw_line(screen, config.BLUE, start_pos, end_pos, 5)

        # --- Polygon Drawn --- #
        points = [(340, 250), #middle
                  (194, 429), #right
                  (15, 532)  #bottom
                    ]
        thickness = 0
        draw_poly(screen, config.RED, points,thickness)

        # --- Polygon Drawn 2 --- #
        points = [(657, 269), #top left
                  (499, 577), #bottom left
                  (374, 394)  #right
                    ]
        thickness = 3
        draw_poly(screen, config.GREEN, points,thickness)   

        # --- Polygon Drawn 3 --- #
        points = [(93, 249), #left
                  (257, 547), # bottom
                  (400, 2),  #top right
                  (200,300) #mid indent
                    ]
        thickness = 0
        draw_poly(screen, config.BLACK, points,thickness)    







        #-- other shapes --#
        while pygame.mouse.get_pressed()[0] == True:
            # --- Circle Drawn --- #
            circle_center = (380, 295)
            circle_radius = 200
            circle_color = config.RED
            circle_thick = 0
            draw_circle(screen, circle_center, circle_radius, circle_color, circle_thick)

            # --- Circle Drawn out line --- #
            circle_center = (380, 295)
            circle_radius = 200
            circle_color = config.BLACK
            circle_thick = 4
            draw_circle(screen, circle_center, circle_radius, circle_color, circle_thick)

            # --- Rectangle Drawn --- #
            my_rect1 = [230, 170, 300, 250]
            border_radius = 50
            thickness_r = 0
            draw_rectangle(screen, my_rect1, config.WHITE, thickness_r, border_radius)

            # --- Rectangle Drawn outline --- #
            my_rect1 = [230, 170, 300, 250]
            border_radius = 50
            thickness_r = 4
            draw_rectangle(screen, my_rect1, config.BLACK, thickness_r, border_radius)

            # --- triangle Drawn --- #
            points = [(340, 250), #top left
                      (340, 340), #bottom left
                      (430, 300)  #right
                      ]
            thickness = 0
            draw_poly(screen, config.RED, points,thickness)

            # --- triangle Drawn outline --- #
            points = [(340, 250), #top left
                      (340, 340), #bottom left
                      (430, 300)  #right
                      ]
            thickness = 4
            draw_poly(screen, config.BLACK, points,thickness)

        pygame.display.flip()

        # -- Limit the frame rate to the specified frames per second (FPS) -- #
        clock.tick(config.FPS)  # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
