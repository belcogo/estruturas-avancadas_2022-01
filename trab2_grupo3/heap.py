class BinaryHeap:
  def __init__(self):
    self.n = 0
    self.list = [None] * 10

  def resize(self):
    temp = [None] * (self.list.len() * 2)
    for index, value in enumerate(self.list):
      temp[index] = value
    self.list = temp

  def exchange(self, i, j):
    int swap = self.list[i]
    self.list[i] = self.list[j]
    self.list[j] = swap

  def compareTo(i, j):
    return i < j
  
  def isEmpty(self):
    return self.n == 0

  def bottomUpHeapfy(self, i):
    int parent = (i - 1) / 2
    if i > 0 and self.compareTo(parent, i):
      self.exchange(parent, i)
      self.bottomUpHeapfy(parent)
  
  def topDownHeapify(self, i):
    int temp = 2 * i + 1;
    if temp + 1 < n and self.compareTo(temp, temp + 1):
      temp++;
    if temp < n and compareTo(i, temp): 
      self.exchange(i, temp);
      self.topDownHeapify(temp);

  def increase(self, i, key):
    if i < 0 or i >= self.n:
      print('Invalid index!')
      return
    if self.compareTo(key, self.list[i]) < 0:
      print('Key is less than the key in the priority queue!')
    self.list[i] = key

  def decrease(self, i, key):
    if i < 0 or i >= self.n:
      print('Invalid index!')
      return
    if self.compareTo(key, self.list[i]) > 0:
      print('Key is less than the key in the priority queue!')
    self.list[i] = key
    
  def insert(self, key):
    if self.n == self.list.len():
      self.resize()
    self.list[self.n] = key
    self.bottomUpHeapfy(self.n++)

  def extract(self):
    if self.isEmpty():
      print('Priority queue is empty')
    key = self.list[0]
    self.exchange(0, --n)
    self.topDownHeapify(0)
    self.list[self.n] = null
    return key

