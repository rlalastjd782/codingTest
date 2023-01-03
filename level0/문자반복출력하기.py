# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 2 ≤ my_string 길이 ≤ 5
# 2 ≤ n ≤ 10
# "my_string"은 영어 대소문자로 이루어져 있습니다.
# 입출력 예
# my_string	n	result
# "hello"	3	"hhheeellllllooo"
# 입출력 예 설명
# 입출력 예 #1

# "hello"의 각 문자를 세 번씩 반복한 "hhheeellllllooo"를 return 합니다.

def solution(my_string, n):
    m_list = []
    s_list = []
    answer = ''
    m_list = list(my_string)
    print(m_list)
    for i in range(0,len(m_list)):
        s_list.append(m_list[i]*n)
    print(s_list)

    answer = ''.join(s_list)
    print(answer)

    return answer







'''
더쉬운답

문자를 그대로 .. for 문을 돌린다..

str = "hello"

for i in str :
    answer = ''.join(i * 3)




'''

str = "hello"

print(''.join(i * 3 for i in str ))
