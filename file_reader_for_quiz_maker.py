# Quiz file reader 
# Pseudocode
# Try to use the following: readlines, readfiles 
# Use startswith
# Make sure only 4 of the lines are printed each time

def file_reader():
    while True:
        subject = (input('What subject would you like?(math, english, science, history) ')).lower()
        quiz = open(f"{subject}.txt", 'r')
        count_line = 0   # Counts how many lines 

        # Separates each line
        for line in quiz:
            print(line.strip())
            count_line +=1      # Counts the line

            # Checks if the lines have reached the max quantity
            if count_line % 5 == 0:
                input('What do you think is the answer? ')
                next_line = next(quiz, None)
                print(next_line)

def menu():
    while True:
        user_input = input('Would you like to start now? (y/n) ').lower()
        if user_input == "y":
            file_reader()
        else:
            break
 
menu()
file_reader()
