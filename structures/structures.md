# Disjoint Set

Using N as the number of vertices in the graph and $\alpha$ as Inverse Ackermann function, we have:

|   |  **Union-find Constructor**  | **Find** | **Union** | **Connected**
| ------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
|  **Time Complexity** |  $O(N)$ | $O(\alpha(N))$ | $O(\alpha(N))$ | $O(\alpha(N))$



# Sorting

## Merge Sort

A usefull link for this sort algorithm is [Merge Sort](https://www.geeksforgeeks.org/merge-sort/). 

This algorithm is based on divide and  conquer paradigm.

Merge sort is a stable algorithm and is not in place one.

### Complexity

The time complexity of this algorithm is $O(NlogN)$ and the space complexity is $O(N)$ because it requires another array of space N.

### Drawbacks

Slower compared to the other sort algorithm for smaller tasks.

It requires additional memory space of $O(N)$.

It goes through the whole process even if the array is sorted.


## Quick Sort

A usefull link for this sort algorithm is [Quick Sort](https://www.geeksforgeeks.org/quick-sort/). 

This algorithm is based on divide and  conquer paradigm.

The worst case is when the pivot is always the biggest or smallest element. It can occur when the array is already sorted. In this case, the time complexity will be $O(n^2)$.

The best case is occurs when the partition process always picks the middle element as the pivot.

The default implementation is not stable. But, Quick Sort is in-place algorithm.

### Complexity

The time complexity of this algorithm is $O(NlogN)$ and the space complexity is $O(1)$.

## Insertion Sort

A usefull link for this sort algorithm is [Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/). 

This algorithm is similar to our approach of sorting cards on the hand.

The worst case case is if the array is sorted in the reverse order and it takes minimum time $O(n)$ if the array is already sorted.

This algorithm is stable and in-place. 

This algorithm is used to sort smaller arrays.

### Complexity

The time complexity of this algorithm is $O(n^2)$ and the space complexity is $O(1)$.


## Bucket Sort

The advanced to use bucket sort is when the elements are uniformly distributed over a range.

### Complexity

The time complexity of this algorithm is $O(n^2)$, but for distributed elements over a range, the time complexity is $O(n)$ and the space complexity is $O(n)$, because we use the buckets.