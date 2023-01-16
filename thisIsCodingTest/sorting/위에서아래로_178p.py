n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

# nums.sort() 대신 "nums = sorted(nums, reverse=True)"로 처리해 처음부터 내림차순으로 정렬하는 것도 가능
nums.sort()

for i in range(len(nums) - 1, -1, -1):
    print(nums[i], end=' 3')