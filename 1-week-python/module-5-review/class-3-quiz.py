#----- Exercise 1: What is a computer program?
    # Answer: A step-by-step recipe of what needs to be done to complete a task, that gets executed by the computer.


#----- Exercise 2: What’s automation?
    # Answer: The process of replacing a manual step with one that happens automatically.


#----- Exercise 3: Which of the following tasks are good candidates for automation? Check all that apply.
    # Answer:
    # 2. Creating a report of how much each sales person has sold in the last month.
    # 3. Setting the home directory and access permissions for new employees joining your company.
    # 6. Populating your company's e-commerce site with the latest products in the catalog.


#----- Exercise 4: What are some characteristics of the Python programming language? Check all that apply.
    # Answer:
    # 1. Python programs are easy to write and understand.
    # 2. The Python interpreter reads our code and transforms it into computer instructions.
    # 4. We can practice Python using web interpreters or codepads as well as executing it locally. 


#----- Exercise 5: How does Python compare to other programming languages?
    # Answer: Each programming language has its advantages and disadvantages.


#----- Exercise 6: Write a Python script that outputs "Automating with Python is fun!" to the screen.
    # Answer: 
print("Automating with Python is fun!" )

# Output: Automating with Python is fun!


#----- Exercise 7: in the blanks so that the code prints "Yellow is the color of sunshine".
# color = ___
# thing = ___
# print(color + " is the color of " + thing)
    # Answer: 
color = "Yellow"
thing = "sunshine"
print(color + " is the color of " + thing)

# Output: Yellow is the color of sunshine


#----- Exercise 8: Keeping in mind there are 86400 seconds per day, write a program that calculates how many seconds there are in a week, if a week is 7 days.  Print the result on the screen. Note: Your result should be in the format of just a number, not a sentence.
    # Answer: 
secondsPerWeek= (86400*7)
print(secondsPerWeek)

# Output: 604800


#----- Exercise 9: Use Python to calculate how many different passwords can be formed with 6 lower case English letters.  For a 1 letter password, there would be 26 possibilities.  For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities.  Using this information, print the amount of possible passwords that can be formed with 6 letters.
    # Answer: 
PossibleCombinations= ((26)**6)
print(PossibleCombinations)

# Output: 308915776


#----- Exercise 10: Most hard drives are divided into sectors of 512 bytes each.  Our disk has a size of 16 GB. Fill in the blank to calculate how many sectors the disk has. Note: Your result should be in the format of just a number, not a sentence.
# disk_size = 16*1024*1024*1024
# sector_size = 512
# sector_amount = ___

# print(sector_amount)
    # Answer: 
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = ((disk_size)/sector_size)

print(sector_amount)

# Output: 33554432.0