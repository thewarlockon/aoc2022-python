import sys

input_path = "input.txt"
top_elves_number = 3

max_elf = 0
top_x_elves = [0 for x in range(top_elves_number)]

with open(input_path) as input_file:
    elf_calories=0
    for line in input_file:
        if line=='\n':
            for ind, elf in enumerate(top_x_elves):
                if elf<elf_calories:
                    top_x_elves[ind]=elf_calories
                    break
            if max_elf < elf_calories:
                max_elf=elf_calories
            elf_calories=0
        else:
            elf_calories+=int(line)

print(max_elf)
print(top_x_elves)
print(sum(top_x_elves))
