import pygame
import math
from queue import PriorityQueue
from cell import Cell

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

def astar(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {cell: float("inf") for row in grid for cell in row}
	g_score[start] = 0
	f_score = {cell: float("inf") for row in grid for cell in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		current = open_set.get()[2]
		open_set_hash.remove(current)
		if current == end:
			reconstruct_path(came_from, end, draw)
			start.make_start()
			end.make_end()
			return True
		for successor in current.successors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[successor]:
				came_from[successor] = current
				g_score[successor] = temp_g_score
				f_score[successor] = temp_g_score + h(successor.get_pos(), end.get_pos())
				if successor not in open_set_hash:
					count += 1
					open_set.put((f_score[successor], count, successor))
					open_set_hash.add(successor)
					successor.make_open()
		draw()
		if current != start:
			current.make_closed()
	return False
