# Do you know what Mississippi is? Well, it's the name of one of the states and rivers in the United States. 
# The word Mississippi is also used for a slightly different purpose: to count mississippily.

# If you're not familiar with the phrase, we're here to explain to you what it means: it's used to count seconds.

# The idea behind it is that adding the word Mississippi to a number when counting seconds aloud makes them sound closer to clock-time, 
# and therefore "one Mississippi, two Mississippi, three Mississippi" will take approximately an actual three 
# seconds of time! It's often used by children playing hide-and-seek to make sure the seeker does an honest count.

# Your task is very simple here: write a program that uses a for loop to "count mississippily" to five. 
# Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"

import time

for i in range(1,6):
    print(f"{i} Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")