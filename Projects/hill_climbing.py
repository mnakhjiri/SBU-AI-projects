import random


def get_neighbours(queens_board: list):
    result = []
    for i in range(len(queens_board)):
        for j in range(i + 1, len(queens_board)):
            neighbour = queens_board[:]
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
            result.append(neighbour)
    return result


def get_point(board: list):
    point = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if i != j:
                if abs(board[i] - board[j]) == abs(i - j):
                    point -= 1
    return point


def hill_climbing_stochastic(queens_board: list, n: int):
    for i in range(n):
        neighbours = get_neighbours(queens_board)
        neighbours_points = [get_point(neighbour) for neighbour in neighbours]
        neighbours_points = [point + 28 for point in neighbours_points]
        result_array = []
        for i in range(len(neighbours_points)):
            result_array += [neighbours[i]] * neighbours_points[i]
        queens_board = random.choice(result_array)
    return queens_board


def hill_climbing(queens_board: list):
    while True:
        neighbours = get_neighbours(queens_board)
        queens_board_point = get_point(queens_board)
        winner_neighbour = None
        for neighbour in neighbours:
            neighbour_point = get_point(neighbour)
            if neighbour_point > queens_board_point:
                queens_board_point = neighbour_point
                winner_neighbour = neighbour
        if winner_neighbour is None:
            break
        queens_board = winner_neighbour
    return queens_board


best_boards = []


def get_best_boards():
    queens_board = [i for i in range(8)]
    random.shuffle(queens_board)
    result = hill_climbing(queens_board)
    best_boards.append((get_point(result), result))


best_boards_stochastic = []


def get_best_boards_stochastic():
    queens_board = [i for i in range(8)]
    random.shuffle(queens_board)
    result = hill_climbing_stochastic(queens_board, 50)
    best_boards_stochastic.append((get_point(result), result))


# normal mode

print("normal mode")
for i in range(1000):
    get_best_boards()
best_boards.sort(reverse=True)
# getting the best 3 boards
for i in range(3):
    print(best_boards[i])

# stochastic mode

for i in range(100):
    get_best_boards_stochastic()
best_boards_stochastic.sort(reverse=True)
# getting the best 3 boards

print("\nstochastic mode")
for i in range(3):
    print(best_boards_stochastic[i])
