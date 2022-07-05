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

        def check_radar(self, degree, game_map):
            length = 0
            x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
            y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

            # searching for the longest distance to wall and traveling that direction
            while not game_map.get_at((x, y)) == border_color and length < 300:
                length += 1
                x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
                y = int(self.center[0] + math.sin(math.radians(360 - (self.angle + degree))) * length)

                dist = int(math.sqrt(math.pow(x - self.center[0], 2) + math.pow(y - self.center[1], 2)))
                self.radars.append([(x, y), dist])

        # setting speed @ 20 for first time, only with 4 or more output nodes allow speed to regulate itslef
        def update(self, game_map):
            if not self.speed:
                self.speed = 20
                self.speed = True

                # dont let car get closer than 20px to the border
                self.rotated_sprite = self.rotate_center(self.sprite, self.angle)
                self.position[0] += math.cos(math.radians(360 - self.angle)) * self.speed
                self.position[0] = max(self.position[0], 20)
                self.position[0] = min(self.position[0], width - 120)






