# https://leetcode.com/problems/valid-anagram/description/
# 242. Valid Anagram
def isAnagram(s, t):
   """
   :type s: str
   :type t: str
   :rtype: bool
   """
   if len(s) != len(t):
      return False
   s_dic = {}
   t_dic = {}
   
   for i in s:
      if i in s_dic:
            s_dic[i] += 1
      else:
            s_dic[i] = 1
   for i in t:
      if i in t_dic:
            t_dic[i] += 1
      else:
            t_dic[i] = 1


   if s_dic == t_dic:
      return True
   else:
      return False
   
   
print(isAnagram("anagram","nagaram")) # True
print(isAnagram("rat", "car")) # Flase