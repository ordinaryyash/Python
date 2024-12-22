import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 450, 450
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
RADIUS = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hybrid Clock")
font = pygame.font.SysFont("Arial", 18)

def draw_number_hand(angle, length, number):
    angle = math.radians(angle - 90)
    x = CENTER_X + math.cos(angle) * length
    y = CENTER_Y + math.sin(angle) * length
    text = font.render(str(number), True, (0, 0, 255))
    screen.blit(text, (x - 10, y - 10))  # Centering the text:/

# Mainloop
running = True
while running:
    screen.fill((255, 255, 255))

    #clock_ka_face
    pygame.draw.circle(screen, (0, 0, 0), (CENTER_X, CENTER_Y), RADIUS, 2)
    
    for i in range(12):
        angle = math.radians(i * 30)
        x = CENTER_X + math.cos(angle) * (RADIUS - 30)
        y = CENTER_Y + math.sin(angle) * (RADIUS - 30)
        number = str(i if i != 0 else 12)
        text = font.render(number, True, (0, 0, 0))  # Black color for the numbers
        screen.blit(text, (x - 10, y - 10))  # Center the text

    #current time
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
  
#movement of hands
    hour_angle = (hour % 12 + minute / 60) * 30  # Hour_hand
    minute_angle = (minute + second / 60) * 6  # Minute_hand 
    second_angle = second * 6  # Second_hand


    draw_number_hand(hour_angle, 100, f"{hour}".rjust(2, "0"))
    draw_number_hand(minute_angle, 150, f"{minute}".rjust(2, "0"))
    draw_number_hand(second_angle, 180, f"{second}".rjust(2, "0"))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.Clock().tick(60)

pygame.quit()
