# 짝수 홀수 개수
# 문제 설명
# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 1 ≤ num_list의 길이 ≤ 100
# 0 ≤ num_list의 원소 ≤ 1,000
# 입출력 예
# num_list	result
# [1, 2, 3, 4, 5]	[2, 3]
# [1, 3, 5, 7]	[0, 4]
# 입출력 예 설명
# 입출력 예 #1

# [1, 2, 3, 4, 5]에는 짝수가 2, 4로 두 개, 홀수가 1, 3, 5로 세 개 있습니다.
# 입출력 예 #2

# [1, 3, 5, 7]에는 짝수가 없고 홀수가 네 개 있습니다.


def solution(num_list):
    answer = []
    b = 0
    c = 0
    # 일단 짝수부터
    for i in range(0,len(num_list)):
        a = num_list[i]
        if a % 2 == 0:
           b += 1
        elif a % 2 != 0 :
           c += 1

    answer.append(b)
    answer.append(c)
    print(answer)


    return answer

solution([1, 3, 5, 7])

'''
남의 답

def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer




'''