import pygame as pg

pg.init()

# Set up display
background_colour = (250, 250, 250)
screen = pg.display.set_mode((800, 800))
pg.display.set_caption('Driver Environment') 

# Define our cars properties
car_x_cor = 400
car_y_cor = 760
car_width = 30
car_height = 60
car_color = (150, 150, 150)
speed = 0.25


running = True
while running: 
    screen.fill(background_colour)
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:  # Move right
        car_x_cor += speed
    if keys[pg.K_LEFT]:   # Move left
        car_x_cor -= speed
    if keys[pg.K_UP]:     # Move up
        car_y_cor -= speed
    if keys[pg.K_DOWN]:   # Move down
        car_y_cor += speed

    pg.draw.rect(screen, car_color, (car_x_cor, car_y_cor, car_width, car_height))

    pg.display.flip()

pg.quit()