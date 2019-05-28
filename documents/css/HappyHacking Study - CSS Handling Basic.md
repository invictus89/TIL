# 20190528 - 해피해킹 강의 3일차

## 목표

기본 CSS 스타일 조작 방법 익히기! (파이썬 기반)

## 들어가기 전에

들어가기 전에 코딩에 도움이 되는 파이썬 속성을 변경하자!

1. JSON 설정 변경

   open setting json에서 아래와 같이 설정을 바꿔주자. 

   ```json
   {
       "python.pythonPath": "C:\\ProgramData\\Anaconda3\\pythonw.exe",
       "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
       "editor.fontFamily" : "Hack",
       "[html]" : {
           "editor.tabSize":2
       }
   }
   ```

   코드가 망가졌을 때 위에서 설정한 spaces(2)를 적용하기 위하여 beautify 라이브러리를 설정한다.

   >extension -> beautify install -> Crtl + Shift + p -> open keyboards shortcuts -> beautify file의 keybinding 설정!

## 코드 파일 생성하기

기존에는 마우스로 new file을 클릭하여 생성하였는데 터미널을 이용한 더 편한한 방법이 있었다.

```
code [file_name.html]
code [file_name.css]
```

## size

- 기존의 px / % / em은 사용은 권장되지 않는다. 최근 개발 트렌드는 rem!

>1 rem = 16px

- vh과 vw는 부모 요소의 높이와 너비의 1/100의 크기로 적용된다. 만약 브라우저 높이가 900px이면 1vh와 1vw는 각 각 9px이다.
- vmax와 vmin은 최대값과 최소값이 필요할 때 사용한다. 만약 브라우저 사이즈가 1100 * 700 이면 1vmax는 11px, 1vmin은 7px가 설정된다.

```html
<p class="vh">vh</p>
<p class="vw">vw</p>
<p class="vmin">vmin</p>
```

```css
.vh {
    font-size: 5vh;
}

.vw{
    font-size: 5vw;
}

.vmin {
    font-size: 10vmin;
}
```

## color

색상 적용 우선 순위는 !important > ID > CLASS > TAG 순서이다! 그리고 색상을 결정하는 여러 클래스가 정의되어있을 때 클래스 이름 순서는 상관없고 css 에 마지막으로 정의된 클래스 이름의 속성이 적용된다

```html
<p class="bold blue pink">blue pin</p>
```

## Selector

nth-child() 와 nth-of-type()의 미묘한 차이를 이해할 줄 알아야 한다.

```html
<div id="mulcam">
    <h2>어떤것이 선택될까?</h2>
    <p>1111</p>
    <p>2222</p>
    <p>3333</p>
    <p>4444</p>
</div>
```

```css
#mulcam > p:nth-child(2){ /* p는 중요하지 않음 */
    color: red;
}
#mulcam > p:nth-of-type(2){
    color: blue;
}
```

p:nth-child()에서 p는 의미가 없다. 따라서 1111 텍스트에 속성이 적용된다.

## Box model

- margin을 이용하 정렬 기준을 이해하자

  ```css
  margin:auto /*가운데정렬*/
  margin-left:auto /*오른쪽 정렬*/
  ```

  설정값이 4개 일때는 top, right, left, bottom

  설정값이 2개 일때는 (top-bottom), (right-left)

  설정값이 3개 일때는 (top), (right-left), (bottom)

- box-sizing을 이해하는 것이 중요하다. 원래는 padding 값을 주면 div 사이즈 크기가 padding 크기만큼 늘어난다. 하지만 box-sizing을 하면 border를 기준으로 box 크기가 고정되어 이를 기준으로 padding과 contents의 크기 값이 변하게 된다. 

  >div 크기 : content size + padding size + border size
  >
  >content 영역 : content size + padding size
  >
  >width , height : content 영역이 설정됨

  ```html
  <div class="square">
      <p>contents 영역 100 * 100</p>
  </div>
  <br>
  <div class="square padding-10">
      <p>contents 영역 120 * 120</p>
  </div>
  <br>
  <div class="square padding-10 border-box">
      <p>contents 영역 98 * 98</p>
  </div>
  ```

  [CSS 코드 생략]

## Display

block : 항상 새로운 자리에서 시작하여 한줄을 다 차지한다.

inline : 새로운 라인에서 시작하지 않으며 content의 너비만큼 가로폭을 차지한다.

inline-block : inline의 단점(width, height, margin 속성 지정 못함)을 보완하기 위한 것

None :  공간이 사라진다.

visible : default value

hidden : 공간은 차지하지만 보여주지는 않는다. (cf. display's none)

## position

- 05_display.html

static : 

relatvie : 자기 원래 위치를 기준으로 움직임, 이동하여도 이전 공간을 차지하고 있다.

absolute :  static이 아닌 relative인 부모를 찾을 때까지 상위 이동 후 그 기준으로 위치 변경. 이것을 사용하려면 부모는 반드시 relative가 되어야 한다.

fixed(고정 위치) : 보통 네비게이션 바

