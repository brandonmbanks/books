# Elements of Programming Interviews in Python
### 5. Arrays
Insertion into a full array can be handled by resizing, i.e., allocating a new array with additional memory and copying over the entries from the original array.

Deleting an element from an array entails moving over all successive elements one over to the left to fill the vacated space. Time complexity O(n - i) where i is the index.

When working with arrays you should take advantage of the fact that you can operate efficiently on both ends.
* seems similar to two pointer problems

Array problems often have simple brute-force solutions that use O(n) space, but there are subtler solutions that use the array itself to reduce space complexity to O(1).

Filling an array from the front is slow, so see if it's possible to write values from the back.

Instead of deleting an entry (which requires moving all entries to its right), consider overwriting it.

When dealing with integers encoded by an array consider processing the digits from the back of the array. Alternately, reverse the array so the least-significant digit is the first entry.
* [1, 2, 0, 0, 1]  # 12001

List comprehension supports multiple levels of looping. This can be used to create the product of sets, e.g., if `A = [1, 3, 5]` and `B = ['a', 'b']`, then `[(x, y) for x in A for y in B]` creates `[(1, 'a'), (1, 'b'), (3, 'a'), (3, 'b'), (5, 'a'), (5, 'b')]`. It can also be used to convert a 2D list to a 1D list, e.g., if `M = [['a', 'b', 'c'], ['d', 'e', 'f']]` `[x for row in M for x in row]` creates `['a', 'b', 'c', 'd', 'e', 'f']`.
