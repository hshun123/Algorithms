# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    count = 0
    length = len(stages)
    for i in range(1, N + 1):
        count = stages.count(i)
        if length == 0:
            answer.append((i, 0))
        else:
            answer.append((i, count/length))
        length -= count
        
    answer = sorted(answer, key = lambda x: x[1], reverse = True)
    answer = [i[0] for i in answer]
        
    return answer