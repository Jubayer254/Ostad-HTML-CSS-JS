# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each)
# and big bricks (5 inches each). 
# Return True, if it is possible to make the goal by choosing from the given bricks.
# This is a little harder than it looks and can be done without any loops.
# See also: Introduction to MakeBricks

# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

# WITH LOOP
def make_bricks(small, big, goal):
  while goal >= 5 and big > 0:
    goal = goal- 5
    big = big- 1
    
  while goal >= 1 and small > 0:
    goal = goal- 1
    small = small- 1
    
  if goal == 0:
    return True
    
  return False

# WITHOUT LOOP (STEP BY STEP)
def make_bricks(small, big, goal):
  while goal >= 5 and big > 0:
    goal = goal- 5
    big = big- 1
    
  while goal >= 1 and small > 0:
    goal = goal- 1
    small = small- 1
    
  return goal == 0

#--------------------------------------------------#

def make_bricks(small, big, goal):
  while goal >= 5 and big > 0:
    goal = goal- 5
    big = big- 1
    
  if small >= goal :
    return True
  else:
    return False
  
#--------------------------------------------------#

def make_bricks(small, big, goal):
  while goal >= 5 and big > 0:
    goal = goal- 5
    big = big- 1
    
  return small >= goal

#--------------------------------------------------#

def make_bricks(small, big, goal):
  big = big * 5
  
  if big >= goal:
    goal = goal % 5
  else:
    goal = goal - big
  
  return small >= goal



# Given a string, return a string where for every char in the original, there are two chars.

# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(string):
  li = list(string)
  li2 = []
  for x in li:
    for y in range (0, 2):
      li2.append(x)
  result = ''.join(li2)
  return result

def double_char(string):
  new_str = ''
  for c in string:
    new_str += c * 2
  return new_str
    

# Return True if the string "cat" and "dog" appear the same number of times in the given string.

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def find_occurrence(str, search):
  len_str = len(str)
  len_search = len(search)
  count = 0
  for i in range (0, len_str - len_search + 1):
    if str[i:i+len_search] == search:
      count = count + 1
  return count
  
def cat_dog(str):
  return find_occurrence(str, 'cat') == find_occurrence(str, 'dog')


# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7
# (every 6 will be followed by at least one 7). Return 0 for no numbers.

# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
  ignore = False
  sum = 0
  for x in nums:
    if ignore == False and x == 6:
      ignore = True
    if ignore == False:
      sum += x 
    if ignore == True and x == 7:
      ignore = False
  return sum
