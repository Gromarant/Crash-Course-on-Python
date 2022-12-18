#----- Question: Can you work out what this function does? Try passing different parameters to the attempts function to see what it does. 
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)
    # Answer: This function print the value of 'x' while it is lower or equal to the 'n' parameter and print 'done' when 'x' is bigger than n or n is lower than x