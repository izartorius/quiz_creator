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