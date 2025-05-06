# Quiz file reader 
# Pseudocode
# Try to use the following: readlines, readfiles 
# Use startswith
# Make sure only 4 of the lines are printed each time



def file_reader():
    while True:
        subject = (input('What subject would you like?(math, english, science, history) ')).lower()
        quiz = open(f"{subject}.txt", 'r')
        count_line = 0
        for line in quiz:
            print(line.strip())
            count_line +=1
            if count_line == 5:
                input("do you want to continue? yes or no?")
                if input == "yes":
                    continue
                if input == "no":
                    break

file_reader()