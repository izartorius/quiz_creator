# Define a class to manage all quiz-related functionality
class QuizManager:
    def __init__(self, quiz_file, answer_file):
        #Initialize the QuizManager with file paths for storing questions and answers.
        self.quiz_file = quiz_file
        self.answer_file = answer_file