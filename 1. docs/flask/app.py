from flask import Flask, render_template, request
import random
from pprint import pprint

app = Flask(__name__)
#flask가 자기를 동작한 인스턴스(app)을 하나 만든다.

'''
def add(func):
라는 함수가 이미 정의되어 있다.
'''
@app.route('/')
def index():
    # View 함수
    return 'hello world'

@app.route('/hello')
def hello():
    # View 함수
    return '반가워요'

'''
@app.route('/user/<int:username>')
def show_user_profile(username):
    return f'User {username}'

# main page의 경우 '/' 유무 상관없이 접속이 가능해야 한다.
@app.route('/projects/')
def projects():
    return 'The project page'

# unique URL로서 /about/은 안된다.
@app.route('/about')
def about():
    return 'The about page'
'''

@app.route('/greeting/<name>')
def greeting(name):
    return f'반가워요. {name}님'

@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return str(result)

# '/lunch/3'으로 요청이 들어왔을 때
# 메뉴 리스트에서 랜덤으로 인원 수 만큼 메뉴 골라서
# 출력해주기
@app.route('/menu/<int:num>')
def menu(num):
    menu_list = ['apple', 'grape', 'watermelone', 'strawberry', 'mango']
    my_list = random.sample(menu_list, 3)
    my_str = ''
    for val in my_list:
        my_str = my_str + val + ' '
    #return str(my_list)
    return str(my_str)

@app.route('/html_tag')
def html_tag():
    return '<h1>안녕하세요.</h1>'

@app.route('/html_line')
def html_line():
    return """
        <h1> multi lines </h1>
        <ul>
            <li> list 1 </li>
            <li> list 2 </li>
            <li> list 3 </li>
        </ul>
    """
@app.route('/html_render')
def html_render():
    return render_template('index.html')

@app.route('/html_name/<name>')
def html_name(name):
    return render_template('hello.html', name=name)

@app.route('/html_cal/<int:num>')
def html_cal(num):
    result = num ** 3
    return render_template('hello.html', num = str(num), result = str(result))

 # 저녁 메뉴 랜덤 뽑기(이미지)
 # /dinner 로 요청이 들어왔을 때
 # 저녁 메뉴에서 하나를 뽑아 이미지와 메뉴 이름을 응답해주자.
@app.route('/dinner')
def dinner():
    my_dict = {
        'apple' : 'https://previews.123rf.com/images/dionisvera/dionisvera1304/dionisvera130400046/19451482-%EC%9E%8E%EA%B3%BC-%EB%B9%A8%EA%B0%84-%EC%82%AC%EA%B3%BC.jpg',
        'pear' : 'https://previews.123rf.com/images/akulamatiau/akulamatiau1411/akulamatiau141101389/33930360-%ED%9D%B0%EC%83%89-%EB%B0%B0%EA%B2%BD-%EC%9C%84%EC%97%90-%EC%95%84%EC%8B%9C%EC%95%84-%EB%B0%B0-%EB%98%90%EB%8A%94-%EB%82%98%EC%8B%9C-%EB%B0%B0-%EA%B3%BC%EC%9D%BC.jpg',
        'grape' : 'https://previews.123rf.com/images/dionisvera/dionisvera1509/dionisvera150900027/46020263-%EC%9E%8E-%EB%8B%AC%EC%BD%A4%ED%95%9C-%ED%8F%AC%EB%8F%84.jpg'
    }

    my_name = random.choice(list(menu.keys()))
    #my_url = menu[my_name] # key error
    my_url = menu.get(my_name) # none
    return render_template('dinner.html', name=my_name, src=my_url)

@app.route('/lotto')
def lotto():
    number_list = list(range(1, 46))
    lucky = random.sample(number_list, 6)
    return render_template('lotto.html', lucky=lucky)

@app.route('/fake_search')
def fake_search():
    return render_template('fake_search.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    #pprint(request.args)
    user_name = request.args.get('name')
    text_list = ['매력 한 스푼', '체력도 넣어주고', '뭔지 모르겠는데 너무 많이 넣었어', '운도 많이 많이', '사랑도 많이 많이']
    get_list = random.sample(text_list, 3)
    my_str = ''
    for idx in range(0, len(get_list)):
        if idx is not len(get_list)-1:
            my_str = my_str + get_list[idx] + '/'
        else:
            my_str = my_str + get_list[idx]
    return render_template('pong.html', user_name=user_name, get_list=get_list, my_str=my_str)

@app.route('/ping_new')
def ping_new():
    return render_template('ping_new.html')

@app.route('/pong_new', methods=['POST'])
def pong_new():
    user_name = request.form.get('name')
    return render_template('pong_new.html', user_name=user_name)

# 이 파이썬 파일이 직접 실행된 코드라면 아래를 동작한다.
if __name__ == '__main__':
    app.run(debug=True)
    #debug : 코드가 바뀌는 것을 인식함
    #서버를 재가동할 필요가 없음