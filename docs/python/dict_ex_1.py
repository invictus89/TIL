'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

sum = 0
for value in score.values():
    sum = sum + value
print(f'평균 점수:{sum / len(score)}')

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
for key in scores.keys():
    sum = 0
    for value in scores[key].values():
        sum = sum + value
    avg = sum / 3
    print(f'{key}반의 평균 점수 : {avg}')


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?
temp = [1,2,3]
# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
for key, value in city.items():
    sum = 0
    for val in value:
        sum = sum + val
    avg = sum / 3
    print(f'{key} : {int(avg)}')

'''
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
'''


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
max_val = -123123
max_city = ''
min_val = 123123
min_city = ''
for key, value in city.items():
    for val in value:
        if max_val < val:
            max_city = key
            max_val = val
        if min_val > val:
            min_city = key
            min_val = val
print(f'가장 더운 곳 : {max_city}({max_val}), 가장 추운 곳: {min_city}({min_val})')
print(2 in city['서울'])