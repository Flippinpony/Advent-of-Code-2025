solution1 = 0
solution2 = 0

def find_repeat(s):
    #print(f"Finding {s}")
    for n in range(1,len(s)//2 + 1):
        sub = s[:n]
        if len(s) % n == 0 and len(s) // n == s.count(sub):
            return True
    return False

def find_double(s):
    #print(f"Finding {s}")
    #print(f"Check {s[:len(s)//2]} vs {s[len(s)//2:]}")
    if s[:len(s)//2] == s[len(s)//2:]:
        return True
    return False
        

with open("input/day2input.txt") as file:
    num_ranges = file.readline().split(',')
pairs = []
for num_range in num_ranges:
    pairs.append(num_range.split('-'))

for pair in pairs:
    values = range(int(pair[0]), int(pair[1])+1)
    for n in values:
        if find_double(str(n)):
            #print(n)
            solution1 += n
        if find_repeat(str(n)):
            #print(n)
            solution2 += n

print (f"Part 1: {solution1}")
print (f"Part 2: {solution2}")
