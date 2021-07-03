# https://programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations

def solution(n, weak, dist):
    # extend the list to make it a circle
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1 # set as  max

    for start in range(length):
        for frieds in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + frieds[count - 1]

            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + frieds[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return - 1
    
    return answer



