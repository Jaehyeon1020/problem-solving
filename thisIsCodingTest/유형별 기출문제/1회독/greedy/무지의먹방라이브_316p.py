from heapq import heappush, heappop


def solution(food_times, k):
  if sum(food_times) <= k:
    return - 1

  foodHeap = []
  length = len(food_times)  # 남은 음식 개수
  for i in range(length):
    heappush(foodHeap, [food_times[i], i + 1])

  time_prev = 0
  while (foodHeap[0][0] - time_prev) * length < k:
    k -= (foodHeap[0][0] - time_prev) * length
    time_prev = foodHeap[0][0]
    length -= 1
    heappop(foodHeap)

  result = sorted(foodHeap, key=lambda x: x[1])    # index를 기준으로 heap을 다시 정렬
  answer = result[k % length][1]
  return answer
