class BinaryHeap:
  stringTree = ""
  # void
  def setInitialConfigs(self):
    self.n = 0
    self.pq = [None] * 10

  # void
  def __init__(self):
    self.setInitialConfigs()

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
  def bottomUpHeapfy(self, i):
    index = int(i)
    parent = int((index - 1) / 2)
    if index > 0 and index <= self.n and self.compareTo(parent, index):
      self.exchange(index, parent)
      self.bottomUpHeapfy(parent)
  
  # void
  def topDownHeapify(self, i):
    index = int(i)
    temp = 2 * index + 1
    if temp + 1 < self.n and self.compareTo(temp, temp + 1):
      temp = temp + 1
    if temp < self.n and self.compareTo(index, temp): 
      self.exchange(index, temp)
      self.topDownHeapify(temp)

  # void
  def exchange(self, i, j):
    indexI = int(i)
    indexJ = int(j)
    swap = int(self.pq[indexI])
    self.pq[indexI] = self.pq[indexJ]
    self.pq[indexJ] = swap

  # returns boolean
  def compareTo(self, i, j):
    return int(i) < int(j)

  # void
  def increase(self, i, key):
    index = int(i)
    if index < 0 or index >= self.n:
      print("Invalid index!")
      return
    if self.compareTo(key, self.pq[index]) < 0:
      print("Key is less than the key in the priority queue!")
    self.pq[index] = key

  # void
  def decrease(self, i, key):
    index = int(i)
    if index < 0 or index >= self.n:
      print("Invalid index!")
      return
    if self.compareTo(key, self.pq[index]) > 0:
      print("Key is less than the key in the priority queue!")
    self.pq[index] = key

  # returns int
  def key(self, i):
    index = int(i)
    if self.isEmpty():
      print("Priority queue is empty")
    return self.pq[index]

  # void
  def insert(self, key):
    if self.n == len(self.pq):
      self.resize()
    self.pq[self.n] = key
    self.n = self.n + 1
    self.bottomUpHeapfy(self.n + 1)

  # returns int
  def extract(self):
    if self.isEmpty():
      print("Priority queue is empty")
    key = self.pq[0]
    self.exchange(0, self.n - 1)
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

  # void
  def callPrintTree(self):
    if self.n > 2: 
      self.printTree(2, True, "")

    self.stringTree = (str(self.pq[0]) + "\n")

    if self.n > 1:
      self.printTree(1, False, "")

    return self.stringTree

  # void
  def printTree(self, index, isRight, indent):
    rightChild = index * 2 + 2
  
    if rightChild < self.n:
      rightIndent = indent + "         " if isRight else " |        "
      self.printTree(rightChild, True, rightIndent)
    
    self.stringTree = self.stringTree + indent + ("/" if isRight else "\\") + str(self.pq[index]) + "\n"
    leftChild = index * 2 + 1
    
    if leftChild < self.n:
      leftIndent = indent + " |        " if isRight else "          "
      self.printTree(leftChild, False, leftIndent)
    


