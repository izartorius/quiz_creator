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
    #Stores the data (questions, answers) extracted from the text files
    quiz = []
    #Take every 5 lines from the text file as a one question
    for i in range(0, len(lines), 5):
        question_block = lines[i:i+5]  # Grab 5 lines
        full_question = '\n'.join(question_block)  # Make a multiline question
        answer = answers[i // 5]  # Get the corresponding answer
        quiz.append((full_question, answer))
#Define function for running the quiz game
#Run the quiz with the loaded data