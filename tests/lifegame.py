"""
### Life Game Sample
"""

import random

import TkEasyGUI as eg

# Cell Status - ライフゲームのセルの状態
DEAD = 0
ALIVE = 1

# board rows and columns - ゲーム盤の行と列の数
ROWS = 30
COLS = 40


# ライフゲームのルールに基づいて次の世代の盤面を計算する関数
def calculate_next_generation(board):
    new_board = [[DEAD for _ in range(COLS)] for _ in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            neighbors = count_neighbors(board, i, j)
            if board[i][j] == ALIVE:
                if neighbors < 2 or neighbors > 3:
                    new_board[i][j] = DEAD
                else:
                    new_board[i][j] = ALIVE
            else:
                if neighbors == 3:
                    new_board[i][j] = ALIVE
    return new_board


# 指定されたセルの周囲の生存セルの数を数える関数
def count_neighbors(board, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < ROWS and 0 <= y + j < COLS:
                count += board[x + i][y + j]
    return count


# GUIを作成する関数
def create_gui(_board):
    layout = []
    for i in range(ROWS):
        row = []
        for j in range(COLS):
            row.append(
                eg.Text(
                    "", key=f"b{i}-{j}", size=(2, 1), pad=(0, 0), enable_events=True
                )
            )
        layout.append(row)

    window = eg.Window("Life Game", layout, row_padding=0, finalize=True)
    return window


# GUI上の盤面を更新する関数
def update_gui(window, board):
    for i in range(ROWS):
        for j in range(COLS):
            bg = "red" if board[i][j] == ALIVE else "black"
            window[f"b{i}-{j}"].update(background_color=bg)


# メイン関数
def main():
    # ゲーム盤の初期化
    board = [[random.choice([ALIVE, DEAD]) for _ in range(COLS)] for _ in range(ROWS)]
    window = create_gui(board)
    paused = False
    while True:
        event, _ = window.read(timeout=200 if not paused else None)
        if event == eg.WINDOW_CLOSED:
            break
        if event and isinstance(event, str) and event.startswith("b"):
            a = event[1:].split("-")
            x, y = int(a[0]), int(a[1])
            if board[x][y] == ALIVE:
                board[x][y] = DEAD
            else:
                board[x][y] = ALIVE
            update_gui(window, board)
        elif not paused:
            board = calculate_next_generation(board)
            update_gui(window, board)
    window.close()


if __name__ == "__main__":
    main()
