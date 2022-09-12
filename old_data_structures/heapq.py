
class PriorityQueue:

    def _init__(self):
        pass

    def heapfy(self, arr, n, i):

        smaller = i
        l = 2*i + 1
        r = 2*i + 2

        if l < n and arr[smaller] > arr[l]:
            smaller = l
        if r < n and arr[smaller] > arr[r]:
            smaller = r
        
        if smaller != i:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            self.heapfy(arr, n, smaller)

    def insert(self, arr, value):

        size = len(arr)
        arr.append(value)
        for i in range((size//2) -1, -1, -1):
            self.heapfy(arr, size+1, i)

    def delete(self, arr: list, value):

        size = len(arr)
        i = 0
        for i in range(0, size):
            if value == arr[i]:
                break

        arr[i], arr[size - 1] = arr[size - 1], arr[i]
        arr.remove(size - 1)
        for i in range((len(arr)//2) - 1, -1, -1):
            self.heapfy(arr, len(arr), i)


if __name__ == '__main__':

    arr = []
    pq = PriorityQueue()

    pq.insert(arr , 3)
    pq.insert(arr , 4)
    pq.insert(arr , 9)
    pq.insert(arr , 5)
    pq.insert(arr , 2)

    print ("The Max-Heap array is: " + str(arr))
    pq.delete(arr, 4)
    print("After deleting an element: " + str(arr))
