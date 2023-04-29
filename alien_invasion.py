import sys

import pygame

class AlienInvasion:
    """Overall class to manage the game"""
    
    def __init__(self):
        """Initialize game and create resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (230, 230,230)

    def run_game(self):
        """Start the main game loop"""
        while True:
            # Watch the keyboard and mouse for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            
            # Display the screen
            pygame.display.flip()

if __name__ == "__main__":
    #Make an instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
