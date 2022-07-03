import math
import random
import sys
import os
import neat
import pygame

width = 1920
height = 1080

car_size_x = 60
car_size_y = 60

border_color = (255, 255, 255, 255)  # Color in case of crash

current_generation = 0  # Generation counter


class Car:

    def __innit(self):
        # Loading car image and adding rotation and sprite
        self.sprite = pygame.image.load('car.png').convert()
        self.sprite = pygame.transform.scale(self.sprite, (car_size_x, car_size_y))
        self.rotated_sprite = self.sprite

        # Adding starting position(Depending on the map)
        self.position = [830, 920]
        self.angle = 0
        self.speed = 0

        self.speed_set = False

        self.center = [self.position[0] + car_size_x / 2,
                       self.position[1] + car_size_y / 2]  # Calculate center of the car

        self.radars = []  # Using list for radars
        self.drawing_radars = []  # Radars to be drawn

        self.alive = True  # Checking if car has crashed

        self.distance = 0  # Recording distance traveled
        self.time = 0  # Recording time spent driving

        def draw(self, screen):
            screen.blit(self.rotated_sprite, self.position)
            self.draw_radar(screen)

        def draw_radar(self, screen):
            for radar in self.radars:
                position = radar[0]
                pygame.draw.line(screen, (0, 255, 0), self.center, position, 1)
                pygame.draw.circle(screen, (0, 255, 0), position, 5)

        def check_collision(self, game_map):
            self.alive = True
            for point in self.corners:
                # if any corner of the car touches the border color == Crash
                if game_map.get_at(int(point[0]), int(point[1])) == border_color:
                    self.alive = False
                    break
