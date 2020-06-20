import pygame
pygame.init()
window = pygame.display.set_mode((200, 200))
image = pygame.image.load('racecar.png').convert(24)
image.set_alpha(128)
window.fill((255,255,255))
window.blit(image, (0,0))
pygame.display.flip()

a=input()
