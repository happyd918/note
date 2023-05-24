# URLS

### Trailing Slashes

- Django는 URL 끝에 `/`가 없다면 자동으로 붙여주는 것이 기본 설정
- Django의 url 설계 철학을 통해 살펴보면 `/`가 붙은것과 안붙은 것이 서로 다른 url이다
  - 검색 엔진 로봇이나 웹 트래픽 분석 도구에서 그 둘을 서로 다른 페이지로 봄
  - 그래서 그들이 혼동하지 않도록 정규화함



### Variable routing

- URL 주소를 변수로 사용하는 것을 의미
- 일부를 변수로 지정하여 view함수의 인자로 넘길 수 있음

1. 작성

   - 변수는 `<>`에 정의한다
   - 기본타입은 string, 5가지 타입

   1. str
      - `/`를 제외하고 비어있지 않은 모든 문자열
   2. int
      - 0 또는 양의 정수와 매치
   3. slug
   4. uuid
   5. path



### App URL mapping

- 앱이 많아졌을 때 urls.py를 각 app에 매핑하는 방법

- app의 view함수가 많아지면 사용하는 path()또한 많아지고,

  app 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음

- Including other URLconfs

  ```python
  # crud/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
  ]
  ```

  - urlpattern은 언제든지 다른 URLconf 모듈을 포함(include)할 수 있음
  - include되는 앱의 urls.py에 urlpatterns가 작성되어 있지 않다면 에러 발생, 빈 리스트라도 작성되어 있어야 한다.

  ```python
  # articles/urls.py
  
  from django.urls import path
  
  
  urlpatterns = [
      
  ]
  ```

  - 각 app 폴더 안에 urls.py를 작성하고 관리할 수 있다

  

### Naming URL patterns

`path('greeting/', views.greeting, name='greeting')`

- `path()` 함수의 name인자를 정의해서 사용
- DTL의 Tag 중 하나인 URL 태그를 사용해서 `path()`함수의 name을 사용할 수 있음
  - `{% url 'greeting' %}`



### URL namespace

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
    ...,
]
```

- 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 사용가능
- `{% url 'greeting' %}` -> `{% url 'articles:greeting' %}`