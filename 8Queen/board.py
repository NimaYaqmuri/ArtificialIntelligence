import random

class Board:
    def __init__(self, queen_count=8):
        self.queen_count = queen_count
        self.queens = [-1 for i in range(0, self.queen_count)]
        for i in range(0, self.queen_count):
            self.queens[i] = random.randint(0, self.queen_count - 1)
        
    @staticmethod
    def calculate_cost(queens):
        threat = 0
        queen_count = len(queens)
        for queen in range(0, queen_count - 1):
            for next_queen in range(queen + 1, queen_count):
                if queens[queen] == queens[next_queen] or abs(queen - next_queen) == abs(queens[queen] - queens[next_queen]):
                    threat += 1
        return threat

    @staticmethod
    def get_successor(queens):
        queen_count = len(queens)
        index = random.randint(0, queen_count - 1)
        value = random.randint(0, queen_count - 1)
        while queens[index] == value:
            value = random.randint(0, queen_count - 1)
        return (index, value)

    @staticmethod
    def evaluate_function(queens):
        x, y = -1, -1
        best = 100000
        queen_count = len(queens)
        for j in range(queen_count):
            tmp = queens[j]
            for i in range(queen_count):
                if i != queens[j]:
                    queens[j] = i
                    cost = Board.calculate_cost(queens)
                    if cost < best:
                        best = cost
                        x = i
                        y = j
            queens[j] = tmp
        return y, x, best

    @staticmethod
    def queen_movement(queens, index, value):
        queens[index] = value
        return queens
