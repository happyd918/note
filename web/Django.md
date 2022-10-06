# Django

소개

- 서버를 구현하는 Web Framework

- 파이썬으로 작성됨



### Django's Design Pattern

- MTV 패턴

| MTV      | MVC        |
| -------- | ---------- |
| Model    | Model      |
| Template | View       |
| View     | Controller |

1. Model

   - 데이터와 관련된 로직 관리
   - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록 관리

2. Template

   - 레이아웃과 화면 처리
   - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의

3. View

   - Model & Template과 관련한 로직을 처리해서 응답을 반환

   - 클라이언트의 요청에 대해 처리를 분기하는 역할

   - 예시

     - 데이터가 필요하면 model에 접근해서 데이터를 가져오고

       가져온 데이터를 template로 보내 화면을 구성

       구성된 화면을 응답으로 만들어 클라이언트에게 반환

![img_mtv](https://user-images.githubusercontent.com/84832358/194217093-e07e2f7a-e8d5-45ab-ba1a-ea8e017b77dd.PNG)