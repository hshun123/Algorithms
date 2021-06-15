# count the total number of "3" in given time
h = int(input())

count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # increase the count when 3 is in the string: 00:00:00 which represents the time
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)