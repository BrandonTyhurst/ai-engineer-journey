#This code was not written by me. I am using this file to practice my prompt engineering with ChatGPT
#I asked ChatGPT to create code for a TicTacToe game with an AI opponent to play against.
#I will resolve any part of the prompt as needed.

from __future__ import annotations
import math
import random
from typing import List, Optional, Tuple

Board = List[str]  # length 9, each is "X", "O", or " "


WIN_LINES: Tuple[Tuple[int, int, int], ...] = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def new_board() -> Board:
    return [" "] * 9


def print_board(b: Board) -> None:
    def cell(i: int) -> str:
        # Show position numbers for empty cells to help user pick
        return b[i] if b[i] != " " else str(i + 1)

    print("\n")
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")
    print("\n")


def winner(b: Board) -> Optional[str]:
    for a, c, d in WIN_LINES:
        if b[a] != " " and b[a] == b[c] == b[d]:
            return b[a]
    return None


def is_draw(b: Board) -> bool:
    return winner(b) is None and all(x != " " for x in b)


def available_moves(b: Board) -> List[int]:
    return [i for i, v in enumerate(b) if v == " "]


def make_move(b: Board, idx: int, player: str) -> None:
    if idx < 0 or idx >= 9:
        raise ValueError("Move out of range.")
    if b[idx] != " ":
        raise ValueError("Cell already taken.")
    b[idx] = player


def other(player: str) -> str:
    return "O" if player == "X" else "X"


def ask_choice(prompt: str, valid: List[str]) -> str:
    valid_lower = [v.lower() for v in valid]
    while True:
        s = input(prompt).strip().lower()
        if s in valid_lower:
            # return in original casing matching valid list
            return valid[valid_lower.index(s)]
        print(f"Please enter one of: {', '.join(valid)}")


def ask_move(b: Board) -> int:
    while True:
        s = input("Enter your move (1-9): ").strip()
        if not s.isdigit():
            print("Please enter a number 1-9.")
            continue
        move = int(s) - 1
        if move < 0 or move > 8:
            print("Please enter a number 1-9.")
            continue
        if b[move] != " ":
            print("That spot is taken. Choose another.")
            continue
        return move


def minimax(b: Board, current: str, ai: str, human: str, alpha: float, beta: float) -> Tuple[int, Optional[int]]:
    """
    Returns (score, best_move)
    score perspective: +1 AI win, -1 human win, 0 draw
    """
    w = winner(b)
    if w == ai:
        return (1, None)
    if w == human:
        return (-1, None)
    if is_draw(b):
        return (0, None)

    moves = available_moves(b)

    if current == ai:
        best_score = -math.inf
        best_move = None
        for m in moves:
            b[m] = current
            score, _ = minimax(b, human, ai, human, alpha, beta)
            b[m] = " "
            if score > best_score:
                best_score = score
                best_move = m
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return (int(best_score), best_move)
    else:
        best_score = math.inf
        best_move = None
        for m in moves:
            b[m] = current
            score, _ = minimax(b, ai, ai, human, alpha, beta)
            b[m] = " "
            if score < best_score:
                best_score = score
                best_move = m
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return (int(best_score), best_move)


def ai_move(b: Board, ai: str, human: str, difficulty: str) -> int:
    moves = available_moves(b)

    # Easy: 40% random, 60% best
    if difficulty == "Easy":
        if random.random() < 0.4:
            return random.choice(moves)

    # Hard (and the "best" part of Easy): minimax
    _, best = minimax(b, ai, ai, human, -math.inf, math.inf)
    return best if best is not None else random.choice(moves)


def play_game() -> None:
    print("=== Tic Tac Toe (You vs AI) ===")
    difficulty = ask_choice("Choose difficulty (Easy/Hard): ", ["Easy", "Hard"])
    human = ask_choice("Do you want to be X or O? (X goes first): ", ["X", "O"])
    ai = other(human)

    b = new_board()
    turn = "X"

    print("\nPositions are numbered 1-9 like this:")
    print_board(new_board())

    while True:
        print_board(b)

        w = winner(b)
        if w is not None:
            print(f"{w} wins! 🎉" if w == human else f"{w} wins! (AI got you) 🤖")
            break
        if is_draw(b):
            print("It's a draw! 🤝")
            break

        if turn == human:
            move = ask_move(b)
            make_move(b, move, human)
        else:
            print("AI is thinking...")
            move = ai_move(b, ai, human, difficulty)
            make_move(b, move, ai)
            print(f"AI played at position {move + 1}.")

        turn = other(turn)


def main() -> None:
    while True:
        play_game()
        again = ask_choice("Play again? (Y/N): ", ["Y", "N"])
        if again == "N":
            print("Goodbye!")
            return


if __name__ == "__main__":
    main()

#ChatGPT 5.2 Really nailed this first try. Super interactive and quick. 
    #Easy and Hard Mode 
    #Overall nicely done!