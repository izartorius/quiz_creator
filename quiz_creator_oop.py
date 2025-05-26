# Define a class to manage all quiz-related functionality
class QuizManager:
    def __init__(self, quiz_file, answer_file):
        #Initialize the QuizManager with file paths for storing questions and answers.
        self.quiz_file = quiz_file
        self.answer_file = answer_file

    def run(self):
        """
        Main loop to run the quiz creation interface.
        Continuously asks the user for input until they type 'Exit'.
        """
        with open(self.quiz_file, "a") as quiz, open(self.answer_file, "a") as answer:
            while True:
                # Get the quiz question from the user
                question = input("Add a question: ").capitalize()

                # Check for exit condition
                if question.lower() == "exit":
                    print("Saving inputs.. Exiting..")
                    break