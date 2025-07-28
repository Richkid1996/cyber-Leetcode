#Max Consecutive Ones 
#Given a binary nums, return the maximum number of consecutive 1's in the array.
#Explination: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

nums = [1,1,0,1,1,1]
#Use a variable like count to track current streak of 1s
count = 0
#Use another variable like max_count to store the longest streak so far
max_count = 0

for num in nums:
    if num == 1:
        count += 1 #This counts the number of one's in the list 
        max_count = max(max_count, count) #This updates the max count only if count is larger using the built in max function 
    else:
        count = 0
    
print(max_count)



# Find Numbers with Even Number of Digits
#Given an array nums of integers, return how many of them contain on even number of digits
#Explination: There are Five numbers listed in the array the objective is to find and count how many are even numbers

nums = [555, 901, 482, 1771]

#use a variable like count to track the number of even numbers in the array 
count = 0

for num in nums:
    if len(str(nums)) % 2 == 0:
        count += 1

print(count)


#Return an array of the squares of each number sorted in non-decreasing order 
#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.