puzzle_input = open("Day 5/puzzleinput.txt").read().splitlines()

def decode_row(s):
    options = [i for i in range(128)]
    for char in s[0:7]:
        l = int(len(options)/2)
        if char == "F":
            del options[l:]
        if char == "B":
            del options[:l]
    return options[0]

def decode_column(s):
    options = [i for i in range(8)]
    for char in s[7:]:
        l = int(len(options)/2)
        if char == "L":
            del options[l:]
        if char == "R":
            del options[:l]
    return options[0]

def seat_id(s):
    return ((decode_row(s) * 8) + decode_column(s))

list_of_ids = []

for seat in puzzle_input:
    list_of_ids.append(seat_id(seat))
    list_of_ids.sort()

missing = []

for num in range(54,930):
    if num not in list_of_ids:
        missing.append(num)

print(missing)