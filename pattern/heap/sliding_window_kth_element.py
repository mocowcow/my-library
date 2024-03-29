from collections import Counter
from heapq import heappop, heappush
from typing import List


def SlidingWindowKthElement(nums: List[int], window_size: int, k: int) -> List[float]:
    N = len(nums)
    ans = []
    L = []  # max heap
    R = []  # min heap
    lazy = Counter()  # lazy removal count

    def get_value():
        # get k-th element
        return -L[0]

    # init window
    for i in range(window_size):
        heappush(L, -nums[i])
    # only keep k elements in max heap L
    while len(L) > k:
        heappush(R, -heappop(L))

    ans.append(get_value())

    # slide window
    for i in range(window_size, N):
        # bal<0: L has less
        # bal=0: balanced
        # bal>0: R has less
        bal = 0
        add = nums[i]

        # element to be removed
        rmv = nums[i-window_size]
        lazy[rmv] += 1

        # pop rmv from L
        if L and rmv <= -L[0]:
            bal -= 1
        else:
            bal += 1

        # insert n into L
        if L and add <= -L[0]:
            heappush(L, -add)
            bal += 1
        else:
            heappush(R, add)
            bal -= 1

        # make two heaps balanced
        if bal > 0:  # L>R, take largest one from L
            heappush(R, -heappop(L))
        elif bal < 0:  # L<R, take smallest one from R
            heappush(L, -heappop(R))

        # check if elements should be removed
        while L and lazy[-L[0]] > 0:
            lazy[-heappop(L)] -= 1

        while R and lazy[R[0]] > 0:
            lazy[heappop(R)] -= 1

        ans.append(get_value())

    return ans
