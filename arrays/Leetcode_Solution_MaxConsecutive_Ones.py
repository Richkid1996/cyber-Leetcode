#Max Consecutive Ones 
#Given a binary nums, return the maximum number of consecutive 1's in the array.
#Explination: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

nums = [1,1,0,1,1,1]
def findMaxConsecutiveOnes(self, nums):
#Use a variable like count to track current streak of 1s
 count = 0
#Use another variable like max_count to store the longest streak so far
max_count = 0

for num in nums:
    if num == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
    
return max_count