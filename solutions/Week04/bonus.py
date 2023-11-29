player1_wins = 0
player2_wins = 0
draws = 0
with open("player1.txt", "r") as file1:
    player1_list = [line.strip() for line in file1]
with open("player2.txt", "r") as file2:
    player2_list = [line.strip() for line in file2]
for rounds in range(len(player1_list)):
    if player1_list[rounds] == player2_list[rounds]:
        draws += 1
    elif player1_list[rounds] == "R":
        if player2_list[rounds] == "S":
            player1_wins += 1
        else:
            player2_wins += 1
    elif player1_list[rounds] == "P":
        if player2_list[rounds] == "R":
            player1_wins += 1
        else:
            player2_wins += 1
    elif player1_list[rounds] == "S":
        if player2_list[rounds] == "P":
            player1_wins += 1
        else:
            player2_wins += 1
with open("result.txt", "w") as file3:
    file3.write(f"Player1 wins: {player1_wins}\nPlayer2 wins: {player2_wins}\nDraws: {draws}\n")