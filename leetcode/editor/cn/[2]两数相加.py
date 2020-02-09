# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学

class ListNode():
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k))
                         for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(
            self.gatherAttrs()) + "}"


class Solution:
    def addTwoNumbers(self, l1, l2 ,c = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        print('val=',val)
        c = val // 10
        print('c=',c)
        ret = ListNode(val % 10 )
        print('ret=',ret)
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret


l1 = [2, 4, 3]
l2 = [5, 6, 4]
if isinstance(l1, list):
    l1 = ListNode(l1)
    l2 = ListNode(l2)

print(Solution().addTwoNumbers(l1, l2))

print(l1)
print(l1.val)
print(l1.next)
print(l1.next.val)

print(122 / 60)
print(200 //50)
print(19//10)
print(25//10)

i = 122 % 60
print(i)
i = 122 % 11
print(i)
x= 200 % 48
print(x)