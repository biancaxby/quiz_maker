# Quiz file reader 
# Pseudocode
# Try to use the following: readlines, readfiles 
# Use startswith
# Make sure only 5 of the lines are printed each time

usernames = []
correct_answers_list = []   # Storage for username, and score

def file_reader():
    while True:
        subject = (input('What subject would you like?(math, english, science, history) (enter quit to go back) ')).lower()
        if subject == "quit":
             menu()

        username = input("Enter your name: ")
        usernames.append(username)

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
            
            correct_answers_list.append(correct_answers)
            percentage = correct_answers / question_counter * 100    # Calculates the percentage of the score 
            print(f"Congrats {username}! You have scored {correct_answers} out of {question_counter}!\n Which means you have answered {percentage}% of the questions correctly!")
            
        finally:
             quiz.close()
                
def score_viewer():
    # Create a list of [username, score] pairs
    top_scorers = [[name, score] for name, score in zip(usernames, correct_answers_list)]    
    
    # Sort the list by score in descending order
    top_scorers.sort(key=lambda x: x[1], reverse=True)
    
    # Display the sorted scores
    print("Top Scorers:")
    for i, (name, score) in enumerate(top_scorers, 1):
        print(f"{i}. {name} {score} points")

def menu():
    while True:
        print('1. Start quiz')
        print('2. View scores')
        user_input = input("What would you like to do? ")
        if user_input == "1":
            file_reader()
        if user_input == "2":
            score_viewer()
        else:
            break

menu()
