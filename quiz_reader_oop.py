# Define the Quiz class to contain all quiz-related functions
class Quiz:
    def __init__(self, questions_file, answers_file):
        self.questions_file = questions_file  # File containing quiz questions
        self.answers_file = answers_file      # File containing correct answers
        self.quiz_data = []                   # List to store tuples of (question, correct_answer)
        self.score = 0                        # Variable to track the user's score


def load_quiz(self):
    # Open and read the questions file, removing blank lines and extra spaces
    with open(self.questions_file, 'r') as qf:
        lines = [line.strip() for line in qf if line.strip() != '']

    # Open and read the answers file, also removing blank lines and extra spaces
    with open(self.answers_file, 'r') as af:
        answers = [line.strip() for line in af if line.strip() != '']

    # Process each question (5 lines per question block) and pair it with the corresponding answer
    for i in range(0, len(lines), 5):
        question_block = lines[i:i + 5]  # Get the current 5-line block
        full_question = '\n'.join(question_block)  # Join the lines into a single string with newlines
        answer = answers[i // 5]  # Get the corresponding answer from the answer list
        self.quiz_data.append((full_question, answer))  # Store the question and answer as a tuple