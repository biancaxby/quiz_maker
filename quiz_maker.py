# Append the user's input to a txt file
def question_comp():
    while True:
        # Asks the user to choose a subject
        subjects = input('What subject? (math, science, english, history) or enter "quit": ').lower()
        if subjects == "quit":  # Quit option 
            main_menu()

        # Open file and append input to the text file
        questionares = open(f"{subjects}.txt", 'a')
        questionares.write(input(f"Enter a question: \n"))
        questionares.write(f"a) {input('Enter option a: ')}\n")
        questionares.write(f"b) {input('Enter option b: ')}\n")
        questionares.write(f"c) {input('Enter option c: ')}\n")
        questionares.write(f"d) {input('Enter option d: ')}\n")
        questionares.write(f'The correct answer is: {input('what is the right answer? a, b, c, or d? ')}\n\n ')
        questionares.close()  # Closes file
        print('Questions are saved!')

def file_edit():
    while True:
        subjects = input('What subject? (math, science, english, history) or enter "quit": ').lower()
        if subjects == "quit":
            main_menu()
            
        # Opens file and then prints it for the user to see contents
        questionares = open(f"{subjects}.txt", 'r')
        lines = questionares.readlines()

        # Adds numbering per line
        for i, line in enumerate(lines, 1):
            print(f"{i}) {line.strip()}")

        # Asks user what to change and then prints out the questions and their line number
        print('What would you like to change?')
        print(questionares.read)

        # User will choose what line to edit
        edit_line = int(input('What line would you like to change?(Enter 0 to cancel): '))
        if edit_line == 0:
            main_menu()   

        # Asks user what to replace
        edit_statement = input(f"Enter new content on line {edit_line}: \n")
            
        # Replaces the line with new content
        lines[edit_line - 1] = f"{edit_statement}\n"
            
        # Writes on the file again
        questionares = open(f"{subjects}.txt", 'w')
        questionares.writelines(lines)
        questionares.close()

def view_questions():
    while True:
        subjects = input('What subject? (math, science, english, history) or enter "quit": ').lower()
        if subjects == "quit":
            main_menu()
        questionares = open(f"{subjects}.txt", 'r')
        print(questionares.read())  # Prints all the questions stored on the text file

def main_menu():
    print('1. Create questions\n2. Edit questions\n3. See questions')
    user_input = input('What would you like to do?: ')
    if user_input == '1':
        question_comp()
    elif user_input == '2':
        file_edit()
    elif user_input == '3':
        view_questions()

main_menu()
view_questions()
file_edit()
question_comp()