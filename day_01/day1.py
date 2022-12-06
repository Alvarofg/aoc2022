import sys
data_into_list = "".join(sys.stdin).split("\n\n")
high = 0
highest = 0
calories_list = []
for i, elf in enumerate(data_into_list):
    calories = sum(list(map(int, filter(lambda x: x != '', elf.split("\n")))))
    calories_list.append(calories)
    if calories > high:
        high = calories
        highest = i
calories_list.sort(reverse=True)
print("Part 1: The elf with the highest calories is elf #", highest, " carrying ", high, " calories" )
print("Part 2: Calories carrying in total: ", sum(calories_list[0:3]))
