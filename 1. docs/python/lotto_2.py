import requests
import random
import json
from pprint import pprint

url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=860'
res = requests.get(url)
lottery = res.json()
# pprint(lottery)

winner = []
for i in range(1, 7):
    winner.append(lottery[f'drwtNo{i}'])
bonus = lottery['bnusNo']

# 내가 풀이한 방법
count = 1
while True:
    my_list = random.sample(range(1, 46), 7)
    #my_list = [4, 8, 18, 25, 27, 41, 32]
    dup_count = 0

    for idx in range(0, 7):
        if my_list[idx] in winner:
            dup_count = dup_count + 1
    if dup_count == 6:
        print(winner, bonus)
        print(my_list)
        print(f'1등 / {count}번 시도함')
        break
    elif dup_count == 5:
        if bonus in my_list:
            print(my_list)
            print(winner, bonus)
            print(f'2등 / {count}번 시도함')
        else:
            print(my_list)
            print(winner, bonus)
            print(f'3등 / {count}번 시도함')
    elif dup_count == 4:
        print(f'4등 / {count}번 시도함')
    elif dup_count == 3:
        print(f'5등 / {count}번 시도함')
    count = count+1

'''
# 교집합을 이용한 방법
count = 0
while True:
    my_list = random.sample(range(1, 46), 7)
    dup_count = len(set(my_list) & set(winner))

    if dup_count == 6:
        print(winner, bonus)
        print(my_list)
        print(f'1등 / {count}번 시도함')
        break
    elif dup_count == 5:
        if bonus in my_list:
            print(winner, bonus)
            print(my_list)
            print(f'2등 / {count}번 시도함')
        else:
            print(f'3등 / {count}번 시도함')
    elif dup_count == 4:
        print(f'4등 / {count}번 시도함')
    elif dup_count == 3:
        print(f'5등 / {count}번 시도함')

    count = count + 1
'''