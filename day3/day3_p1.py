input_path = "input.txt"

priority_dict = {}
for i in range(26):
    priority_dict[chr(i+97)]=i+1
    priority_dict[chr(i+65)]=i+27

def find_duplicate(pack_str):
    c1 = pack_str[:len(pack_str)//2]
    c2 = pack_str[len(pack_str)//2:]
    for char in c1:
        if char in c2:
            return priority_dict[char]

with open(input_path) as input_file:
    sum_of_priority = 0
    for line in input_file:
        sum_of_priority = sum_of_priority + find_duplicate(line.strip())

print(sum_of_priority)
