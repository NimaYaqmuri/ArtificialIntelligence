import math

def who_is_next(state):
    x = 0
    o = 0
    for i in state:
        for j in i:
            if j == "X":
                x += 1
            if j == "O":
                o += 1
    return "O" if x > o else "X"

def result(state, successor):
    i, j = successor
    next_move = who_is_next(state)
    next_state = []
    for a in range(3):
        tmp = []
        for b in range(3):
            tmp.append(state[a][b])
        next_state.append(tmp)
    next_state[i][j] = next_move
    return next_state

def winner(state):
    rows = [[state[0][0], state[1][1], state[2][2]],
            [state[0][2], state[1][1], state[2][0]]]
    rows += state
    for i in range(3):
        rows.append([row[i] for row in state])
    for row in rows:
        current_palyer = row[0]
        if current_palyer != None and row.count(row[0]) == 3:
            return current_palyer
    return None

def successors(state):
    successor = set()
    for i, row in enumerate(state):
        for j , value in enumerate(row):
            if value == None:
                successor.add((i,j))
    return successor

def terminal_test(state):
    if winner(state) != None:
        return True
    if all(all(j != None for j in i) for i in state):
        return True
    return False

def utility(state):   
    win = winner(state)
    if win == "X":
        return 1
    elif win == "O":
        return -1
    else:
        return 0

def max_value(state, alpha, beta):
    if terminal_test(state) == True:
        return utility(state), None
    v = float("-inf")
    best = None
    for successor in successors(state):
        mn = min_value(result(state ,successor), alpha, beta)[0]
        if mn > v:
            best = successor
            v = mn     
        if v >= beta:
            return v, best
        alpha = max(alpha, v)
    return v, best

def min_value(state , alpha, beta):
    if terminal_test(state) == True:
        return utility(state), None
    v = float("inf")
    best = None
    for successor in successors(state):
        mx = max_value(result(state ,successor), alpha, beta)[0]
        if mx < v:
            best = successor
            v = mx 
        if (v <= alpha):
            return v, best
        beta = min(beta,v)
    return v, best

def alpha_beta_search(state):
    if who_is_next(state) == "X":
        return max_value(state ,float("-inf") ,float("inf"))[1]
    else:
        return min_value(state , float("-inf"), float("inf"))[1]
