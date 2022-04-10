from heap import MaxBinaryHeap

def findKthElement(a: list[int], k: int) -> int:
  if k not in range(1, len(a)):
    print('Sorry!\nKey out of available range :(\nTry again with number between 0 and ' + str(len(a)))
    return -1

  maxHeap = MaxBinaryHeap()
  
  for value in a:
    maxHeap.insert(value)
  
  for index in range(0, k):
    resultKey = maxHeap.extract()
    if index == k - 1:
      return resultKey
