import pygame
import math
from queue import PriorityQueue
from Node import Node

SIDE = 800
win = pygame.display.set_mode((SIDE, SIDE))
pygame.display.set_caption("A* Path Finder")


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return abs(x2 - x1) + abs(y2 - y1)

def gen_grid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    
    return grid