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