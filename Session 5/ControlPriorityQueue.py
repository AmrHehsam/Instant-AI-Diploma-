# The priority of the Priority Queue can be controlled using Heapq library by using either
# MaxHeap or MinHeap
import heapq


def custom_priority(element):
    return element[1]


priority_queue = []
heapq.heapify(priority_queue)

heapq.heappush(priority_queue, (3, 15))  # 3rd output
heapq.heappush(priority_queue, (1, 10))  # 1st output
heapq.heappush(priority_queue, (2, 5))   # 2nd output
heapq.heappush(priority_queue, (5, 20))  # 5th output
heapq.heappush(priority_queue, (4, 1))   # 4th output

while priority_queue:
    item = heapq.heappop(priority_queue)
    print(item)
