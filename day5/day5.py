import re
import sys

input_path = "input.txt"

# Set which part of the problem we are calculating defaults to part 1
part=1
if sys.argv:
    part=int(sys.argv[1])

print("Calculating part: "+str(part)+"\n")

crate_stacks = [] 

with open(input_path) as input_file:
    stack_building = True
    for linenum, line in enumerate(input_file, start= 0):
        if stack_building:
            if linenum==0:
                for i in range(int((len(line))/4)): # Create empty lists in crate_stacks based on line length of the first line
                    crate_stacks.append([])
                    i+=1
            matches = re.finditer(r'[A-Z]', line) 
            for match in matches:
                stack_number = int((match.start()-1)/4)
                crate_stacks[stack_number].insert(0, match.group())
            if line=='\n':
                stack_building = False
        else:
            # Parse and perform crate movement between stacks
            quantity = int(re.search(r'(?<=move )\d+', line).group(0))
            col_from = int(re.search(r'(?<=from )\d+', line).group(0))
            col_to = int(re.search(r'(?<=to )\d+', line).group(0))
            if part==1:
                for crates in range(quantity):
                    in_motion = crate_stacks[col_from-1].pop()
                    crate_stacks[col_to-1].append(in_motion)
            elif part==2:
                crateholder = []
                for crates in range(quantity):
                    in_motion = crate_stacks[col_from-1].pop()
                    crateholder.append(in_motion)
                for crates in range(quantity):
                    in_motion = crateholder.pop()
                    crate_stacks[col_to-1].append(in_motion)

print("\nEnd State")
tops = []
for col in crate_stacks:
    print(col)
    tops.append(col[-1])

print("\nTop Crates")
print(tops)
