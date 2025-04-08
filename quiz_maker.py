import os

# Append the user's input to a txt file
def question_comp():
    while True:
        subjects = input('What subject? (math, science, english, history) or enter "quit": ').lower()
        if subjects == "quit":
            break

        # Open file and append input to the text file
        questionares = open(f"{subjects}.txt", 'a')
        questionares.write(input('Enter a question: ') + '\n')
        questionares.write('a) ' + input('Enter option a: ') + '\n')
        questionares.write('b) ' + input('Enter option b: ') + '\n')
        questionares.write('c) ' + input('Enter option c: ') + '\n')
        questionares.write('d) ' + input('Enter option d: ') + '\n\n')
        questionares.flush()
        questionares.close() 
        print('Questions are saved!')
        print(f"Saved to: {os.path.abspath(subjects + '.txt')}")  # Show full file path

question_comp()