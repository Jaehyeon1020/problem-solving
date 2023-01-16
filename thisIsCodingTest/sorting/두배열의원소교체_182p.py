n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    # b에서 가장 큰 원소가 a의 가장 작은 원소보다 작을 수 있으므로 확인 하고 교체
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(sum(a))