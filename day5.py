from itertools import chain

fresh_ranges = []
solution1 = 0
solution2 = 0

def search_set(line):
    val = int(line)
    for curr_range in fresh_ranges:
        if val >= curr_range[0] and val <= curr_range[1]:
            return True
    return False


def range_len(in_tup):
    return in_tup[1]-in_tup[0]+1


with open("input/day5input.txt") as file:
    blank_found = False
    for line in file:
        if line == "\n":
            blank_found = True
        elif blank_found:
             if search_set(line):
                 solution1 += 1
        else:
            fresh_ranges.append(tuple(int(n) for n in line.split('-')))
            
#part 2 - form a union of all sets
sorted_ranges = sorted(fresh_ranges)
last_range = sorted_ranges[0]
solution2 += range_len(last_range)
#print(f"Adding initial: {range_len(last_range)}")

for curr_range in sorted_ranges[1:]:
    #print(f" processing {curr_range}")
    if curr_range[0] <= last_range[1]: 
        if curr_range[1] <= last_range[1]:
            #subset, skip it
            print("skipping subset")
        else:
            #Partial subset, calculate overlap
            overlap = last_range[1]-curr_range[0]+1
            solution2 += range_len(curr_range) - overlap
            #print(f"Adding partial: {range_len(curr_range) - overlap}")
    else:
        #no overlap
        #print(f"Adding Full: {range_len(curr_range)}")
        solution2 += range_len(curr_range)

    last_range = curr_range
    
    


print (f"Part 1: {solution1}")
print (f"Part 2: {solution2}")