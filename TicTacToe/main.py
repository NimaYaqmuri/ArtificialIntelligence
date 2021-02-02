import pygame
import sys
import algorithm

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.display.set_caption("C) Tic-Tac-Toe Game _ Alpha-Beta Pruning")
WIDTH = 400
SCREEN = pygame.display.set_mode((WIDTH, WIDTH))
FONT = pygame.font.SysFont("arial", 60)

def main(symbol):
    state = [[None, None, None],
            [None, None, None],
            [None, None, None]]
    computer_turn = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        SCREEN.fill(WHITE)
        house_size = 80
        house_center = (WIDTH / 2 - (1.5 * house_size), WIDTH / 2 - (1.5 * house_size))
        houses = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(house_center[0] + j * house_size, house_center[1] + i * house_size, house_size, house_size)
                pygame.draw.rect(SCREEN, BLACK, rect, 3)
                if state[i][j] != None:
                    move = FONT.render(state[i][j], True, BLACK)
                    move_rectangle = move.get_rect()
                    move_rectangle.center = rect.center
                    SCREEN.blit(move, move_rectangle)
                row.append(rect)
            houses.append(row)
        game_over = algorithm.terminal_test(state)
        player = algorithm.who_is_next(state)

        title = ""
        if game_over:
            winner = algorithm.winner(state)
            if winner is None:
                title = "Tie"
            else:
                title = f"{winner} wins"
        title = FONT.render(title, True, BLACK)
        title_rectangle = title.get_rect()
        title_rectangle.center = ((WIDTH / 2), 30)
        SCREEN.blit(title, title_rectangle)

        if symbol != player and not game_over:
            if computer_turn:
                move = algorithm.alpha_beta_search(state)
                state = algorithm.result(state, move)
                computer_turn = False
            else:
                computer_turn = True

        if pygame.mouse.get_pressed()[0] and symbol == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if (state[i][j] == None and houses[i][j].collidepoint(mouse)):
                        state = algorithm.result(state, (i, j))
        pygame.display.flip()
main("O")
