import random

def create_board(num_players, num_ladders):
    # Initialize the board with empty connections
    board = [[] for _ in range(num_players)]
    
    for _ in range(num_ladders):
        p1 = random.randint(0, num_players - 2)
        p2 = p1 + 1
        # Ensure no duplicate connections
        if p2 not in board[p1]:
            board[p1].append(p2)
            board[p2].append(p1)

    return board

def display_board(board, num_players):
    print("P1  P2  P3  P4  P5")
    for i in range(num_players):
        line = f"{i + 1:02d} " + " | ".join(["--" if j in board[i] else "  " for j in range(num_players)])
        print(line + " |")

def play_ghost_leg(board):
    num_players = len(board)
    results = list(range(1, num_players + 1))
    
    for i in range(num_players):
        position = i
        for j in board[i]:
            if j > i:
                position += 1
            else:
                position -= 1
        results[i] = position + 1

    return results

def map_prizes(num_players):
    # Create a mapping of players to prizes
    prizes = list(range(1, num_players + 1))  # Assuming prizes are numbered 1 to num_players
    random.shuffle(prizes)  # Shuffle to assign random prizes
    return {f"P{i + 1}": f"Prize {prizes[i]}" for i in range(num_players)}

def display_prize_mapping(prize_mapping):
    print("\nPlayer-to-Prize Mapping:")
    for player, prize in prize_mapping.items():
        print(f"{player} -> {prize}")

def main():
    num_players = int(input("Enter the number of players: "))
    num_ladders = int(input("Enter the number of ladders: "))
    
    board = create_board(num_players, num_ladders)
    display_board(board, num_players)

    while True:
        update = input("Enter a number to update the board (or 'n' to stop): ")
        if update.lower() == 'n':
            break
        else:
            try:
                update = int(update)
                print(f"Updating board with new input: {update}")
                # Update logic (if needed) can be added here
            except ValueError:
                print("Please enter a valid number or 'n' to stop.")

    results = play_ghost_leg(board)
    print("Results:")
    for i, result in enumerate(results):
        print(f"Participant {i + 1} ends up with: {result}")

    # Map prizes to players
    prize_mapping = map_prizes(num_players)
    display_prize_mapping(prize_mapping)

    # Display final mapping of players to prizes based on results
    print("\nFinal Player-to-Prize Assignment:")
    for i in range(num_players):
        player = f"P{i + 1}"
        prize = prize_mapping[f"P{results[i] - 1}"]
        print(f"{player} -> {prize}")

if __name__ == "__main__":
    main()
