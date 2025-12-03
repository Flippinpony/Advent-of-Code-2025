solution1 = 0
solution2 = 0

with open("input/day3input.txt") as file:
    for line in file:
        first = sorted(line[:len(line)-2])[len(line)-3]
        second = sorted(line[line.find(first)+1:])[::-1][0]
        solution1 += int(first+second)

with open("input/day3input.txt") as file:
    for line in file:
        search_start = 0
        search_end = len(line)-12
        digits = ""
        for n in range(12):
            search_segment = line[search_start:search_end]
            digit = sorted(search_segment)[::-1][0]
            digits += digit
            #print(f"searching {search_segment} .. digit: {digit} - Range: {search_start}-{search_end}")
            search_start += search_segment.find(digit) + 1
            search_end += 1
        #print(digits)
        solution2 += int(digits)


print (f"Part 1: {solution1}")
print (f"Part 2: {solution2}")