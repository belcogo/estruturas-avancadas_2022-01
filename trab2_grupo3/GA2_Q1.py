from heap import MaxBinaryHeap

def findKthElement(a: list[int], k: int) -> int or str:
  if k not in range(1, len(a)):
    return 'Sorry!\nKey out of available range :(\nTry again with number between 0 and ' + str(len(a))

  maxHeap = MaxBinaryHeap()
  
  for value in a:
    maxHeap.insert(value)
  
  for index in range(0, k):
    resultKey = maxHeap.extract()
    if index == k - 1:
      return resultKey
