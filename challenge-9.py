# In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

# 1. take any non-negative and non-zero integer number and name it c0;
# 2. if it's even, evaluate a new c0 as c0 ÷ 2;
# 4. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# 4. if c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.

# Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. 
# We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.

user_input = int(input("Enter the number: "))

steps = 0 

while user_input != 1:
    if user_input % 2 == 0:
        user_input = user_input // 2
        steps +=1
    else:
        user_input = (3 * user_input) +1
        steps +=1
    print(user_input)

print(1) #last piece
print(steps, "steps")