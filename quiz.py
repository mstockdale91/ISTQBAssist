#class to create the quiz - pull questions from csv file
import csv
import random

class Quiz():
    def __init__(self):
        print("Which Chapter would you like to take a quiz on? (1-6)")
        self.chapter_number = input()
        if int(self.chapter_number) >6 or int(self.chapter_number) <1:
            print("Invalid, please enter a number between 1 and 6")
            self.chapter_number = input()


    def createQuiz(self) -> dict:
        #pull several random questions from the csv that meet the chapter number
        questions = {}
        counter = 1
        with open ('questions.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:   
                if row['Chapter'] == self.chapter_number:
                    #print(row)
                    questions[counter] = {"Question": row['Question'],
                                          "Option_1": row['Option_1'],
                                          "Option_2": row['Option_2'],
                                          "Option_3": row['Option_3'],
                                          "Option_4": row['Option_4'],
                                          "Answer": row['Answer']}
                    #print(questions[counter])
                    counter += 1
        #print(f"TESING QUESTIONS: {questions}")
        #pull a set of random questions out of the dictionary to create the quiz
        a = list(range(1,counter))
        b = int(counter/2)
        random.shuffle(a)
        a = a[:b]
        quiz = {}
        for i in range(0,b):
            quiz[i+1] = questions[a[i]]
        print(f"Created a {len(quiz)} question quiz")

        return quiz
                
    def takeQuiz(self, quiz: dict) -> int:
        correct = 0
        #print(f"TESTING QUIZ {quiz}")
        for i in range(1, len(quiz)+1):
            print(quiz[i]["Question"])
            print(quiz[i]["Option_1"],quiz[i]["Option_2"],quiz[i]["Option_3"],quiz[i]["Option_4"])
            user_answer = input()
            if int(user_answer) > 4 or int(user_answer) < 1:
                print("Invalid, please input a number between 1 and 4")
                user_answer = input()
            if user_answer == quiz[i]["Answer"]:
                correct +=1
        return correct
        

    def score(self, correct: int, quiz: dict):
        total = float(correct/len(quiz))*100
        print(f"You got {total}% of questions correct")