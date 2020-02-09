# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。 
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#
# leetcode submit region end(Prohibit modification and deletion)

from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 因为是返回下标  而下标需要做一个dict把它与原来的数字对应上
        dict = {}
        for i, n in enumerate(nums):  # 这里的i就是返回的第二个index
            if target - n in dict:
                return [dict[target - n], i]  # 这里的i ==  dict[n] 但是这时候dict[n]还没存进去 所以要用i
            dict[n] = i


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))


d = {"key1": 10, "key2": 23}

if "key1" in d:
    print("this will execute")

if 10 in d:
    print("this will not")