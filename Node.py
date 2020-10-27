import pygame
from colors import RED, GREEN, BLUE, YELLOW, WHITE, BLACK, PURPLE, ORANGE, GREY, TURQ

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
    
    def get_position(self):
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
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQ

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbours(self, grid):
        self.neighbours = []
        #Check bottom neighbour
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
                 self.neighbours.append(grid[self.row + 1][self.col])
        #Check top neighbour
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
                 self.neighbours.append(grid[self.row - 1][self.col])
        #Check right neighbour
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
                 self.neighbours.append(grid[self.row][self.col + 1])
        #Check right neighbour
        if self.col < self.total_rows + 1 and not grid[self.row][self.col - 1].is_barrier():
                 self.neighbours.append(grid[self.row][self.col - 1])
        pass
    
    def __lt__(self, other):
        return False