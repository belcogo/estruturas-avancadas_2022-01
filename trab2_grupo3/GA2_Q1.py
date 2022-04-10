from heap import MaxBinaryHeap

def findKthElement(a: list[int], k: int) -> int:
  maxHeap = MaxBinaryHeap()
  
  for value in a:
    maxHeap.insert(value)
  
  for index in range(0, k):
    resultKey = maxHeap.extract()
    if index == k - 1:
      return resultKey
