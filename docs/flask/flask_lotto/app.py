from flask import Flask, render_template, request
import requests
import json
import random
app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    #page 만 띄어주는 역할을 한다.
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    temp_num = request.args.get('my_num')

    response = requests.get(f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}')
    lotto = response.json()

    # list comprehension
    winner = [lotto[f'drwtNo{idx}'] for idx in range(1, 7)]

    # 내 번호 리스트 만들기
    # my_num = random.sample(range(1, 46), 7)
    temp_num = temp_num.split(',')
    my_num = [int(num) for num in temp_num]

    # 당첨번호와의 교집합
    dup_count = len(set(my_num) & set(winner))
    '''
    for idx in range(0, 7):
        if my_list[idx] in winner:
            dup_count = dup_count + 1
    '''

    # 조건에 따라 1등부터 꽝까지 결과값을 Lotto_result 로 보내준다.
    result = ''
    if dup_count == 6:
        result = '1등'
    elif dup_count == 5:
        if lotto['bnusNo'] in my_num:
            result = '2등'
        else:
            result = '3등'
    elif dup_count == 4:
        result = '4등'
    elif dup_count == 3:
        result = '5등'
    else:
        result = '꽝'

    return render_template('lotto_result.html', lotto_round=lotto_round, winner=f'{winner} + {lotto["bnusNo"]}', my_num=my_num, result=result)

if __name__ == "__main__":
    app.run(debug=True)
