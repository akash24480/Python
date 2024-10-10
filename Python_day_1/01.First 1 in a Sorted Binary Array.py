

class Solution:
    def firstIndex(self, arr):
      
      position = 0

      while position < len(arr):
          if arr[position] == 1:
              return position
          position += 1

      return -1