# 머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 0 < money ≤ 1,000,000
# 입출력 예
# money	result
# 5,500	[1, 0]
# 15,000	[2, 4000]
# 입출력 예 설명
# 입출력 예 #1

# 5,500원은 아이스 아메리카노 한 잔을 살 수 있고 잔돈은 0원입니다.
# 입출력 예 #2

# 15,000원은 아이스 아메리카노 두 잔을 살 수 있고 잔돈은 4,000원입니다.


# 내 정답


def solution(money):
    ice = 5500
    # 이게 잔수
    a = money // ice
    b = money - (ice*a)
    answer = [a, b]
    print(answer)
    return answer


solution(15000)

'''
남의답

파이썬의 divmod 라는것이있음
이것을 이용한 답안


def solution(money):
    return divmod(money, 5500)

divmod(x,y)
=> 두 숫자를 인자로 전달받아 첫번쨍인자를 두번째 인자로 나눈 몫과 나머지를 tuple 형식으로 반환한다.    
'''