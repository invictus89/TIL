from flask import Flask
import A
app = Flask(__name__)

print('top-level B.py')
A.fuc()

if __name__ == '__main__':
    print('B.py가 직접 실행')
else:
    print('B.py가 import 되어 사용됨')