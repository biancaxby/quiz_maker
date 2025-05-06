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
            question_count = 0

            while count_line < len(lines):
                question_storage = []         # Stores the qestions here so that it is easier to deal with
                if lines.isspace:      # Checks if the line is empty or only has space
                    count_line += 1   
                for i in range(5):
                    if count_line + i < len(lines):
                            question_count.append(lines[question_count + i].strip())

            # Separates each line
            for line in lines:
                print(line.strip())
                count_line +=1      # Counts the line
                
                user_answer = input('What do you think is the answer? ').strip
                
                # Checks if the line is the answer key
                if count_line < len(lines) and lines[count_line].startswith("The correct answer is:"):
                    answer = lines[count_line].split(":")[1].strip()   # Separates the answer
                    count_line += 1
                    
                if  user_answer == answer:
                    print("\033[32mCorrect!!\033[0m")
                    correct_answers += 1
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