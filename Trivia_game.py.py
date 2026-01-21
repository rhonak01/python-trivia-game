# list of questions
# store the answers
# randomly pick question
#  ask the questions
#  see if they are correct
# keep track of the score
# tell the user thire score
 
import random


questions = {
    "what is the keyword to define a function in python ?": "def",
    "which data type us used to store True ar false values?": "boolean",
    "what is the correct file extension for python files": ".py",
    "which symbol is used to get input in python ?":"input",
    "How do you start a for loop in python?":"for",
    "what does the len() function reaturn ?":"length",
    "What is the result of 10 // 3 in python? ":"3"
}

def py_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    
    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("your answer :  ").lower().strip()

        correct_answer = questions[question]
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"wrong. The correct answer is: {correct_answer}.\n")
 
    print(f"Game over! Your final score is : {score}/{total_questions}")




py_trivia_game()