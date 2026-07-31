class Solution:

    def findMedianSortedArrays(
        self, nums1: list[int], nums2: list[int]
    ) -> float:
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        m, n, half = len(A), len(B), (len(nums1) + len(nums2) + 1) // 2
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = half - i

            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < m else float("inf")
            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < n else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if (m + n) % 2:
                    return float(max(A_left, B_left))
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            elif A_left > B_right:
                high = i - 1
            else:
                low = i + 1