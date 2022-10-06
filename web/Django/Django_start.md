# Django_start

```bash
# 1. 가상환경 만들기
$ python -m venv venv

# 2. 가상환경 활성화
$ source venv/Scripts/activate # Windows
$ source venv/bin/activate # Mac

# 2-1. 가상환경 비활성화
$ deactivate

# 3. django 설치하기 3.2(LTS)
$ pip install django==3.2.13

# 3-1. 가상환경 패키지 목록 조회
$ pip list

# 4. requirements.txt 생성
$ pip freeze > requirements.txt

# 4-1. requirements.txt 목록 설치
$ pip install -r requirements.txt

# 5. django 프로젝트 생성
$ django-admin startproject firstpjt .

# 6. django 서버 실행
$ python manage.py runserver

# 7. django 애플리케이션 생성, 일반적으로 app이름은 복수형으로 작성하는 것을 권장
$ python manage.py startapp articles

# 8. INSTALLED_APPS에 앱을 등록
# 9. urls.py에 path 등록
# 10. views.py에 함수 생성
# 11. template 생성
# 12. 크롬에서 해당 URL로 요청
```

- LTS
  - Long Term Support (장기 지원 버전)
  - 일반적인 경우보다 장기간에 걸쳐 지원하도록 고안된 소프트웨어의 버전
  - 컴퓨터 소프트웨어의 제품 수명주기 관리 정책
  - 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장



### Project & Application

1. project

   - "collection of apps"

   - 구조

     ![img_pjt구조](https://user-images.githubusercontent.com/84832358/194228014-5dde7816-4c3c-4e5e-b618-28aaf19e124f.PNG)

     - manage.py

       - Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

         ```bash
         $ python manage.py <command> [options]
         ```

         

2. Application

   - 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당
   - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장
   - 일반적으로 app이름은 복수형으로 작성하는 것을 권장



### 이후

1. 애플리케이션 등록 

   - 반드시 app생성 후 등록
   - 순서

   ```python
   # crud/setting.py
   
   INSTALLED_APPS = [
       # Local apps
       'articles',
       
       # Third party apps
       
       # Django apps
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   ```

2. URLs

   ```python
   # crud/urls.py
   
   from django.contrib import admin
   from django.urls import path
   from articles import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('index/', views.index)
   ]
   ```

   

   

3. Views

   ```python
   # articles/views.py
   
   def index(request):
       return render(request, 'index.html')
   ```

   

4. Templates

   - 실제 내용을 보여주는데 사용되는 파일
   - 파일의 구조나 레이아웃을 정의
   - 기본 경로
     - app 폴더 안의 templates 폴더 (템플릿 폴더 이름은 반드시 templates)