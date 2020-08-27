# Program to guess user input.

"""
Name : GUESSING NUMBER GAME / Total 5 user trials
Author : Zohaib Asim Khan 
Description : Take number as input from user and prints trials... Random number Range is 1 to 10. \
Number of trials will be 5.
Date :  8th July 2015
"""

import random
ran_num = random.randint(1,10)

user_name = input("Enter your name... ")
print("Well", user_name, ", I am expecting number within range 1 to 10.")

proceed = input("\n\nEnter Y to proceed towards execution or N to end the program. ")
confirm = proceed.lower()


if confirm == 'y' or confirm == 'yes':
    
    print()

    trials = 1

    while trials < 6:
        guess = int(input("Enter a number? "))

        if guess < ran_num:
            print("You entered smaller number.")
            trials +=1

        if guess > ran_num:
            print("You entered greater number.")
            trials +=1


        if guess == ran_num:
            break

    if guess == ran_num:
        print("Congratulations" , user_name + "," + " you guessed a number in", trials, "trials.")
        raise SystemExit

    else:
        print("Trials are over! Actual number is", ran_num)
        raise SystemExit


elif confirm == 'n' or confirm == 'no':
    print("**** THE END ****")
    raise SystemExit

else:
    print("Program terminated due to invalid user input.")
    raise SystemExit
    


    

    
