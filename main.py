import pygame

print('Setup Start')
pygame.init()

window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')

while True:
    # check for all Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close Windows
            quit()  # end pygame
