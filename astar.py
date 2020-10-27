import pygame
import math
from queue import PriorityQueue

SIDE = 800
win = pygame.display.set_mode((SIDE, SIDE))
pygame.display.set_caption("A* Path Finder")

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows
    
    def get_position(self)
        return self.row, self.col

    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQ
    
    def is_path(self):
        return self.color == PURPLE
    
    def reset(self):
        return self.color == WHITE