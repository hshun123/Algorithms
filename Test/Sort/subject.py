# https://www.acmicpc.net/problem/10825
n = int(input())
students = []

for _ in range(n):
    students.append(input().split())

students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# print out the results
for student in students:
    print(student[0])