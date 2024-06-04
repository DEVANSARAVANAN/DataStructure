import heapq
lst=[2,3,26,5,23,1,34]
heapq.heapify(lst)

heapq.heappush(lst,4)
print(list(lst))

while lst:
    print(heapq.heappop(lst))