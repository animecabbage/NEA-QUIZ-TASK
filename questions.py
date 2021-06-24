import random
import time 

answers = ["a", "b", "c", "d"]
#used to check for a valid answer later

questionOneAnswer = "a"
questionTwoAnswer = "c"
questionThreeAnswer = "b"
questionFourAnswer = "b"
questionFiveAnswer = "d"
questionSixAnswer = "a"
questionSevenAnswer = "d"
questionEightAnswer = "b"
questionNineAnswer = "a"
questionTenAnswer = "d"
#choosing what option will be the answer ahead of time to prevent making 4 if statements per question

score = 0
#starting score

def start():
    print("Welcome to your tracker assessment!")
    print("Remember to answer the letter corresponding to the answer. Don't write out the answer, or the test won't recognise it")
#function to tell student all information that is needed
    


def questionOne(questionOneAnswer, answers, score):
    global newscore
    print("QUESTION ONE")
    print("What is the pH of hydrochloric acid?")
    print("a: 2")
    print("b: 20")
    print("c: -2")
    print("d: 8")
    questionOneInput = input()
    while questionOneInput.lower() not in answers:
        print("Answer not recognised, please try again")
        questionOneInput = input()
    if questionOneInput.lower() == questionOneAnswer:
        newscore = score + 1
        print("ANSWER SUBMITTED")
    else:
        print("ANSWER SUBMITTED")
        newscore = score
    return newscore

def QuestionTwo(questionTwoAnswer, answers, score):
    global newscore
    print("QUESTION TWO")
    print("What country has the capital Nairobi")
    print("a: South Africa")
    print("b: Jamaica")
    print("c: Kenya")
    print("d: Brazil")
    questionTwoInput = input()
    while questionTwoInput.lower() not in answers:
        print("Answer not recognised, please try again")
        questionTwoInput = input()
    if questionTwoInput.lower() == questionTwoAnswer:
        newscore = score + 1
        print("ANSWER SUBMITTED")
    else:
        print("ANSWER SUBMITTED")
        newscore = score
    return newscore 
    
    



start()
questionOne(questionOneAnswer, answers, score)
score = newscore
QuestionTwo(questionTwoAnswer, answers, score)
score = newscore


print(f"Your score was {score}")
