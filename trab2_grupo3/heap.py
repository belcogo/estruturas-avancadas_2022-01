class BinaryHeap:
  stringTree = ""
  # void
  def setInitialConfigs(self):
    self.pq = [None] * 10
    self.n = 0

  # void
  def __init__(self):
    self.setInitialConfigs()
  
  def PQ(self):
    self.clear()

  # returns boolean
  def isEmpty(self):
    return self.n == 0

  # returns int
  def size(self):
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
  def bottomUpHeapify(self, i):
    parent = int((i - 1) / 2)
    print(parent)
    if i > 0 and self.compareTo(parent, i):
      self.exchange(i, parent)
      self.bottomUpHeapify(parent)
  
  # void
  def topDownHeapify(self, i):
    index = int(i)
    temp = 2 * index + 1
    if (temp + 1) < self.n and self.compareTo(temp, temp + 1):
      temp = temp + 1
    if temp < self.n and self.compareTo(index, temp): 
      self.exchange(index, temp)
      self.topDownHeapify(temp)

  # void
  def exchange(self, i, j):
    indexI = int(i)
    indexJ = int(j)
    swap = self.pq[indexI]
    self.pq[indexI] = self.pq[indexJ]
    self.pq[indexJ] = swap

  # returns int
  def baseCompareTo(self, i, j):
    if (i is not None and j is None) or i > j: return 1
    if (i is None and j is not None) or i < j: return -1
    return 0
  
  # returns bool
  def compareTo(self, i, j):
    I = self.pq[int(i)]
    J = self.pq[int(j)]
    return self.baseCompareTo(I, J) > 0

  # void
  def increase(self, i, key):
    index = int(i)
    if index < 0 or index >= self.n:
      print("Invalid index!")
      return
    if self.compareTo(key, self.pq[index]) < 0:
      print("Key is less than the key in the priority queue!")
      return
    self.pq[index] = key

  # void
  def decrease(self, i, key):
    index = int(i)
    if index < 0 or index >= self.n:
      print("Invalid index!")
      return
    if self.compareTo(key, self.pq[index]) > 0:
      print("Key is less than the key in the priority queue!")
      return
    self.pq[index] = key

  # returns int
  def key(self):
    if self.isEmpty():
      print("Priority queue is empty")
    return self.pq[0]

  # void
  def insert(self, key):
    if self.n == len(self.pq):
      self.resize()
    self.pq[self.n] = key
    self.bottomUpHeapify(self.n)
    self.n = self.n + 1

  # returns int
  def extract(self):
    if self.isEmpty():
      print("Priority queue is empty")
    key = self.pq[0]
    self.n = self.n - 1
    self.exchange(0, self.n)
    self.topDownHeapify(0)
    self.pq[self.n] = None
    return key

  # returns string
  def toString(self):
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
    


