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

    def collect_choices(self):
        """
        Collects four multiple-choice options (A, B, C, D) from the user.
        Returns a list of (letter, choice) tuples.
        """
        choices = []
        for option in ["A", "B", "C", "D"]:
            choice = input(f"Add choice {option}: ").title()
            choices.append((option, choice))
        return choices

    def get_correct_answer(self, choices):
        """
        Prompts the user to input the correct answer.
        Repeats until a valid choice (one of the entered options) is given.
        Returns the correct answer string.
        """
        valid_choices = [choice for _, choice in choices]
        while True:
            answer = input("Enter the correct answer: ").title()
            if answer in valid_choices:
                return answer
            print("Invalid input. Try again.")

    def write_question(self, quiz_file, question, choices):
        quiz_file.write("Question: " + question + "\n")
        for option, choice in choices:
            quiz_file.write(f"{option}. {choice}\n")

    def write_answer(self, answer_file, correct_answer):
        answer_file.write(correct_answer + "\n")

# Specify file names for storing quiz questions and answers
quiz_file = "quiz.txt"
answer_file = "answer.txt"

# Create an instance of QuizManager with the file paths
quiz_app = QuizManager(quiz_file, answer_file)

# Start the quiz creation loop
quiz_app.run()

print("JAGAAAAN! Transfer complete.")