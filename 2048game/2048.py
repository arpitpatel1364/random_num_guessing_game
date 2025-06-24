from game2048 import start_game, move_up, move_down, move_left, move_right, add_new_2, get_current_state

def print_grid(mat):
    for row in mat:
        print(row)
    print()

# Start the game
grid = start_game()
print_grid(grid)

while True:
    move = input("Enter move (W/A/S/D): ").lower()

    if move == 'w':
        grid, changed = move_up(grid)
    elif move == 's':
        grid, changed = move_down(grid)
    elif move == 'a':
        grid, changed = move_left(grid)
    elif move == 'd':
        grid, changed = move_right(grid)
    else:
        print("Invalid input! Use W/A/S/D.")
        continue

    if changed:
        add_new_2(grid)
        print_grid(grid)
        status = get_current_state(grid)
        print("Game Status:", status)
        if status != 'GAME NOT OVER':
            break
    else:
        print("Move not possible. Try a different direction.")
