input_path = "input.txt"
scoring_dict = {"R":1, "P":2, "S":3}
win_dict = {"R":1, "P":2, "S":3}
win_dict2 = {v:k for (k,v) in win_dict.items()}


elf_strat_1 = {"A":"R","B":"P","C":"S"}

my_strat_2 = {"X":0,"Y":1,"Z":2}

def determine_choice(game_strat):
    elf_choice = elf_strat_1[game_strat[0]]
    my_strat = my_strat_2[game_strat[1]]
    if my_strat==1:
        return elf_strat_1[game_strat[0]]
    elif my_strat==2:
        return win_dict2[(win_dict[elf_choice]%3)+1]
    elif my_strat==0:
        return win_dict2[(win_dict[elf_choice]+1)%3+1]

with open(input_path, encoding="utf-8") as input_file:
    score = 0
    for line in input_file:
        game_strat = line.strip("\n").split(" ")
        my_strat1 = my_strat_2[game_strat[1]]
        my_choice = determine_choice(game_strat)
        score=score+scoring_dict[my_choice]
        score=score+(3*my_strat1)

print(score)
