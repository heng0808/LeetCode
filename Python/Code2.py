# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        power1 = 1
        value1 = l1
        while value1:
            num1 = num1 + value1.val * power1
            value1 = value1.next
            power1 = power1 * 10

        num2 = 0
        power2 = 1
        value2 = l2
        while value2:
            num2 = num2 + value2.val * power2
            value2 = value2.next
            power2 = power2 * 10

        sum = num1 + num2
        if sum == 0:
            return ListNode(x=0)

        sum = str(sum)
        list = []
        for index in range(0, len(sum)):
            list.append(sum[index])
        list.reverse()

        result_node = None
        last_node = None
        for value in list:
            if result_node is None:
                result_node = ListNode(x=int(value))
                last_node = result_node
            else:
                last_node.next = ListNode(x=int(value))
                last_node = last_node.next

        return result_node

        # 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
        # 输出：7 -> 0 -> 8
        # 原因：342 + 465 = 807


if __name__ == '__main__':

    arr1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    l1 = None
    current1 = None
    for value in arr1:
        if l1 is None:
            l1 = ListNode(x=value)
            current1 = l1
        else:
            current1.next = ListNode(x=value)
            current1 = current1.next

    arr2 = [5,6,4]
    l2 = None
    current2 = None
    for value in arr2:
        if l2 is None:
            l2 = ListNode(x=value)
            current2 = l2
        else:
            current2.next = ListNode(x=value)
            current2 = current2.next

    Solution().addTwoNumbers(l1, l2)
