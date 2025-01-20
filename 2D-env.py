import pygame as pg

# Initialize Pygame
pg.init()

background_colour = (250, 250, 250)
screen = pg.display.set_mode((800, 800))
pg.display.set_caption('Environment') 

class Car():
    def __init__(self):
        self.x_cor = 0
        self.y_cor = 0
        self.width = 30
        self.height = 60
        self.color = (150, 150, 150)
        self.speed = 0.3
    
    def update(self, keys):
        if keys[pg.K_RIGHT]:  # Move right
            self.x_cor += self.speed
        if keys[pg.K_LEFT]:   # Move left
            self.x_cor -= self.speed
        if keys[pg.K_UP]:     # Move up
            self.y_cor -= self.speed
        if keys[pg.K_DOWN]:   # Move down
            self.y_cor += self.speed

    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x_cor, self.y_cor, self.width, self.height))
    
car = Car()
# Game loop
running = True
while running: 
    screen.fill(background_colour) 

    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False

    # Get pressed keys
    keys = pg.key.get_pressed()
    if (keys):
        car.update(keys)

    car.draw(screen)
    pg.display.flip()

pg.quit()