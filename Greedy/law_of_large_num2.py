n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort() # sort the array
first = data[n -1] # largest num
second = data[n -2] # second largest num 

# count the times the max num is added
count = int(m/(k + 1)) * k
count = m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result) # final result 