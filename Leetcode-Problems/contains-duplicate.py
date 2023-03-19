# https://leetcode.com/problems/contains-duplicate/description/
# 217. Contains Duplicate

def containsDuplicate(nums):
   """
   Args:
      nums (List[int]): an integer array nums
   Returns:
      bool: return true if any value appears at least twice
   """
   return len(unique_elements(nums))!= len(nums)

def mySet(arr):
   """
   Args:
      arr (List[int]): an integer array nums
   Returns:
      List[int]: return unique number as array (slow)
   """
   newArr = []
   for num in arr:
      if num not in newArr:
         newArr.append(num)
   return newArr


def unique_elements(arr):
   """
   Args:
      arr (List[int]): an integer array nums
   Returns:
      List[int]: return unique number as array (fast)
   """
   counts = {}
   for element in arr:
      if element in counts:
         counts[element] += 1
      else:
         counts[element] = 1
   return list(counts.keys())

print(containsDuplicate([1,2,3,1])) # true
print(containsDuplicate([1,2,3,4])) # false