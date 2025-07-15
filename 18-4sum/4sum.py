class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    
        # Check
        if len(nums) < 4:
            return []

        # sort the list
        nums.sort()

        i = 0

        result = []

        while i < len(nums):
            j = i + 1
            while j < len(nums):
                curr_sum = nums[i] + nums[j]
                m = j + 1
                n = len(nums) - 1

                while m < n:
                    rem_sum = nums[m] + nums[n]
                    if rem_sum == (target - curr_sum):
                        result.append([nums[i], nums[j], nums[m], nums[n]])
                        m += 1
                        n -= 1
                        while m < n and nums[m] == nums[m - 1]:
                            m += 1
                        while n > m and nums[n] == nums[n + 1]:
                            n -= 1
                    elif (target - curr_sum) > rem_sum:
                        m += 1
                        while m < n and nums[m] == nums[m - 1]:
                            m += 1
                    else:
                        n -= 1
                        while n > m and nums[n] == nums[n + 1]:
                            n -= 1

                # Remove duplicate nums[j]
                j += 1
                while j < len(nums) and nums[j] == nums[j - 1]:
                    j += 1

            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1

        return result
        