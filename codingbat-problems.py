def first_last6(nums):
  value = False
  if nums[0] == 6 or nums[len(nums) - 1] == 6:
    value = True
  return value

def common_end(a, b):
  value = False
  if a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]:
    value = True
  return value

def reverse3(nums):
  reverse = [nums[2],nums[1],nums[0]]
  return reverse

def middle_way(a, b):
  middle = [a[1],b[1]]
  return middle

def same_first_last(nums):
  value = False
  if len(nums) > 0: 
    if nums[0] == nums[-1]:
      value = True
  return value

def sum3(nums):
  sum = nums[0] + nums[1] + nums[2]
  return sum

def max_end3(nums):
  max = nums
  if nums[0] > nums[2]:
    max = [nums[0],nums[0],nums[0]]
  elif nums [0] < nums[2]:
    max = [nums[2],nums[2],nums[2]]
  else: 
    max = [nums[0],nums[0],nums[0]] 
  return max

def make_ends(nums):
  new = [nums[0],nums[-1]]
  return new

def make_pi():
  return [3,1,4]

def rotate_left3(nums):
  return [nums[1],nums[2],nums[0]]

def sum2(nums):
  if len(nums) == 0:
    return 0;
  elif len(nums) > 1:
    return nums[0] + nums[1]
  else:
    return nums[0]

def has23(nums):
  if nums[0] == 2:
    return True
  elif nums[1] == 2:
    return True
  elif nums[0] == 3:
    return True
  elif nums [1] == 3:
    return True
  else:
    return False
    
def count_evens(nums):
  count = 0
  for item in nums:
    if item % 2 == 0:
      count = count + 1
  return count

def big_diff(nums):
  largest = nums[0]
  smallest = nums[0]
  for item in nums:
    if item > largest:
      largest = item
    elif item < smallest:
      smallest = item
  return largest - smallest

def has22(nums):
  value = False
  counter = 0
  for item in nums:
    if counter != len(nums) - 1:
      if item == 2:
        if item == nums[counter+1]:
          value = True
    counter = counter + 1
  return value
    
def centered_average(nums):
  sum = 0
  counter = 0
  for item in nums:
    if item != min(nums) and item != max(nums):
      sum = sum + item
  return sum/(len(nums) - 2)
