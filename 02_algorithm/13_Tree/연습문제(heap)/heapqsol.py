import heapq

hq = [3, 2, 1, 6, 7, 9]

heapq.heapify(hq)
print(hq)

heapq.heappush(hq,5)
print(hq)
heapq.heappush(hq,4)
print(hq)
print(heapq.heappop(hq))
print(heapq.heappop(hq))
print(heapq.heappop(hq))
