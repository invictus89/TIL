from django.shortcuts import render
import random
from pprint import pprint
import requests

from datetime import datetime
# Create your views here.
# 필수 인자 : request(사용자 요청)
# Render 의 필수 인자
def index(request):
#     print(request)
#     print(type(request))
#     pprint(request.META)
    return render(request, 'pages/index.html')

def dinner(request):
    menus = ['apple', 'pear', 'watermelon']
    pick = random.choice(menus)
    context = {
        'pick' : pick
    }
    return render(request, 'pages/dinner.html', context)

def hello(request, name):
    context = {'name' : name,}
    return render(request, 'pages/hello.html', context)

# 자기소개 - 이름/나이를 url로 받아서 출력합니다.
def introduce(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'pages/intro.html', context)

# 숫자 두 개를 variable routing 으로 받아 곱셉 결과를 출력합니다.
def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result,
    }
    return render(request, 'pages/times.html', context)

# 원의 반지릅 값을 variable routing 으로 받아 원의 넓이를 출력
def area(request, num):
    result = num * num * 3.14
    context = {
        'num' : num,
        'result' : result,
    }
    return render(request, 'pages/area.html', context)

def dtl_example(request):
    menus = ['apple', 'hotteok', 'noddle']
    my_sentence = "life is short, you need python"
    msg = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus' : menus,
        'my_sentence' : my_sentence,
        'msg' : msg,
        'datetimenow' : datetimenow,
        'empty_list' : empty_list,
    }
    return render(request, 'pages/dtl_example.html', context)

def throw(request):
    return render(request, 'pages/throw.html')
# form에서 오는 것과 url에 직접 입력해서 받는 방법은 다르다.
def catch(request):
    # print(request.GET)
    message = request.GET.get('message')
    context = {'message' : message}
    return render(request, 'pages/catch.html', context)

def artii(request):
    return render(request, 'pages/artii.html')

def result(request):
    # 1. form 에서 데이터를 받는다.
    # 2. http://artii.herokuapp.com/fonts_list 로 요청을 보낸 응답 결과를 .text 변환후 저장한다.
    # 3. 저장한 데이터를 list 로 바꾼다.
    # 4. list 안에 들어있는 요소(font) 하나를 선택해서 저장한다.
    # 5. 우리가 전달한 data와 list안의 폰트를 가지고 다시 요청을 보내
    # 해당 응답 결과를 저장한다. (.text)
    # 6. 최종적으로 저장한 데이터를 template 으로 넘겨준다.
    my_text = request.GET.get('my_text')
    req = requests.get('http://artii.herokuapp.com/fonts_list').text
    my_list = req.split('\n')
    my_font = random.choice(my_list)
    url = f'http://artii.herokuapp.com/make?text={my_text}&font={my_font}'
    my_req = requests.get(url).text
    print(my_text)
    print(my_font)
    print(my_req)
    context = {'my_req': my_req, 'my_url': url, }
    return render(request, 'pages/result.html', context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name' : name,
        'pwd' : pwd,
    }
    return render(request, 'pages/user_create.html', context)

def static_example(request):
    return render(request, 'pages/static_example.html')
