import pygame

class Ship:
    # a class to manage the shp.

    def __init__(self, ai_game):
        #initialize the ship and set its starting position.
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the ship image and get its rect.
        self.image = pygame.image.load ('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (100,100))
        # Start each new ship at the bottom center of the screen.

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a float for the ship's exact horizontal postiion.
        self.x = float(self.rect.x)

        #Movement Flag; start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False
    def update (self):
        #Update the ship's position based on the movement flag.
        #update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)
        