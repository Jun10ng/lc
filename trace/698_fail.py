# 给定一个整数数组 nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
#
#
#
#  示例 1：
#
#
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
#
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tsum = sum(nums)
        n = len(nums)

        # nums.sort(reverse=True)
        if tsum % k is not 0:
            return False
        partSum = int(tsum/k)
        for v in nums:
            if v > partSum: return False
        # if nums[0]>partSum: return False

        used = [False] * len(nums)

        def track(begin:int,target:int,tk)->bool:
            if not tk:
                return True

            if target < 0:
                return False

            if not target:
                 return track(0,partSum,tk-1)

            for idx in range(begin,n):
                if not used[idx]:
                    used[idx] = True
                    num = nums[idx]
                    ans = track(idx+1,target-num,tk)
                    if ans: return True
                    used[idx] = False
            return False

        return track(0,partSum,k)

    def canPartitionKSubsets2(self,nums, k):
        n = len(nums)
        tsum = sum(nums)

        if tsum % k != 0:
            return False
        target = tsum / k
        # 排序剪枝
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        used = [False] * n  # 把数组分为两部分：已经满足target的group元素和待处理的剩下元素

        def dfs(cur, begin, k):
            if k == 0:
                return True
            if cur > target:
                return False
            if cur == target:
                return dfs(0, 0, k - 1)  # 剩下的元素是否能被等和分割成k-1份
            for i in range(begin, n):
                if not used[i]:
                    used[i] = True
                    if dfs(cur + nums[i], i + 1, k):  # 加上当前元素后能否被等和分割成k份
                        return True
                    used[i] = False  # 可以帮助下一组（k-1）与这一组的元素区分开来
            return False

        return dfs(0, 0, k)


if __name__ == '__main__':
    s = Solution()
    # print(s.canPartitionKSubsets([3,3,10,2,6,5,10,6,8,3,2,1,6,10,7,2],6))
    # print(s.canPartitionKSubsets([2,9,4,7,3,2,10,5,3,6,6,2,7,5,2,4], 7))

    print(s.canPartitionKSubsets2([3,3,10,2,6,5,10,6,8,3,2,1,6,10,7,2],6))
    print(s.canPartitionKSubsets2([2,9,4,7,3,2,10,5,3,6,6,2,7,5,2,4], 7))

