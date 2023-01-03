# 문자열 배열 strlist가 매개변수로 주어집니다. strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ strlist 원소의 길이 ≤ 100
# strlist는 알파벳 소문자, 대문자, 특수문자로 구성되어 있습니다.
# 입출력 예
# strlist	result
# ["We", "are", "the", "world!"]	[2, 3, 3, 6]
# ["I", "Love", "Programmers."]	[1, 4, 12]
# 입출력 예 설명
# 입출력 예 #1

# ["We", "are", "the", "world!"]의 각 원소의 길이인 [2, 3, 3, 6]을 return합니다.
# 입출력 예 #2

# ["I", "Love", "Programmers."]의 각 원소의 길이인 [1, 4, 12]을 return합니다.


# 나의 정답
strlist = ["We", "are", "the", "world!"]
# 이것으로 따옴표를 제외 하고 센다는것을 알았음

def solution(strlist):
    strlist_len = len(strlist)
    answer = []
    for i in range(0,strlist_len):
        print(i)
        a = len(strlist[i])
        answer.append(a)
    
    
    return answer


solution(["We", "are", "the", "world!"])

# 쉬운정답

def solution(strlist):
    answer = list(map(len, strlist))
    return answer


def solution(strlist):
    answer =[]
    for i in strlist:
        answer.append(len(i))
    return answer    