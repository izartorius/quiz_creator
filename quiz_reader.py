#Define functions for loading the text files
def load_quiz(questions_file, answers_file):
    #Open and read the questions file
    with open(questions_file, 'r') as qf:
        #Strips all the spaces and blank lines in the text file
        lines = [line.strip() for line in qf if line.strip() != '']
    #Open and read the answers file
    with open(answers_file, 'r') as af:
        #Strips all the spaces and blank lines in the text file
        answers = [line.strip() for line in af if line.strip() != '']
#Remove all spaces in the text file
#Take every 5 lines from the text file as a one question
#Define function for running the quiz game
#Run the quiz with the loaded data