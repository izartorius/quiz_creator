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

                    # Collect the choices for the question (A-D)
                    choices = self.collect_choices()

                    # Get the correct answer from the user and validate it
                    correct_answer = self.get_correct_answer(choices)

                    # Write the question and choices to the quiz file
                    self.write_question(quiz, question, choices)

                    # Write the correct answer to the answer file
                    self.write_answer(answer, correct_answer)

            print("JAGAAAAN! Transfer complete.")