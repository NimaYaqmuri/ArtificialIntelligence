import pygame

GREEN = (25, 111, 61)
BLUE = (31, 97, 141)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TURQUOISE = (64, 224, 208)

class Cell:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.successors = []
		self.width = width
		self.total_rows = total_rows

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == BLUE

	def is_open(self):
		return self.color == TURQUOISE

	def is_wall(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == GREEN

	def is_end(self):
		return self.color == GREEN

	def reset(self):
		self.color = WHITE

	def make_start(self):
		self.color = GREEN

	def make_closed(self):
		self.color = BLUE

	def make_open(self):
		self.color = TURQUOISE

	def make_wall(self):
		self.color = BLACK

	def make_end(self):
		self.color = GREEN

	def make_path(self):
		self.color = GREEN

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def get_successors(self, grid):
		self.successors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall(): # DOWN
			self.successors.append(grid[self.row + 1][self.col])
			
		if self.row > 0 and not grid[self.row - 1][self.col].is_wall(): # UP
			self.successors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall(): # RIGHT
			self.successors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_wall(): # LEFT
			self.successors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False
