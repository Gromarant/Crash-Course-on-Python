#----- Exercise 1: In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. The friends decide to split the bill evenly between them, after adding 15% tip for the service. Calculate the tip, the total amount to pay, and each friend's share, then output a message saying "Each person needs to pay: " followed by the resulting number.
# bill = ___
# tip = bill * ___
# total = bill + ___
# share = ___
# print("")
    # Answer:
bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total/2
print("Each person needs to pay: " + str(share))

# Output: Each person needs to pay: 27.186


#----- Exercise 2: This code is supposed to take two numbers, divide one by another so that the result is equal to 1, and display the result on the screen. Unfortunately, there is an error in the code. Find the error and fix it, so that the output is correct.
# numerator = 10
# denominator = 0
# result = numerator / denominator
# print(result)
    # Answer:
numerator = 10
denominator = 10
result = numerator / denominator
print(result)

# Output: 1.0


#----- Exercise 3: Combine the variables to display the sentence "How do you like Python so far?"
# word1 = "How"
# word2 = "do"
# word3 = "you"
# word4 = "like"
# word5 = "Python"
# word6 = "so"
# word7 = "far?"

# print(___)
    # Answer:
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print( word1 + ' ' + word2 + ' ' + word3 + ' ' + word4 + ' ' + word5 + ' ' + word6 + ' ' + word7 )

# Output: How do you like Python so far?


#----- Exercise 4: This code is supposed to display "2 + 2 = 4" on the screen, but there is an error. Find the error in the code and fix it, so that the output is correct.
# print("2 + 2 = " + (2 + 2))
    # Answer:
print("2 + 2 = " + str(2 + 2))

# Output: 2 + 2 = 4


#----- Exercise 5: What do you call a combination of numbers, symbols, or other values that produce a result when evaluated?
    # Answer: An expression