#----- Question: The is_positive function should return True if the number received is positive, otherwise it returns None. Can you fill in the gaps to make that happen?
# def is_positive(number):
#   if ___:
#     return ___
    # Answer: 
def is_positive(number):
  if number > 0:
    return True
  if number < 0:
    return None

is_positive(-5)
is_positive(0) 
is_positive(13)

# Output: 
    # None
    # None
    # True