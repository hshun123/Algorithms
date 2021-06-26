'''
num = list(input())

mid = len(num) // 2

lst1 = num[:mid]
lst2 = num[mid:]

if sum(map(int, lst1)) == sum(map(int, lst2)):
    print("LUCKY")
else:
    print("READY")
'''

n = input()
length = len(n)
summary = 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length//2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")