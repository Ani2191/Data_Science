#!/usr/bin/env python
# coding: utf-8

# In[27]:


#WAP for a player to guess the number between 1 - 25 while the player has maximum 4 attempts to guess the number

#Step 1 - Take user input

n = input('Hello! What is your name : ')

print('Welcome',n,'.I am thinking of a number between 1 to 25')

#Step 2 - Validate the user input

while True:
    try:
        gc = int(input('Take a guess : '))
    except ValueError:
        print('Please enter an integer between 1 to 25')
        continue
    break


#Step 3 - Generate a random number between 1 to 25

import random as rd

cc = rd.randint(1,25)

# Step 4 - Initialize the loop

count = 1

while gc != cc:
    if (gc - cc) >= 3 :
        print('Your guess is too high')
    elif (gc-cc > 0) and (gc-cc < 3):
        print('Your guess is a bit high')
    elif (gc-cc < 0) and (gc-cc > -3):
        print('Your guess is a bit low')
    elif (gc-cc <= -3):
        print('Your guess is a too low')
    while True:
        try:
            gc = int(input('Take another guess : '))
        except ValueError:
            print('Please enter an integer between 1 to 25')
            continue
        break
    count+=1
    
#Step 5 - Break the loop if user exceeds max tries of 4    
    if count == 4:
        break

#Step 6 - print the end statements

if (gc == cc) and (count < 5):
    print(f'Good job {n}!. You guessed my number in',count,'chances')
else:
    print('You have exceeded 4 attempts. The answer I was looking for is',cc)
    


# In[ ]:




