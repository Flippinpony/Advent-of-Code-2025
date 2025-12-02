dial_pos = 50
zero_count = 0
zero_count_inclusive = 0

with open("input/day1input.txt") as file:
    for line in file:
        dial_change = int(line.replace('R','').replace('L','-'))
        # workaround (starting at 0 and going left)
        if (dial_pos == 0 and dial_change < 0):
            zero_count_inclusive -= 1
        dial_pos_premod = dial_pos + dial_change
        print(f"Line: {line} Old: {dial_pos} Change: {dial_change} New: {dial_pos_premod} Crossings: {abs(dial_pos_premod // 100)}")
          # workaround 2 (going right and ending at 0 after at least one full revolution)
        if (dial_pos_premod // 100 > 0 and dial_pos_premod % 100 == 0):
            zero_count_inclusive -= 1
        zero_count_inclusive += abs(dial_pos_premod // 100)
        dial_pos = dial_pos_premod % 100
        if not dial_pos:
            zero_count += 1
            zero_count_inclusive += 1
print (f"Part 1: {zero_count}")
print (f"Part 2: {zero_count_inclusive}")
# I should not have started this at 2am, brain no work