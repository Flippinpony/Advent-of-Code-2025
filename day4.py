grid = []
to_remove = []
solution1 = 0
solution2 = 0

def build_grid():
    with open("input/day4input.txt") as file:
        for line in file:
            grid.append(['.'] + list(line.strip()) + ['.'])
    # add padding rows
    grid.append(['.'] * len(grid[0]))
    grid.insert(0,['.'] * len(grid[0]))

def get_adjacent(row, column):
   #print(f"Check {row},{column}")
   adjacent = 0
   for i in range(-1,2):
       for j in range(-1,2):
           if grid[row+i][column+j] == '@':
               if (i != 0 or j != 0):
                adjacent += 1;
   #print(adjacent)
   return adjacent

def mark_for_remove():
    remove_count = 0
    for row in range(1,len(grid)-1):
        for column in range(1, len(grid[row])-1):
            if grid[row][column] == '@' and get_adjacent(row, column) < 4:
                #print(f"Candidate: {row},{column}")
                to_remove.append((row,column))
                remove_count += 1
    return remove_count
        
def do_remove():
    for x in range(len(to_remove)):
        grid[to_remove[x][0]][to_remove[x][1]] = '.'
    to_remove.clear()



# do part 1
build_grid()
solution1 = mark_for_remove()
solution2 += solution1
# now loop for part 2
while len(to_remove) > 0:
    do_remove()
    solution2 += mark_for_remove()

print (f"Part 1: {solution1}")
print (f"Part 2: {solution2}")