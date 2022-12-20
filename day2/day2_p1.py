import sys

input_path = "input.txt"
scoring_dict = {"R":1, "P":2, "S":3} #Used for scoring could be distinct from wins but not in this case
win_dict = {"R":1, "P":2, "S":3} #Used to determine winning combinations

elf_strat_1 = {"A":"R","B":"P","C":"S"}
my_strat_1 = {"X":"R","Y":"P","Z":"S"}

def determine_winner(game_choices):
    elf_choice = win_dict[elf_strat_1[game_choices[0]]]
    my_choice = win_dict[my_strat_1[game_choices[1]]]
    if elf_choice==my_choice:
        return(1)
    elif (my_choice+1)%3==elf_choice%3:
        return(0)
    else:
        return(2)


with open(input_path) as input_file:
    score = 0
    for line in input_file:
        game_choices = line.strip("\n").split(" ")
        my_choice = my_strat_1[game_choices[1]]
        score=score+scoring_dict[my_choice]
        outcome = determine_winner(game_choices)
        score=score+(3*outcome)

print(score)
