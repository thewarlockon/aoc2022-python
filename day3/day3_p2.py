input_path = "input.txt"

priority_dict = {}
for i in range(26):
    priority_dict[chr(i+97)]=i+1
    priority_dict[chr(i+65)]=i+27

with open(input_path) as input_file:
    sum_of_priority = 0
    members_read = 0
    members = []
    for line in input_file:
        if members_read <= 2:
            members.append(line.strip())
            members_read=members_read+1
        if members_read==3:
            for counter,char in enumerate(members[0], start=1):
                if char in members[1] and char in members[2]:
                    sum_of_priority = sum_of_priority + priority_dict[char]
                    break
                if counter == len(members[0]) :
                    print("Shared item not found")
            members_read = 0
            members = []

print(sum_of_priority)