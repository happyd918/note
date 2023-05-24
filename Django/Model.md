# Model

> Django는 Model을 통해 데이터에 접속하고 관리
>
> 저장된 데이터베이스의 구조
>
> 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(대응)
>
> - 모델 클래스 1개 == 데이터베이스 테이블 1개



### Model 작성

1. models.py 작성

   - 모델 클래스를 작성하는 것은 데이터베이스 테이블의 **스키마를 정의**하는것

   - id컬럼은 테이블 생성시 Django가 자동으로 생성

     ```python
     # articles/models.py
     
     class Article(models.Model):
         title = models.CharField(max_length=10)
         content  = models.TextField()
     ```

     - 각 모델은 `django.models.Model`클래스의 서브 클래스로 표현됨

       `django.db.models`모듈의 `Model`클래스를 상속받아 구성

     - 클래스 상속 기반 형태의 Django 프레임워크 개발

     - 데이터 유형에 따라 다양한 모델 필드 제공

     - https://docs.djangoproject.com/en/3.2/ref/models/fields/



### Migrations

- 모델에 대한 청사진을 만들고 이를 통해 테이블을 생성하는 일련의 과정
- Django가 모델에 생긴 변화(필드 추가 ,모델 삭제 등)를 DB에 반영하는 방법

1. makemigrations
   - 모델을 작성 혹은 변경한 것에 기반한 새로운 migration(설계도)을 만들 때 사용
   - 파이썬으로 만든 설계도
2. migrate
   - 위에서 만든 설계도를 실제 db.sqlite3 DB 파일에 반영하는 과정
   - 모델과 DB의 동기화



### ORM

- makemigrations에 의해 파이썬으로 만든 설계도를 SQL만 알아 들을 수 있다는 DB와 migrate 할 수 있는 이유
- 중간에 해석 담당
- Django는 내장 Django ORM을 사용