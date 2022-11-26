# Author: Dimitrios Ntentia, Kyle Drummonds
# Username: ntentiad drummondsk
#purpose: The purpose of the program is to give it your birth, and then it will tell you your mastery number
#acknowledgements: The program was created for the class of CSC 226

import time

def summing(i):
   '''We need our code to add the number, untill the sum is smaller than 10'''
   mainstr = str(i)
   while i > 9:
     i = int("0")
     for k in mainstr:
        k = int(k)
        i += k
     mainstr = str(i)
   return str(i)

def info(a):
    ''' This function prints information to the user regarding the meaning behind their life paths'''

    if int(a) == 1:

        print("Congratulations, your life path number is: " + a + "!")
        time.sleep(1)
        print("Guess what?")
        time.sleep(1)
        print("")
        print("You are a leader who values their independence.")
        time.sleep(2)
        print("You are innovative, independent and goal oriented.")
        time.sleep(2)
        print("Hold on there's more...")
        time.sleep(2)
        print("")
        print("Watch out for stubborn tendencies.")
        time.sleep(2)

    elif int(a) == 2:

        print("Congratulations, your life path number is: " + a + "!")
        time.sleep(1)
        print("Guess what?")
        time.sleep(1)
        print("")
        print("You are a diplomat with a gentle nature")
        time.sleep(2)
        print("You are influential, unifying and intuitive")
        time.sleep(2)
        print("Hold on there's more...")
        time.sleep(2)
        print("")
        print("Watch out for becoming too dependent on others.")
        time.sleep(2)

    elif int(a) == 3:

        print("Congratulations, your life path number is: " + a + "!")
        time.sleep(1)
        print("Guess what?")
        time.sleep(1)
        print("")
        print("You are a social butterfly with a positive attitude.")
        time.sleep(2)
        print("You are artistic, charming and communicative.")
        time.sleep(2)
        print("Hold on there's more...")
        time.sleep(2)
        print("")
        print("Watch out for scattered energy.")
        time.sleep(2)

    elif int(a) == 4:

        print("Congratulations, your life path number is: " + a + "!")
        time.sleep(1)
        print("Guess what?")
        time.sleep(1)
        print("")
        print("You are a hard worker with a practical streak.")
        time.sleep(2)
        print("You are loyal, practical and service-oriented")
        time.sleep(2)
        print("Hold on there's more...")
        time.sleep(2)
        print("")
        print("Watch out for narrow-mindedness.")
        time.sleep(2)

    elif int(a) == 5:

        print("Congratulations, your life path number is: " + a + "!")
        time.sleep(1)
        print("Guess what?")
        time.sleep(1)
        print("")
        print("You ar an intellectual with a taste for freedom. ")
        time.sleep(2)
        print("You are social, curious and adaptable")
        time.sleep(2)
        print("Hold on there's more...")
        time.sleep(2)
        print("")
        print("Watch out for irresponsibility.")
        time.sleep(2)

    elif int(a) == 6:

        print("Congratulations, your life path number is: " + a + "!")
        time.sleep(1)
        print("Guess what?")
        time.sleep(1)
        print("")
        print("You are a peacemaker with a loving nature. ")
        time.sleep(2)
        print("You are supportive, protective and romantic")
        time.sleep(2)
        print("Hold on there's more...")
        time.sleep(2)
        print("")
        print("Watch out for jealousy.")
        time.sleep(2)

    elif int(a) == 7:

        print("Congratulations, your life path number is: " + a + "!")
        time.sleep(1)
        print("Guess what?")
        time.sleep(1)
        print("")
        print("You are a profound thinker with a tendency for introspection.")
        time.sleep(2)
        print("You are spiritual, curious and analytical")
        time.sleep(2)
        print("Hold on there's more...")
        time.sleep(2)
        print("")
        print("Watch out for moodiness.")
        time.sleep(2)

    elif int(a) == 8:

        print("Congratulations, your life path number is: " + a + "!")
        time.sleep(1)
        print("Guess what?")
        time.sleep(1)
        print("")
        print("You are a manager with an ambitious side.")
        time.sleep(2)
        print("You are enduring, ambitious and karmic")
        time.sleep(2)
        print("Hold on there's more...")
        time.sleep(2)
        print("")
        print("Watch out for tension.")
        time.sleep(2)

    elif int(a) == 9:

        print("Congratulations, your life path number is: " + a + "!")
        time.sleep(1)
        print("Guess what?")
        time.sleep(1)
        print("")
        print("You are a teacher with a humanitarian nature.")
        time.sleep(2)
        print("You are tolerant, awakening and supportive")
        time.sleep(2)
        print("Hold on there's more...")
        time.sleep(2)
        print("")
        print("Watch out for restlessness. ")
        time.sleep(2)
    else:
        print("Congratulations, your life path number is: " + a + "!")


def main():
    '''This is where we are combining our code'''

    sum=0
    day=int(input("What day were you born on? (Please enter the value as digits): "))
    month=int(input("What month were you born in? (Please enter the value as digits): "))
    year=int(input("What year were you born in? (Please enter the value as digits): "))
    flag=0

    if month%11==0:
        flag = int(summing(day)) + int(month) + int((summing(year)))

        if flag!=11:
            sum = summing(int(summing(day)) + int(month) + int((summing(year))))
            info(sum)

        else:
            print("Congratulations, your life path number is: " + str(flag))
            time.sleep(1)
            print("Guess what?")
            time.sleep(1)
            print("Those with Master Number 11 tend to be even more sensitive to their environment and even have psychic abilities.")
            time.sleep(2)

    elif day%11==0:
        flag = int(summing(month)) + int(day) + int((summing(year)))

        if flag!=11:
            sum = summing(int(summing(month)) + int(day) + int((summing(year))))
            info(sum)

        else:
            print("Congratulations, your life path number is: " + str(flag))
            time.sleep(1)
            print("Those with Master Number 11 tend to be even more sensitive to their environment and even have psychic abilities.")
            time.sleep(2)

    elif day%11==0 and month%11==0:
        flag = int(summing(day)) + int(month) + int((summing(year)))

        if flag != 11:
            sum = (summing(day) + int(month) + int((summing(year))))
            info(sum)

        else:
            print("Congratulations, your life path number is: " + str(flag))
            time.sleep(1)
            print("Guess what?")
            time.sleep(1)
            print("Those with Master Number 11 tend to be even more sensitive to their environment and even have psychic abilities.")
            time.sleep(2)
    else:
        flag = int(summing(day)) + int(summing(month)) + int((summing(year)))

        if flag != 11:

            sum = summing(int(summing(day)) + int(summing(month)) + int((summing(year))))
            info(sum)

        else:
           print("Congratulations, your life path number is: " + str(flag))
           time.sleep(1)
           print("Guess what?")
           time.sleep(1)
           print("Those with Master Number 11 tend to be even more sensitive to their environment and even have psychic abilities.")
           time.sleep(2)

main()