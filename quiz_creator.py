#Assign variables for the text files
quiz_file = "quiz.txt"
answer_file = "answer.txt"

#Open and manage the files
with open(quiz_file, "a") as quiz, open(answer_file, "a") as answer:
    #Loop sequence to constantly ask for user input
    while True:
        questions = input("Add a question: ").capitalize()
        if questions == "Exit":
            print("Saving inputs.. Exiting..")
            break

        #Add another user input for the choices and correct answers
        choices = []
        for option in ["A", "B", "C", "D"]:
            choice = input(f"Add choice {option}: ").title()
            choices.append((option, choice))

        valid_choice = [choice for _, choice in choices]
        correct_answer = ""
        while correct_answer not in valid_choice:
            correct_answer = input("Enter the correct answer: ").title()
            if correct_answer not in valid_choice:
                print("Invalid input. Try again.")
            elif correct_answer in valid_choice:
                break

            #Append all the inputs on their respective files
        quiz.write("Question: " + questions + "\n")
        for option, choice in choices:
            quiz.write(f"{option}. {choice}\n")
        quiz.write("-" * 50 + "\n")

        answer.write(f"{questions} " 
                     f"Answer: {correct_answer} \n")

    print("JAGAAAAN! Transfer complete.")