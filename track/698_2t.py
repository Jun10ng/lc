# 698 题第二次尝试
# 给定一个整数数组 nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
#
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
import copy
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = int(sum(nums) / k)
        ret,cnt = [],0
        visit ,i= [False] * len(nums),0
        # todo sort nums

        def track(curTarget: int,curPath,begin:int):
            nonlocal ret,cnt
            if curTarget<0:
                return False
            if curTarget==0:
                cnt += len(curPath)
                ret.append(copy.deepcopy(curPath))
                return True

            for i in range(begin+1,len(nums)):
                num = nums[i]
                if i >= len(visit):
                    return
                if visit[i]:
                    i += 1
                    continue
                visit[i] = True
                x = track(curTarget - num, curPath+[num],i)
                visit[i] = x
                if visit[i]:
                    # [3,2,2] 只能凑1对，不能凑2对
                    return True
                i += 1
            return False

        for num in nums:
            if num > target:
                return False

            if visit[i]:
                i+=1
                continue
            visit[i] = True
            track(target-num,[num],i)
            i+=1
        return cnt == len(nums)

if __name__  == '__main__':
    s = Solution()
    x = s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1],4)
    print(x)