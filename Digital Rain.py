# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 19:55:03 2022

@author: Sandeep
"""

#To use this code, you should have pygame imported.
#To change the characters rendered change to desired characters in characters = ''
#To change the speed of the characters rendered, make changes to for i in range(350):
#To change the color of the characters, 

import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the window title
pygame.display.set_caption('Digital Rain')

# Load the Japanese font
font = pygame.font.Font('fonts/msjh.ttc', 18)

# Set the list of characters to use for the digital rain effect
characters = 'マトリックスはあなたを見ています'

# Set the starting position and velocity for each character
char_data = []
for i in range(350):
    x = random.randint(0, WINDOW_WIDTH)
    y = random.randint(-100, WINDOW_HEIGHT)
    vx = 0
    vy = random.uniform(1, 10)  # Change the speed of the characters
    brightness = random.uniform(0.7, 1.0)  # Add a brightness factor for each character
    char_data.append((x, y, vx, vy, brightness))

# Set the game clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Update the position of each character
    for i in range(len(char_data)):
        x, y, vx, vy, brightness = char_data[i]
        y += vy
        if y > WINDOW_HEIGHT:
            y = -100
            x = random.randint(0, WINDOW_WIDTH)
        char_data[i] = (x, y, vx, vy, brightness)
    
    # Draw each character on the screen
    for x, y, vx, vy, brightness in char_data:
        char = random.choice(characters)
        
        color = (0, 255, 0)
        text = font.render(char, True, color)
        screen.blit(text, (x, y))
    
    # Update the display
    pygame.display.update()
    
    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit pygame
pygame.quit()
