# 20190529 - 해피해킹 강의 4일차

## 목표

부트스트랩에서 박스 요소의 위치를 자유롭게 조정하기 위한 Flex 기능을 익히자!

Gird 내에서 Flex 기능을 사용할 줄 알아야 하며, 부트스트랩에서 class 이름 명명법으로 사용할 줄 알아야 한다!



## Animation

스타일은 아래와 같이 적용한다.

```css
 .square:hover{
      animation: bounce 2s infinite;
    }
```

HTML을 아래와 같이 적용한다.

```html
 <h1 class="animated infinite bounce delay-2s">Example</h1>
 <i class="fas fa-music fa-5x faa-vertical animated-hover"></i>
```

>* 참고
>
>  완전한 텍스트 중앙 정렬을 위해서는 line-height: 부모 요소 높이, 로 지정하면 된다.

## Flex box

>- 04_flex_00.html ~ 04.flex_04.html / 05_col.html

그리드는 격자로 움직인다. 플랙스는 단 방향으로 움직인다. default 값은 x축 기준이다. 그리드는 12칸이 넘어가면 자동 줄바꿈이 이루어지지만 플렉스는 default로 쭉 나간다.

```html
<div class="container">
    <div class="item item1">1</div>
    <div class="item item2">2</div>
    <div class="item item3">3</div>
</div>
```

1. display : flex
   - 부모 요소(.container)에 적용한다. inline-flex로 지정하면 inline-block level로 적용되면서 내부는 flex가 설정된다.
2. flex-wrap
   - default는 nowrap으로 부모요소의 크기를 넘어가도 한 줄에 배치된다.
   - wrap은 multiple lines 배치된다.
   - wrap-reverse를 하면 밑줄먼저 요소가 생성된다.
3. flex-direction
   - 부모 요소에 적용하며 default : row이다. 
   - row-reverse는 x축 오른쪽에서 부터 왼쪽으로 나열된다.
   - column-reverse는 기본 y축 top에서 bottom으로의 방향의 반대인 from bottom to top이다.
4. flex-grow
   - 자식 요소를 부모 크기에 채운다. 
   - item1에 2 / item2에 3으로 지정되면 2:3 비율로 각각 늘어나게 된다.
5. justify-content
   - flex-start : dafault, 왼쪽 기준
   - flex-end : 오른쪽 기준
   - center : 중앙 정렬
   - space_between : 좌우 정렬
   - space_around : 균등한 좌우 정렬
6. flex-items
   - 기본은 justify-content와 동일, 다만 x축 기준이 y축으로 바뀐다는 것
   - stretch : 상하단을 꽉채운다.
   - baseline : font-size 아래를 기준으로 크기를 조정한다.
7. align-self
   - 부모 요소가 아닌 움직이려는 대상에 적용시킨다!
   - align-items와 동일하다
8. order
   - 요소간의 배치 우선순위를 결정한다.
   - default는 0이고, 작은 값이 우선순위가 높아 top-left에 위치하게 된다.
   - 마이너스 값도 설정 가능하다.

- **주의할 점**

  - **요소를 양쪽으로 넓힐 때 사용하는 것은 space_between!** 
  - **justify-content와 flex-items 활용 시에 flex-direction을 주의한다. 기준이 column이면 justify-content는 default 처럼 x축 기준이 아니라 y축을 기준으로 움직이게 된다!**
  - **flex를 CSS에 설정하는 것과 HTMl에서 직접 클래스 이름으로 접근하는 데 속성 이름 값이 살짝 다르다.**

  ```html
  <div class="row justify-content-around"></div>
  <div class="row row-vh align-items-center"></div>
  <div class="row row-vh align-items-end"></div>
  <div class="col align-self-start"></div>
  ```





## Reference

- <https://daneden.github.io/animate.css/> : HTML 요소에 Animation 효과를 주기위한 기능 설명법과 CSS를 다운받을 수 있다.

- <https://fonts.google.com/>: 구글 폰트 사이트로 Language 설정에서 Kor선택하면 한글도 사용 가능하다.

- <https://fontawesome.com/> : 위의 구글 폰트와 같이 대표적인 폰트 사이트

- https://www.npmjs.com/package/font-awesome-animation : 폰트 awesome에서 animation 적용을 가능케 하는 사이트

  >CDN 방식이 아니기에 .css 파일을 만들어서 사이트의 css 내용을 붙여넣기 해야 한다.

- <https://www.flaticon.com/> : 깔끔한 아이콘들을 사용할 수 있다.

- https://css-tricks.com/snippets/css/a-guide-to-flexbox/> : flox box 사용법을 확인할 수 있다.