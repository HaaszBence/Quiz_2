from functions.data_funcs import *
from os import system
from random import randint
from time import sleep

if __name__ == '__main__':
    SOURCE:str = 'data/QnA.csv'
    APP_NAME:str = "QUIZ"
    points = 0
    app_name_length:int = len(APP_NAME)
    qna_data:dict = read_data(SOURCE)
    qna_data_size:int = len(qna_data) - 1
    letters:list = ['A', 'B', 'C', 'D']
    
    tries:int = 3
    while tries > 0:
        
        system('cls')
        
        # Question -> [0]; Choices -> [1-4]; Correct answer id (within answers[0-3]) -> [5]
        current_data_idx = randint(0, qna_data_size)
        current_data = qna_data[current_data_idx]
        question:str = current_data[0]
        answers:list = current_data[1:5]
        correct_ans_idx:int = int(current_data[5])
        # print(f"{question}\n{answers}\n{correct_ans_idx}\n")

        print(f"{APP_NAME}\n")
        print(question)
        for i, letter in enumerate(letters):
            print(f"{letter}, {answers[i]}")
        
        user_inp = input("\nYour answer: ").upper()
        for i, letter in enumerate(letters):
            if letter == user_inp:
                if i == correct_ans_idx:
                    points += 1
                    print(f"Correct!\nYour points: {points}")
                    sleep(3)
                else:
                    tries -= 1
                    print(f"Incorrect!\nThe correct answer is {letters[correct_ans_idx]}\nLives remaining: {tries}")
                    sleep(3)
                break
    
    print("Thanks for playing the quiz!")