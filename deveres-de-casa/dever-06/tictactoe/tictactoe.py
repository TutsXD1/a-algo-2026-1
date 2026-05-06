"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Conta quantos 'X' e 'O' estão no tabuleiro
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # X sempre joga primeiro. Se tiverem a mesma quantidade ou o tabuleiro estiver vazio, é a vez de X.
    if x_count <= o_count:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Ação inválida: esta célula não está disponível.")

    # deepcopy
    new_board = copy.deepcopy(board)
    current_player = player(board)
    new_board[action[0]][action[1]] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checking rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Checking columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Checking diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # End if find a winner
    if winner(board) is not None:
        return True

    # Or no more empty spaces
    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_player = winner(board)
    if win_player == X:
        return 1
    elif win_player == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if board == initial_state():
        return (1, 1)

    current_player = player(board)

    # Se for a vez do X, queremos maximizar o valor (buscar o 1)
    if current_player == X:
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            action_value = _min_value(result(board, action))
            if action_value > best_value:
                best_value = action_value
                best_action = action
        return best_action

    # Se for a vez do O, queremos minimizar o valor (buscar o -1)
    else:
        best_value = math.inf
        best_action = None
        for action in actions(board):
            action_value = _max_value(result(board, action))
            if action_value < best_value:
                best_value = action_value
                best_action = action
        return best_action


# --- Funções Auxiliares para o Minimax ---

def _max_value(board):
    """ Retorna o maior valor possível para o jogador X """
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    for action in actions(board):
        v = max(v, _min_value(result(board, action)))
    return v


def _min_value(board):
    """ Minimiza o valor para o jogador O """
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        v = min(v, _max_value(result(board, action)))
    return v