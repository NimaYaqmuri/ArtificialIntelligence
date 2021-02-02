import pygame
import numpy
import random
from board import Board

class SimulatedAnnealing:
    def __init__(self, board):
        self.board = board
        self.temperature = 100
        self.schedule = 0.9

    def schedule_function(self):
        self.temperature *= self.schedule

    def run(self):
        board_queens = self.board.queens[:]
        for i in range(100000):
            self.schedule_function()
            if self.temperature == 0:
                break;
            current_cost = Board.calculate_cost(board_queens)
            (index, value, next_cost) = Board.evaluate_function(board_queens)
            if next_cost < current_cost:
                Board.queen_movement(board_queens, index, value)
            else:
                (index, value) = Board.get_successor(board_queens)
                next_state = board_queens[:]
                Board.queen_movement(next_state, index, value)
                next_cost = Board.calculate_cost(next_state)
                x = numpy.random.uniform()
                tmp = numpy.exp((current_cost - next_cost)/self.temperature)
                print("tmp = ", tmp)
                if x < tmp:
                    board_queens = next_state[:]
            if current_cost == 0 or next_cost == 0:
                break;
        return board_queens
