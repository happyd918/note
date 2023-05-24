# Views



### render

`render(request, template_name, context)`

- 주어진 template를 주어진 context 데이터와 결합하고

  렌더링 된 텍스트와 함께 HttpResponse 객체를 반환하는 함수

1. request
   - 응답을 생성하는 데 사용되는 요청 객체
2. template_name
   - 템플릿의 전체 이름 또는 템플릿 이름의 경로
3. context
   - 템플릿에서 사용할 데이터 (딕셔너리 타입)