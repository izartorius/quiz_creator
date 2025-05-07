def load_quiz(filename):
    with open(filename, 'r') as quiz_file:  # Renamed variable to quiz_file
        lines = quiz_file.readlines()  # Reading lines from the file

    # Strip newline characters
    lines = [line.strip() for line in lines if line.strip() != '']

    # Pair questions and answers
    question_answer_pairs = []  # Renamed to avoid shadowing the passed 'quiz'
    for i in range(0, len(lines), 2):
        question = lines[i]
        answer = lines[i + 1]
        question_answer_pairs.append((question, answer))

    return question_answer_pairs  # Returning the list of question-answer pairs


def run_quiz(quiz):
    score = 0
    for question, correct_answer in quiz:
        user_answer = input(f"{question} ")
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}")
    print(f"\nYour score: {score}/{len(quiz)}")


# Example usage
filename = "quiz.txt"  # Replace with your actual file name
quiz = load_quiz(filename)  # Passing the filename correctly here
run_quiz(quiz)