#----- Exercise 1: What is recursion used for?
    # Answer: Recursion lets us tackle complex problems by reducing the problem to a simpler one.


#----- Exercise 2: Which of these activities are good use cases for recursive programs? Check all that apply.
    # Answer: 
    # 1: Going through a file system collecting information related to directories and files.
    # 2: Managing permissions assigned to groups inside a company, when each group can contain both subgroups and users.


#----- Exercise 3: Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can return the result of a comparison.
# def is_power_of(number, base):
  # Base case: when number is smaller than base.
  # if number < base:
    # If number is equal to 1, it's a power (base**0).
    # return __

  # Recursive case: keep dividing number by base.
  # return is_power_of(__, ___)

# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64,4)) # Should be True
# print(is_power_of(70,10)) # Should be False
    # Answer: 
def is_power_of(number, base):
  number = number/base
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return False
  else:
    return True

  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

# Output: 
  # True
  # True
  # False


#----- Exercise 4: The count_users function recursively counts the amount of users that belong to a group in the company system, by going through each of the members of a group and if one of them is a group, recursively calling the function and counting the members. But it has a bug! Can you spot the problem and fix it?
# def count_users(group):
#   count = 0
#   for member in get_members(group):
#     count += 1
#     if is_group(member):
#       count += count_users(member)
#   return count

# print(count_users("sales")) # Should be 3
# print(count_users("engineering")) # Should be 8
# print(count_users("everyone")) # Should be 18
    # Answer: 
def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count += count_users(member) -1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18

# Output: 
  # 3
  # 8
  # 18


#----- Exercise 5: Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.
# def sum_positive_numbers(n):
#   return 0

# print(sum_positive_numbers(3)) # Should be 6
# print(sum_positive_numbers(5)) # Should be 15
    # Answer: 
def sum_positive_numbers(n):
  sum = 0
  if (n <= 1):
    return n
  else:
    sum+= n + sum_positive_numbers(n-1)
    return sum
 
print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# Output: 
  # 6
  # 15