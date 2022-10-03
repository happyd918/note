# 서로소 집합 (Disjoint-sets)

### 소개

서로소 또는 상호배타 집합은 서로 중복 포함된 원소가 없는 집합들이다.

집합에 속한 하나의 특정 멤버를 통해 각 집합을 구분하며 이를 대표자(representative)라한다.



### 연산

##### Make-set(x)

- 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산

- 집합을 만들며 자기 자신이 대표자가 된다

##### Find-Set(x) 

- x를 포합하는 집합의 대표자를 찾는다

  ```python
  # 1. 반복문
  def find_set(node):
      while node != parent[node]:
          node = parent[node]
      return node
  
  
  # # 2. 재귀
  def find_set(node):
      if node != parent[node]:
          return find_set(parent[node])
      return node
  
  
  # # 3. 재귀 - 경로 압축(부모 노드를 대표값으로 만듦)
  def find_set(node):
      if node != parent[node]:
          parent[node] = find_set(parent[node])
      return parent[node]
  ```

  - 재귀 경로 압축 

    ![set1](https://user-images.githubusercontent.com/84832358/193588147-4df8a138-efe6-4cf9-9029-40cf55f1e4d3.png)

    find-set(4) 를 실행하면 다음과 같다.

    ![set2](https://user-images.githubusercontent.com/84832358/193588157-ef2e3114-6e78-4512-bc96-ed224654d00d.png)

##### Union(x,y)

- x, y를 포합하는 두 집합을 통합하는 연산

- 주의점

  - 위 그림에서 다음의 코드를 통해 4, 5 를 합친다고 하면 

    ```python
    x_root, y_root = find_set(x), find_set(y)  # Find
    
        # Union
        if x_root != y_root:  # 서로소 집합인 경우만 합집합 연산
            if x_root < y_root:
                parent[y_root] = x_root
            else:
                parent[x_root] = y_root
    ```

    ![set3](https://user-images.githubusercontent.com/84832358/193588161-a069393e-41c1-41f9-a93a-12f0c1470da8.png)

    5번을 대표자로 가진 집합이 합쳐졌는데 5번은 1번을 가르키지만 5번에 속한 원소들은 1번을 가르키진 않는다. 모든 원소가 경로 압축이 된건 아니다.

