#  3asum Medium Leetcode
class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sort the array
        n = len(nums)
        triplets = []

        for i in range(n-2):  # Iterate till n-2 to avoid out of bounds since we need at least 3 numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first number

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates for the second number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates for the third number
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # Move left pointer to increase the sum
                else:
                    right -= 1  # Move right pointer to decrease the sum

        return triplets  # Return the list of triplets
