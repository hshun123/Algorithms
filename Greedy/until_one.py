# n, k = map(int, input().split())


# count = 0
# while n != 1:
#     if n % k != 0:
#         n -= 1
#         count += 1
#     else:
#         n /= k
#         count += 1

# print(count)

n, k = map(int, input().split())
result = 0

while True:
    # (N == K)
    target = (n // k) * k
    result += (n - target)
    n = target
    # when n < k

    if n < k:
        break
    # divide by k
    result += 1
    n //= k


result += (n - 1) # result
print(result)