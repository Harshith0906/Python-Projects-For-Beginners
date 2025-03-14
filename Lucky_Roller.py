import random

def roll():
    min_val=1
    max_val=6
    roll=random.randint(min_val,max_val)
    return roll
while True:
    players=int(input("Enter the number of players(2-4): "))
    if 2<=players<=4:
        break
    else:
        print("Invalid Number")
        print("Please Select a Number 2-4 again..")
max_score=50
players_scores=[0 for _ in range(players)]

while max(players_scores)<max_score:
    for player_idk in range(players):
        print("\nPlayer Number",player_idk+1,"Turn Just Started")
        print("Your Total Score is",players_scores[player_idk],"\n")
        current_score=0

        while True:
            should_roll=input("Would you like to roll(y)?")
            if should_roll.lower()!="y":
                break

            value=roll()
            if value==1:
                print("You Rolled 1! Turn Done!")
                current_score=0
                break
            else:
                current_score+=value
                print("You Rolled:",value)
            print("Your Score is:",current_score)
        players_scores[player_idk]+=current_score
        print("Your Total Score is:",players_scores[player_idk])
max_score=max(players_scores)
winning=players_scores.index(max_score)
print("Player Number",winning+1,"is the winner with a score of",max_score)