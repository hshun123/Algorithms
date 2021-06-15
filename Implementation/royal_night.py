# data contains the current position of the queen
data = input()
row = int(data[1])
column = int(ord(data[0]) + int(ord('a'))) + 1 # convert the column into integer

# 8 possible directions that the queen can move to 
steps = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:

    next_row = row + step[0]
    next_column = column + step[1]

    # increase the result only when the move is possible
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1


print(result)