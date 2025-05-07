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

    #Returns the full quiz as a list of questions and answers
    return quiz

#Defines the function to run the quiz using the list of questions and answers
def run_quiz(quiz):
    score = 0 #Initialize score
    for question, correct_answer in quiz:
        print("\n" + question)  # Display the full question with choices
        user_answer = input("Your answer: ")
        if user_answer.strip().upper() == correct_answer.strip().upper():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}")
    print(f"\nYour score: {score}/{len(quiz)}")

#Run the quiz with the loaded data