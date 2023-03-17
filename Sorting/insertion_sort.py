# insertion sort with two for loop
def insertion_sort(arr):
   lenArr = len(arr)
   for i in range(1,lenArr):
      for j in range(i,0,-1):
         if arr[j-1] > arr[j ]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
         else:
            break
   
   return arr

# insertion sort with for loop and while loop
def insertion_sort2(arr):
   lenArr = len(arr)
   for i in range(1,lenArr):
      j = i -1
      while arr[j] > arr[j+1] and j >= 0:
         arr[j],arr[j+1] = arr[j+1],arr[j]
         j -= 1
   
   return arr


arr = [6,3,1,2,4]

print(insertion_sort2(arr))