import pygame
import math
from queue import PriorityQueue
from cell import Cell
import algorithm

pygame.display.set_caption("Maze Problem _ A* algorithm")
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
ROWS = 20

WHITE = (255, 255, 255)
GREY = (128, 128, 128)

def draw_grid(win, rows, width):
		gap = width // rows
		for i in range(rows):
			pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
			for j in range(rows):
				pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
	win.fill(WHITE)
	for row in grid:
		for cell in row:
			cell.draw(win)
	draw_grid(win, rows, width)
	pygame.display.update()

def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos
	row = y // gap
	col = x // gap
	return row, col

def maze_world(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			cell = Cell(i, j, gap, rows)
			grid[i].append(cell)
	return grid

def main(win, width, rows):
	grid = maze_world(rows, width)
	start = None
	end = None
	run = True
	while run:
		draw(win, grid, rows, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, rows, width)
				cell = grid[row][col]
				if not start and cell != end:
					start = cell
					start.make_start()
				elif not end and cell != start:
					end = cell
					end.make_end()
				elif cell != end and cell != start:
					cell.make_wall()
			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, rows, width)
				cell = grid[row][col]
				cell.reset()
				if cell == start:
					start = None
				elif cell == end:
					end = None
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for cell in row:
							cell.get_successors(grid)
					algorithm.astar(lambda: draw(win, grid, rows, width), grid, start, end)
				if event.key == pygame.K_c:
					start = None
					end = None
					grid = maze_world(rows, width)
	pygame.quit()

main(WIN, WIDTH, ROWS)
