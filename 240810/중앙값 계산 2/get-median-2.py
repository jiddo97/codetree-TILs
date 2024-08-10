import heapq

def add_number(num, low_heap, high_heap):
    if not low_heap or num <= -low_heap[0]:
        heapq.heappush(low_heap, -num)
    else:
        heapq.heappush(high_heap, num)
    
    if len(low_heap) > len(high_heap) + 1:
        heapq.heappush(high_heap, -heapq.heappop(low_heap))
    elif len(high_heap) > len(low_heap):
        heapq.heappush(low_heap, -heapq.heappop(high_heap))

def get_median(low_heap):
    return -low_heap[0]

n = int(input())
numbers = list(map(int, input().split()))

low_heap = []
high_heap = []

results = []

for i in range(n):
    add_number(numbers[i], low_heap, high_heap)
    
    if (i + 1) % 2 == 1:
        results.append(get_median(low_heap))

print(" ".join(map(str, results)))