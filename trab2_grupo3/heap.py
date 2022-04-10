class MaxBinaryHeap:
  stringTree = ""
  # void
  def setInitialConfigs(self):
    self.pq = [None] * 10
    self.n = 0

  # void
  def __init__(self):
    self.setInitialConfigs()
  
  # void
  def PQ(self):
    self.clear()

  def isEmpty(self) -> bool:
    return self.n == 0

  def size(self) -> int:
    return self.n
  
  # void
  def clear(self):
    self.setInitialConfigs()

  # void
  def resize(self):
    temp = [None] * (len(self.pq) * 2)
    for index, value in enumerate(self.pq):
      temp[index] = value
    self.pq = temp

  # void
  def bottomUpHeapify(self, i: int):
    parent = int((i - 1) / 2)
    if i > 0 and self.compareTo(parent, i):
      self.exchange(i, parent)
      self.bottomUpHeapify(parent)
  
  # void
  def topDownHeapify(self, i: int):
    temp = 2 * i + 1
    if (temp + 1) < self.n and self.compareTo(temp, temp + 1):
      temp = temp + 1
    if temp < self.n and self.compareTo(i, temp): 
      self.exchange(i, temp)
      self.topDownHeapify(temp)

  # void
  def exchange(self, i: int, j: int):
    swap = self.pq[i]
    self.pq[i] = self.pq[j]
    self.pq[j] = swap

  def baseCompareTo(self, i, j) -> int:
    if (i is not None and j is None) or i > j: return 1
    if (i is None and j is not None) or i < j: return -1
    return 0
  
  def compareTo(self, i: int, j: int) -> bool:
    I = self.pq[int(i)]
    J = self.pq[int(j)]
    return self.baseCompareTo(I, J) < 0

  # void
  def increase(self, i: int, key: int):
    index = int(i)
    if index < 0 or index >= self.n:
      print("Invalid index!")
      return
    if self.compareTo(key, self.pq[index]) < 0:
      print("Key is less than the key in the priority queue!")
      return
    self.pq[index] = key

  # void
  def decrease(self, i: int, key: int):
    index = int(i)
    if index < 0 or index >= self.n:
      print("Invalid index!")
      return
    if self.compareTo(key, self.pq[index]) > 0:
      print("Key is less than the key in the priority queue!")
      return
    self.pq[index] = key

  def key(self) -> int:
    if self.isEmpty():
      print("Priority queue is empty")
    return self.pq[0]

  # void
  def insert(self, key: int):
    if self.n == len(self.pq):
      self.resize()
    self.pq[self.n] = key
    self.bottomUpHeapify(self.n)
    self.n = self.n + 1

  def extract(self) -> int:
    if self.isEmpty():
      print("Priority queue is empty")
    key = self.pq[0]
    self.n = self.n - 1
    self.exchange(0, self.n)
    self.topDownHeapify(0)
    self.pq[self.n] = None
    return key

  def toString(self) -> str:
    iMax = self.n - 1
    if (iMax == - 1): return "[]"

    b = "["
    for index, value in enumerate(self.pq):
      b = b + str(value)
      if index == iMax:
        return b + "]"
      b = b + ", "

  # # void
  # def callPrintTree(self):
  #   if self.n > 2: 
  #     self.printTree(2, True, "")

  #   self.stringTree = (str(self.pq[0]) + "\n")

  #   if self.n > 1:
  #     self.printTree(1, False, "")

  #   return self.stringTree

  # # void
  # def printTree(self, index, isRight, indent):
  #   rightChild = index * 2 + 2
  
  #   if rightChild < self.n:
  #     rightIndent = indent + "         " if isRight else " |        "
  #     self.printTree(rightChild, True, rightIndent)
    
  #   self.stringTree = self.stringTree + indent + ("/" if isRight else "\\") + str(self.pq[index]) + "\n"
  #   leftChild = index * 2 + 1
    
  #   if leftChild < self.n:
  #     leftIndent = indent + " |        " if isRight else "          "
  #     self.printTree(leftChild, False, leftIndent)
    


