from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

def is_winner(board, player):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[i]==board[j]==board[k]==player for i,j,k in wins)

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for i, j, k in wins:
        if board[i] and board[i] == board[j] == board[k]:
            return board[i], [i, j, k]
    return None, []

def minimax(board, is_max):
    if is_winner(board, "O"): return 1, 1
    if is_winner(board, "X"): return -1, 1
    if "" not in board: return 0, 1

    best = float('-inf') if is_max else float('inf')
    total_nodes = 0

    for i in range(9):
        if board[i] == "":
            board[i] = "O" if is_max else "X"
            score, nodes = minimax(board, not is_max)
            board[i] = ""
            total_nodes += nodes
            best = max(best, score) if is_max else min(best, score)

    return best, total_nodes + 1

def alpha_beta(board, is_max, alpha, beta):
    if is_winner(board, "O"): return 1, 1
    if is_winner(board, "X"): return -1, 1
    if "" not in board: return 0, 1

    best = float('-inf') if is_max else float('inf')
    total_nodes = 0

    for i in range(9):
        if board[i] == "":
            board[i] = "O" if is_max else "X"
            score, nodes = alpha_beta(board, not is_max, alpha, beta)
            board[i] = ""
            total_nodes += nodes

            if is_max:
                best = max(best, score)
                alpha = max(alpha, best)
            else:
                best = min(best, score)
                beta = min(beta, best)

            if beta <= alpha:
                break

    return best, total_nodes + 1

def best_move(board, algo, player):
    is_max = player == "O"
    best_score = float('-inf') if is_max else float('inf')
    move = None
    total_nodes = 0
    start = time.time()

    for i in range(9):
        if board[i] == "":
            board[i] = player
            if algo == "minimax":
                score, nodes = minimax(board, not is_max)
            else:
                score, nodes = alpha_beta(board, not is_max, float('-inf'), float('inf'))
            board[i] = ""
            total_nodes += nodes

            if (is_max and score > best_score) or (not is_max and score < best_score):
                best_score = score
                move = i

    time_taken = round((time.time() - start) * 1000, 2)
    return move, time_taken, total_nodes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    data = request.get_json()
    board = data["board"]
    algo = data["algo"]
    player = data.get("player", "O")

    move = -1
    time_taken = 0
    nodes = 0

    if player == "O":
        move, time_taken, nodes = best_move(board, algo, player)
        if move is not None and move != -1:
            board[move] = player


    winner, combo = check_winner(board)
    draw = "" not in board and winner is None

    return jsonify({
        "move": move,
        "time": time_taken,
        "nodes": nodes,
        "winner": winner if winner else "",
        "draw": draw,
        "combo": combo
    })

@app.route("/aivsai", methods=["POST"])
def ai_vs_ai():
    data = request.get_json()
    board = data["board"]
    turn = data["turn"]
    algo = "minimax" if turn == "X" else "alphabeta"

    move, time_taken, nodes = best_move(board, algo, turn)
    if move is not None and move != -1:
        board[move] = turn


    winner, combo = check_winner(board)
    draw = "" not in board and winner is None

    return jsonify({
        "move": move,
        "time": time_taken,
        "nodes": nodes,
        "turn": turn,
        "winner": winner if winner else "",
        "draw": draw,
        "combo": combo
    })

if __name__ == "__main__":
    app.run(debug=True)
