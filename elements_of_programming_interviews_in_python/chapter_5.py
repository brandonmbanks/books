def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A


def dutch_flag_partition(pivot_index, a):
    pivot = a[pivot_index]

    smaller = 0

    # first pass: group elements smaller than pivot
    # 3, [5, 3, 2, 3, 7, 1, 2, 0]
    for i in range(len(a)):
        if a[i] < pivot:
            a[i], a[smaller] = a[smaller], a[i]
            smaller += 1

    # second pass: group elements larger than pivot
    larger = len(a) - 1
    for i in reversed(range(len(a))):
        print(i)
        if a[i] < pivot:
            break
        elif a[i] > pivot:
            a[i], a[larger] = a[larger], a[i]
            larger -= 1

    return a


def add_one(D):
    D[-1] += 1
    for i in reversed(range(len(D))):
        if D[i] != 10:
            break
        if i != 0:
            D[i] = 0
            D[i - 1] += 1

    if D[0] == 10:
        D[0] = 0
        D.insert(0, 1)

    return D


def can_reach_end(A):
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0

    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1

    return furthest_reach_so_far >= last_index


# input will be a sorted list of ints
# [2, 3, 5, 5, 7, 11, 11, 11, 13]
def deleted_duplicates(A):
    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1

    return write_index
    # seen = set()
    # removed = len(A) - 1

    # for i, val in enumerate(A):
    #     if val in seen:
    #         A[i], A[removed] = A[removed], 0
    #     else:
    #         seen.add(val)
    # print(A)


print(deleted_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13]))
