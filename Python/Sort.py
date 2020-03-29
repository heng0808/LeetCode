class ListNode:
    @staticmethod
    def quicksort(nums:[int]):
        def sort(left, right):
            if right <= left:
                return
            pointer = left + 1
            start_left = left
            while pointer <= right:
                if nums[pointer] < nums[left]:
                    num = nums[pointer]
                    del nums[pointer]
                    nums.insert(left, num)
                    left = left + 1
                pointer = pointer + 1
            sort(start_left, left - 1)
            sort(left + 1, right)

        sort(left=0, right=len(nums) - 1)

nums = [54, 26, 44, 17, 77, 31, 93, 55]
ListNode.quicksort(nums)