import math
import copy

def score(GameState , depth):
    if GameState.win("X"):
        return 10 - depth
    elif GameState.win("O"):
        return depth - 10
    else:
        return 0

def minimax(game, depth, counter=0):
    if game.over() or counter == depth:
        return (None, score(game, counter))
    if game.active_turn == "X":
        best_val = -math.inf
        best_move = None
        for move in game.get_available_moves():
            _, val = minimax(game.get_new_state(move), depth, counter + 1)
            if val > best_val:
                best_val = val
                best_move = move
        return (best_move, best_val)

    else:
        best_val = math.inf
        best_move = None
        for move in game.get_available_moves():
            _, val = minimax(game.get_new_state(move), depth, counter + 1)
            if val < best_val:
                best_val = val
                best_move = move
        return (best_move, best_val)
    
class GameState:
    def __init__(self, board=None, turn="X"):
        if board is None:
            self.board = [[None for _ in range(7)] for _ in range(6)]
        else:
            self.board = board
        self.active_turn = turn

    def get_available_moves(self):
        return [c for c in range(7) if self.board[5][c] is None]

    def get_new_state(self, move):
        new_board = copy.deepcopy(self.board)
        for r in range(6):
            if new_board[r][move] is None:
                new_board[r][move] = self.active_turn
                break
        new_turn = "O" if self.active_turn == "X" else "X"
        return GameState(new_board, new_turn)

    def win(self, player):
        for r in range(6):
            for c in range(7):
                if self.board[r][c] == player:
                    if c + 3 < 7 and all(self.board[r][c+i] == player for i in range(4)): return True
                    if r + 3 < 6 and all(self.board[r+i][c] == player for i in range(4)): return True
                    if r + 3 < 6 and c + 3 < 7 and all(self.board[r+i][c+i] == player for i in range(4)): return True
                    if r - 3 >= 0 and c + 3 < 7 and all(self.board[r-i][c+i] == player for i in range(4)): return True
        return False

    def over(self):
        return self.win("X") or self.win("O") or len(self.get_available_moves()) == 0
test_board = [[None for i in range(7)] for j in range(6)]
test_board[0][0], test_board[0][1], test_board[0][2], test_board[0][3], test_board[0][4], test_board[0][5], test_board[0][6]= "X", "O", "X", "O", "X", "X","O"
test_board[1][0], test_board[1][1], test_board[1][2], test_board[1][3] = "O","X", "O", "O"
test_board[2][0], test_board[2][2] = "O", "X"
test_board[3][2] = "X"
initial_game = GameState(test_board, "X")
bestmove,bestval=minimax(initial_game,4)
print("Best move for AI (X): Column ",bestval)
print("Predicted score: ", bestmove)