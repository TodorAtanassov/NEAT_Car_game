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
