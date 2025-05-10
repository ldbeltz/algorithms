"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]
"""


def twoSum(nums: list[int], target: int) -> list[int]:
        goal_numbers_dict = {}
        result_array = []
        for i in range(len(nums)):
            goal = target - nums[i]
            index = goal_numbers_dict.get(goal)
            if index is not None:
                result_array.append(index)
                result_array.append(i)
                break
            else:
                goal_numbers_dict[nums[i]] = i
            
        return result_array
            
if __name__ == '__main__':
    nums = [2,1,4,1,2]
    target = 4
    print(twoSum(nums, target))