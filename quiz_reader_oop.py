# Define the Quiz class to encapsulate all quiz-related functions
class Quiz:
    def __init__(self, questions_file, answers_file):
        self.questions_file = questions_file  # File containing quiz questions
        self.answers_file = answers_file      # File containing correct answers
        self.quiz_data = []                   # List to store tuples of (question, correct_answer)
        self.score = 0                        # Variable to track the user's score
