# Template

소개

- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
- 파일의 구조나 레이아웃을 정의

기본 경로

- app 폴더 안의 templates 폴더 (템플릿 폴더 이름은 반드시 templates)



### DTL (Django Template Language)

> Django template에서 사용하는 built-in template system
>
> Python 코드로 실행되는 것이 아님
>
> 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임을 명심할 것

1. **Variable**

   `{{ variable }}`

   - 변수명은 영어, 숫자와 밑줄(_)의 조합으로 구성될 수 있으나 밑줄로는 시작 할 수 없음

   - dot(.)을 사용하여 변수 속성에 접근할 수 있음

   -  render()의 세번째 인자로 `{'key': value}`와 같이 딕셔너리 형태로 넘겨받으며, 

     여기서 정의한 `key`에 해당하는 문자열이 template에서 사용가능한 변수명이다.

2. **Filters**

   `{{ variable|filter }}`

   - 표시할 변수를 수정할 때 사용
   - https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#built-in-filter-reference

3. **Tags**

   `{% tag %}`

   - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하는 등 변수보다 복잡한 일들을 수행
   - ex: if, for, ...
   - https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#built-in-tag-reference

4. **Comments**

   `{# #}`

   - 라인의 주석을 표현하기 위해 사용

   `{% comment %}{% endcomment %}`

   - 여러줄 주석



### Template inheritance (템플릿 상속)

> 템플릿 상속은 기본적으로 코드의 재사용성에 초점
>
> 기본 'skeleton' 템플릿을 만들 수 있다.

1. `{% extends '' %}`
   - 하위템플릿이 부모 템플릿을 확장한다는 것을 알림
   - 반드시 최상단에 작성 (2개이상 사용할 수 없다)

2. `{% block content %}{% endblock content %}`

   - 하위템플릿에서 재지정할 수 있는 블록을 정의
   - 하위 탬플릿이 채울 수 있는 공간

3. 추가 템플릿 경로 추가하기

   - base.html의 위치를 앱 안의 template 디렉토리가 아닌 프로젝트 최상단의 templates 디렉토리 안에 위치하고 싶다면?

   ```python
   # setting.py
   
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [BASE_DIR / 'templates',],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

   

### form

> 클라이언트 측에서 HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법

- 웹에서 사용자 정보를 입력하는 여러 방식을 제공하고 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당
- 데이터를 어디(**action**)로 어떤 방식(**method**)으로 보낼지

1. action
   - 입력 데이터가 전송될 URL을 지정
   - 반드시 유효한 URL이어야 한다.
   - 지정하지 않으면 form이 있는 페이지의 URL로 보내짐
2. method
   - 어떻게 보낼 것인지
   - 입력 데이터의 HTTP request methods를 지정
   - 2가지 방법이 있다. `GET`, `POST`
   - HTTP
     - HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
     - 웹에서 이루어지는 모든 데이터 교환의 기초
     - 주어진 리소스가 수행 할 원하는 작업을 나타내는 request methods를 정의
     - GET, POST, PUT, DELETE
3. input
   - 데이터를 입력 받기 위해 사용
   - `type` 속성에 따라 동작 방식이 달라진다. 기본값은 `text`
   - 핵심속성 name
4. name
   - form을 통해 데이터를 제출했을 때 name 속성에 설정된 값을 서버로 전송하고, 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음
   - 주요 용도는 서버에 전달하는 파라미터로 매핑하는것 (name은 key, value는 value)
   - GET 방식에서는 URL에서 `?key=value&key=value/`형식으로 데이터를 전달



### form Method

#### GET

- 서버로부터 정보를 조회하는 데 사용
- 데이터를 가져올 때만 사용
- 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
  - 데이터는  URL에 포함되어 서버로 보내짐
- 명시적 표현을 위해 대문자 사용 권장
- Query String Parameter
  - 사용자가 입력 데이터를 전달하는 방법 중 하나
  - `key=value` 쌍으로 구성 `?`으로 시작되고 `&`으로 구분

#### GET 데이터 가져오기

- 모든 요청 데이터는 view 함수의 첫번째 인자 request에 들어있다.

- request

  ```python
  # articles/views.py
  
  def catch(request):
      print(request)
      print(type(request))
      print(request.GET)
      print(request.GET.get('mesage'))
      return render(request, 'catch.html')
  ```

  ![img_request](https://user-images.githubusercontent.com/84832358/194263250-30071404-b919-43e6-892b-f52730158400.PNG)

- 작성해보기

  ```python
  def catch(request):
      message = request.GET.get('message')
      context = {
          'message': message,
      }
      return render(request, 'catch.html', context)
  ```

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>Catch</h1>
    <h2>여기서 {{ message }}를 받았어!</h2>
    <a href="/throw/">다시 던지러</a>
  {% endblock content %}
  ```

- Request and Response objects

  - 요청과 응답 객체 흐름

  1. 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 HttpRequest object를 생성
  2. 해당하는 view함수를 로드하고 HttpRequest를 첫번째 인자로 전달
  3. view함수는 HttpResponse object를 반환