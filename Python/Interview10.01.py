class Solution:
    def merge(self, A: [int], m: int, B: [int], n: int) -> None:
        sorted = []
        while len(B) > 0 or len(A) > n:
            if len(B) > 0 and len(A) > n:
                if A[0] < B[0]:
                    sorted.append(A.pop(0))
                else:
                    sorted.append(B.pop(0))
            elif len(B) == 0:
                sorted.append(A.pop(0))
            elif len(A) == n:
                sorted.append(B.pop(0))
        A[:] = sorted

Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)