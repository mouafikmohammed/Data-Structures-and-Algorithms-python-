# https://leetcode.com/problems/group-anagrams/
# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

def groupAnagrams(strs):
   """
   :type strs: List[str]
   :rtype: List[List[str]]
   """
   result_dict = dict()
   
   for _string in strs:
      
      
      sorted_string = ''.join(sorted(_string))
      
      if sorted_string not in result_dict:
         result_dict[sorted_string] = []
      
      result_dict[sorted_string].append(_string)
      
   return list(result_dict.values())

   
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))