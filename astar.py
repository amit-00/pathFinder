import math
import pygame
from queue import PriorityQueue
from Node import Node
from colors import GREY, WHITE

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

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows

    y, x = pos
    row = y // gap
    col = x // gap

    return row, col

def main(win, width):
    ROWS = 50
    grid = gen_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                
                if not start:
                    start = node
                    start.make_start()

                elif not end:
                    end = node
                    node.make_end()

                elif node != start and node != end:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pass

    pygame.quit()

main(win, SIDE)
