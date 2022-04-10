from heap import BinaryHeap

global heap

heap = BinaryHeap()

# print(heap.toString())

heap.insert(int(10))
heap.insert(int(7))
heap.insert(int(20))
heap.insert(int(30))
heap.insert(int(40))
heap.insert(int(6))
heap.insert(int(9))



print(heap.toString())
print(heap.key())
