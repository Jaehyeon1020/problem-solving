# 특정 원소가 속한 집합 찾기(루트 노드)
# parent 인자는 부모 테이블
#
# 기존 방식에서 부모 테이블 자체를 수정하는 방식으로 바뀌어
# 부모 테이블에 최종 루트 노드가 저장되게 됨. 따라서 추가적인 계산 없어짐(경로 압축)
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])

  return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  # 더 작은 숫자가 부모 노드가 되는 것으로 가정
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0 for _ in range(v + 1)]  # 부모 테이블 초기화

# 처음 부모는 자기 자신
for i in range(1, v + 1):
  parent[i] = i

# union 연산을 수행(e번 수행)
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("원소가 속한 집합: ", end='')
for i in range(1, v + 1):
  print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print("부모 테이블: ", end='')
for i in range(1, v + 1):
  print(parent[i], end=' ')
