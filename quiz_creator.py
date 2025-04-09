#Assign variables for the text files
quiz_file = "quiz.txt"
answer_file = "answer.txt"

#Open and manage the files
with open(quiz_file, "a") as quiz, open(answer_file, "a") as answer:
    #Loop sequence to constantly ask for user input
    while True:
        questions = input("Add a question: ")
        if questions == "exit":
            print("Saving inputs.. Exiting..")
            break

        #Add another user input for the choices and correct answers
        choices = []
        for option in ["A", "B", "C", "D"]:
            choice = input(f"Add choice {option}: ")
            choices.append((option, choice))

        correct_answer = input("Enter the correct answer: ")

