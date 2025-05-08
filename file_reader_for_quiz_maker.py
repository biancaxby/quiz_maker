# Quiz file reader 
# Pseudocode
# Try to use the following: readlines, readfiles 
# Use startswith
# Make sure only 5 of the lines are printed each time


def file_reader():
    while True:
        subject = (input('What subject would you like?(math, english, science, history) (enter quit to go back) ')).lower()
        if subject == "quit":
             menu()
        try:
            quiz = open(f"{subject}.txt", 'r')
            lines = quiz.readlines()
            count_line = 0         # Counts how many lines 
            correct_answers = 0    # Counts how many correct answers 
            question_counter = 0

            while count_line < len(lines):
                for _ in range(5):      # Prints 5 lines of the text file
                    if count_line >= len(lines):
                         break      # Exits the loop if the file has no more lines

                    striped_lines = lines[count_line].strip()      # Separates each line

                    # Ignores blank lines and lines with the answer key
                    if striped_lines == "" or striped_lines.startswith("The correct answer is:"):
                        count_line += 1
                        continue
                        
                    print(striped_lines)  # Prints the question
                    count_line += 1

                    # Checks if the line is the answer key
                    if count_line < len(lines) and lines[count_line].startswith("The correct answer is:"):
                        answer = lines[count_line].replace("The correct answer is: ", "").strip()   # Separates the answer
                        count_line += 1

                        # Asks user for the answer to the question
                        user_answer = input('What do you think is the answer? ').lower().strip()
                        question_counter += 1      # Counts how many questions have been displayed

                        if  user_answer == answer:
                                print("Correct!")     # Prints correct if the answer is correct
                                correct_answers += 1  # Adds to the number of correct answers
                        if user_answer != answer:
                             print("Wrong!")          # Prints wrong is the answer is wrong
                        if user_answer == "quit":     # Returns to the menu 
                                menu()
                                return
            percentage = correct_answers / question_counter * 100
            print(f"You have scored {correct_answers} out of {question_counter}! Which means you have answered {percentage} of the questions correctly!")


        finally:
             quiz.close
                
def menu():
    while True:
        print('1. Start quiz')
        print('2. View scores')
        user_input = input("What would you like to do? ")
        if user_input == "1":
            file_reader()
        if user_input == "2":
            continue
        else:
            break
 

file_reader()
menu()