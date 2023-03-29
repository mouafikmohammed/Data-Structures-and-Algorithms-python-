def quick_sort(arr):
   """
   Args:
      arr (list[int]): list[int]
   Returns:
      list[int]: sorted list
   """
   if len(arr) <= 1:
      return arr
   else:
      left = []
      right = []
      pivot = [arr[len(arr) - 1]]
      for i in range(len(arr)-1):
         if pivot[0] > arr[i]:
            left.append(arr[i])
         else:
            right.append(arr[i])
   
   return quick_sort(left) + pivot + quick_sort(right)

arr = [9,-3,5,2,6,8,-6,1,3]
print(quick_sort(arr))