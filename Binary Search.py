# Here I import the 'time' module, just for the somewhat soothing usage of 'time.sleep' pauses in between runs.
import time


# This is the definition of a binary search function 'search()' using recursion.
def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence,number, lower, middle)


# Definition of the main program function 'searching()' that calls the binary search function.
def searching():
    list1 = []
    counter = 0
    answers = {0: "first", 1: "second", 2: "third", 3: "fourth", 4: "fifth", 5: "sixth", 6: "seventh", 7: "eighth", 8: "ninth", 9: "last"}
    print("Welcome to Michael's binary search tool!")
    print("Please create a 10 element list by passing 10 whole numbers.")
    print(" ")
    time.sleep(1.5)


# This block of code runs until 10 numbers are successfully passed in as input. It also helps you keep count.
    for _ in range(10):
        while True:
            try:
                num = int(input("Input a number: "))
                list1.append(num)
                counter += 1
            except ValueError:
                print(" ")
                time.sleep(1.5)
                print("**********************************************************************************")
                print("|   " + "Uhh, theres's something not quite right with the 'number' you just typed in." + " |")
                print("|   " + "It has to be a whole number." + "                                                 |")
                print("|   " + "Please try again. You still need " + str(10 - counter) + " more numbers." + "                             |")
                print("**********************************************************************************")
                print(" ")
                time.sleep(2)
            else:
                break


# This block of code informs the program to sort the 10 provided numbers if they weren't provided in an already sorted order.
    print(" ")
    time.sleep(1)
    print(list1)
    time.sleep(2.5)
    #If the list most likely ISN'T sorted, the code sorts it for you
    if not sorted(list1):
        print("Something looks off. Let's sort it shall we?")
        list1.sort()
        time.sleep(2.5)
        print(" ")
        print("Much better, have a look: ")
        time.sleep(1.5)
        print(list1)
    # If the numbers suprisingly already were sorted, the code proceeds
    print(" ")
    time.sleep(2.5)
    print("----------------------------------------------")


# This block of code requests for the user to input a number that is present in their list, proceeds to check its index, then stores the result.
    while True:
        try:
            find = int(input("What number's position do you want?: "))
            print("----------------------------------------------")
            print(" ")
            answer = search(list1, find, 0, 10)
        except Exception as _:
            print("Invalid action.")
            time.sleep(2.5)
            print("Please input a 'number' that is actually contained in your list.")
            print("----------------------------------------------")
            print(" ")
            time.sleep(2.5)
        else:
            break


# The program displays the result to the user.
    time.sleep(2)
    print("The number " + str(find) + " is the " + answers[answer] + " number on the list.")
    print(" ")
    _ = input("Press ENTER to terminate: ")


# The main function 'searching()' is called.
searching()
    