# Quiz file reader 
# Pseudocode
# Try to use the following: readlines, readfiles 
# Use startswith
# Make sure only 5 of the lines are printed each time


def file_reader():
    while True:
        
        subject = (input('What subject would you like?(math, english, science, history) ')).lower()
        try:
            quiz = open(f"{subject}.txt", 'r')
            lines = quiz.readlines()
            count_line = 0         # Counts how many lines 
            correct_answers = 0    # Counts how many correct answers 
            answer_key = []
            
            while count_line < len(lines):
                for _ in range(5):      # Prints 5 lines of the text file
                    if count_line < len(lines):
                            striped_lines = lines[count_line].strip()
                            
                    if striped_lines.startswith("The correct answer is:"):      # Ignores the lines containing the answer key
                        count_line += 1
                        continue
                    
                    if striped_lines == "":    # Ignores blank or empty lines
                        count_line += 1
                        continue
                    
                    print(striped_lines)
                    count_line += 1

                # Checks if the line is the answer key
                    if count_line < len(lines) and lines[count_line].startswith("The correct answer is:"):
                        answer = lines[count_line].replace("The correct answer is: ", "").strip()   # Separates the answer
                        answer_key.append(answer)
                        count_line += 1

                user_answer = input('What do you think is the answer? ').lower().strip()
                if  user_answer == answer_key:
                        print("correct!")
                        correct_answers += 1

                if user_answer == "quit":
                        menu()
                        return

        except ValueError:
            print('Invalid input')
                
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