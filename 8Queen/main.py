import pygame
from board import Board
from algorithm import SimulatedAnnealing

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_board(the_board):
    pygame.init()
    pygame.display.set_caption("B) 8-Queens Problem _ simulated annealing")
    colors = [WHITE, BLACK]
    n = len(the_board)
    surface_size = 800
    square_size = surface_size // n
    surface_size = n * square_size
    surface = pygame.display.set_mode((surface_size, surface_size))
    ball = pygame.image.load("Queen.png")
    ball_offset = (square_size - ball.get_width()) // 2
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break;
        for row in range(n):
            c_index = row % 2
            for col in range(n):
                the_square = (col * square_size, row * square_size, square_size, square_size)
                surface.fill(colors[c_index], the_square)
                c_index = (c_index + 1) % 2
        for (col, row) in enumerate(the_board):
            surface.blit(ball, (col * square_size + ball_offset, row * square_size + ball_offset))
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    board = Board(8)
    draw_board(SimulatedAnnealing(board).run())
