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

    def run(self):
            """
            Runs the quiz by iterating over each question, prompting the user for an answer,
            and checking it against the correct answer.
            """
            # Loop through each question and its corresponding correct answer
            for question, correct_answer in self.quiz_data:
                print("\n" + question)  # Print the question (with multiple lines)
                user_answer = input("Your answer: ")  # Prompt user for an answer

                # Compare user input with correct answer (case-insensitive)
                if user_answer.strip().upper() == correct_answer.strip().upper():
                    print("Correct!")
                    self.score += 1  # Increment score if answer is correct
                else:
                    print(f"Wrong! The correct answer was: {correct_answer}")  # Show correct answer if wrong

            # Display final score after all questions are answered
            print(f"\nYour score: {self.score}/{len(self.quiz_data)}")


# Main program entry point
if __name__ == "__main__":
    # Create a Quiz instance with the paths to the question and answer files
    quiz = Quiz("quiz.txt", "answer.txt")

    # Load the quiz data from the files
    quiz.load_quiz()

    # Start running the quiz
    quiz.run()