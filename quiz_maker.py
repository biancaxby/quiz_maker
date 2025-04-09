import os
import fileinput

class QuizMaker:

    # Append the user's input to a txt file
    def question_comp(self):
        while True:

            # Asks the user to choose a subject
            subjects = input('What subject? (math, science, english, history) or enter "quit": ').lower()
            if subjects == "quit":  # Quit option 
                break

            # Open file and append input to the text file
            questionares = open(f"{subjects}.txt", 'a')
            questionares.write(input(f'Enter a question: ') + '\n')
            questionares.write(f'a) {input('Enter option a: ')}\n')
            questionares.write(f'b) {input('Enter option b: ')}\n')
            questionares.write(f'c) {input('Enter option c: ')}\n')
            questionares.write(f'd) {input('Enter option d: ')}\n\n')
            questionares.write(f'What is the correct answer? {input(' a, b, c, or d?')} ')
            questionares.flush()  # Forces pthon to write in the text file
            questionares.close()  # Closes file
            print('Questions are saved!')

    def file_edit(self):
        while True:
            subjects = input('What subject? (math, science, english, history) or enter "quit": ').lower()
            if subjects == "quit":
                break
            
            # Opens file and then prints it for the user to see contents
            questionares = open(f"{subjects}.txt, 'r'")
            lines = questionares.readlines()
            for i, line in enumerate(lines, 1):
                print(f"{i}) {line.strip()}")
            
            