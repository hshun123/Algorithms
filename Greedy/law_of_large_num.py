# # N, M, K
# n, m, k = map(int, input().split())

# arr = list(map(int, input().split()))

# arr.sort()

# result = 0
# count = 1
# for i in range(m):
#     if count != k:
#         result += arr[-1]
#         count += 1
#     else:
#         count = 1
#         result += arr[-2]

# print(result)

#n,m,k
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort() # sort the array
first = data[n -1] # largest num
second = data[n -2] # second largest num 

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break
    result += second
    m -= 1

print(result) # final result 