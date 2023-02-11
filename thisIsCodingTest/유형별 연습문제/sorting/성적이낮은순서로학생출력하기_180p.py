n = int(input())
students = []

for _ in range(n):
    students.append(input().split())

for student in students:
    student[1] = int(student[1])

# sorted()의 key 속성에 기준이 되는 값을 반환하는 함수를 전달하면 그 값 기준으로 내림차순 정렬됨
students = sorted(students, key=(lambda student: student[1]))

for student in students:
    print(student[0], end=' ')