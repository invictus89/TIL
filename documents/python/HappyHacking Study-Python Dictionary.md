# 20190529_Python_Dictionary_Set

## 목표

파이썬에서 dictionary와 set 자료구조를 이해하여 lotto 당첨 프로그램을 만들어보자.

## 들어가기 전에

PyCharm 프로젝트를 새로 생성할 때 라이브러리를 새로 설치하여야 한다.

>pip install requests
>
>pip install bs4
>
>etc...

## Json Decorder Error 발생

크롤링 간 웹 사이트에서 json형식의 받아오기 위하여 아래와 같이 코드를 작성하였다.

```python
import requests
import random
import json
from pprint import pprint

url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=860'
res = requests.get(url)
lottery = res.json()
```

그리고 아래와 같은 디코더 오류가 발생하였다.

```text
raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 18 column 1 (char 34)
```

## Error 원인

원인은 URL 문제였다. 

위의 URL은 일반 웹 사이트 주소이다. 이곳에는 여러 데이터들이 있는데 이것을 json으로 바꿔 불러오려면 데이터 형식 오류가 생긴다. 

## Error 해결방법

따라서 일반 웹 사이트 주소가 아닌 API 주소가 필요하다. 다행이 로또 사이트의 API 주소가 따로 있었다.

><https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=860>

그 주소로 접속하면  아래와 같이 Json 형식의 데이터가 뜬다. 

```json
{"totSellamnt":81846672000,"returnValue":"success","drwNoDate":"2019-05-25","firstWinamnt":1879899825,"drwtNo6":32,"drwtNo4":25,"firstPrzwnerCo":10,"drwtNo5":27,"bnusNo":42,"firstAccumamnt":18798998250,"drwNo":860,"drwtNo2":8,"drwtNo3":18,"drwtNo1":4}
```

위의 코드는 보기가 안좋다. 

이를 위한 유용한 확장 프로그램이 있다. json formatter이다. (크롬 extension에서 받으면 된다.)

그럼 아래와 같이 데이터가 바뀐다.

```json
{
"totSellamnt": 81846672000,
"returnValue": "success",
"drwNoDate": "2019-05-25",
"firstWinamnt": 1879899825,
"drwtNo6": 32,
"drwtNo4": 25,
"firstPrzwnerCo": 10,
"drwtNo5": 27,
"bnusNo": 42,
"firstAccumamnt": 18798998250,
"drwNo": 860,
"drwtNo2": 8,
"drwtNo3": 18,
"drwtNo1": 4
}
```

그럼 이렇게 보기 편한게 바뀐다. 

