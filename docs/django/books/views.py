from django.shortcuts import render
from datetime import datetime
import requests
import os
from pprint import pprint

# Create your views here.
def index(request):
    return render(request, 'books/index.html')

def graduation(request):
    datetimenow = datetime.now()
    datetimeend = datetime(2019, 6, 25)
    how_long = datetimeend - datetimenow
    days = how_long.days
    hours = how_long.seconds // 3600
    remained_time = f'{days}일 {hours}시간 남았습니다.'
    context = {
        'remained_time' : remained_time,
    }
    return render(request, 'books/graduation.html', context)

def imagepick(request):
    return render(request, 'books/imagepick.html')

def today(request):
    url =  "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID=" + 'ffe2bc97829d93ca63399baad7c1edb2'
    res = requests.get(url).json()
    print("날씨 정보 출력")
    context = {
        'current' : round(res['main']['temp'] - 273.15, 1),
        'max' : round(res['main']['temp_max'] - 273.15, 1),
        'min' : round(res['main']['temp_min'] - 273.15, 1),
    }
    return render(request, 'books/today.html', context)

def asciinew(request):
    return render(request, 'books/ascii_new.html')

def asciimake(request):
    my_text = request.GET.get('ascii')
    my_font = request.GET.get('font')
    print(my_text)
    print(my_font)
    url = f'http://artii.herokuapp.com/make?text={my_text}&font={my_font}'
    result = requests.get(url).text
    context = {'result': result,}
    return render(request, 'books/ascii_make.html', context)

def original(request):
    return render(request, 'books/original.html')

def translated(request):
    papago_text = request.GET.get('papago_text')
    naver_client_id = os.getenv("NAVER_CLIENT_ID")
    naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    # 네이버에 Post 요청을 위해서 필요한 내용들
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }

    data = {
        "source": "ko",
        "target": "en",
        "text": papago_text,
    }
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    english = papago_response["message"]["result"]["translatedText"]
    context = {
        'korean' : papago_text,
        'english' : english,
    }
    pprint(papago_response)
    print("ENGLISH : ")
    print(english)
    return render(request, 'books/translated.html', context)
