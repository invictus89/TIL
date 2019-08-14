# decorator는 장식해주는 역할을 한다.
# bye라는 함수를 수정하지 않고 다른 함수의 기능을 잠시 붙여 사용하고 싶을 때

def hello(func):
    def wrapper():
        print('hi hi')
        func()
        print('hi hi')
    return wrapper

# hello라는 함수가 bye라는 함수를 꾸며준다.
@hello
def bye():
    print('bye bye')

bye()