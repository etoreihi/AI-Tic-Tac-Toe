# Tic-Tac-Toe with AI

## Overview

This project is a web-based Tic Tac Toe game that lets users either play interactively as a **human vs AI**, or run an **AI vs AI** match with two algorithms competing against each other. The AI uses adversarial search strategies, **Minimax** and **Alpha-Beta Pruning**, to make optimal moves. The game also tracks algorithm performance metrics, such as decision time and nodes evaluated.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Algorithm:** Minimax and Alpha-Beta Pruning

## Features

- 🎮 Human vs AI gameplay mode
- 🤖 AI vs AI mode with selectable algorithm for each player
- ⏱️ Timer to show AI move computation time
- 📊 Node counter for performance analysis
- 🏆 Dynamic scoreboard tracking wins, losses, draws
- ✨ Win-line animation on victory
- 🔄 Turn indicator with colored X and O

## Algorithms Used

### Minimax

A standard adversarial search algorithm that explores the entire game tree to determine the optimal move for the current player, assuming both players play optimally.

### Alpha-Beta Pruning

An optimized version of Minimax that prunes branches that cannot affect the final decision, resulting in faster computation. Alpha and Beta values are used to track the minimum and maximum scores the players are guaranteed.

**Both algorithms are deterministic and guarantee optimal play.**

## Key Implementation Highlights

- The frontend is implemented using semantic HTML and styled with CSS. JavaScript handles game logic and stat tracking.
- The Flask backend handles the AI logic, executing the selected algorithm and returning the AI's move, computation time, and node count.
- A stats display shows the algorithm used, total decision time, number of moves made, and average decision speed for both X and O.

## How to Run

1. Make sure Python 3 is installed on your system.

2. Install the required libraries:
```bash
pip install flask
```

3. Open a terminal and navigate to the project folder.

4. Run the application using:
```bash
python app.py
```

5. Open your browser and go to:
```
http://127.0.0.1:5000
```
Or the URL provided in the terminal.

## Game Modes

### Human vs AI
Choose your preferred difficulty by selecting either Minimax or Alpha-Beta Pruning algorithm. Challenge yourself against optimal AI play!

### AI vs AI
Watch two AI algorithms compete against each other. Compare the performance metrics between Minimax and Alpha-Beta Pruning to see the efficiency gains from pruning.

## Performance Metrics

The game tracks and displays:
- **Decision Time:** How long each AI takes to compute its move
- **Nodes Evaluated:** Number of game states explored
- **Average Speed:** Mean decision time across all moves
- **Move Count:** Total moves made by each player
