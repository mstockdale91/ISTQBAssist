import sys
from chapter import Chapter
from chaptercontents import *
from quiz import Quiz


#Welcome
def welcome():
    print("Welcome to the ISTQB Foundation Learning Assistant")
    print("This assistant was created as a practise project and may be incomplete!")

def printChapters():
    for chapter in chapter_names:
        chapterName = chapter_names[chapter]
        print(f"{chapter}: {chapterName}")

def tableOfContents() -> int:
    print("Please select one of the following chapters")
    printChapters()
    chapterNumber = int(input())
    if chapterNumber > 7 or chapterNumber < 1:
        print("Invalid, please select a number between 1 and 7")
        chapterNumber = int(input())
    print(f"You have selected {chapter_names[chapterNumber]}")
    return chapterNumber

def quit():
    print("Would you like to exit? Y/N")
    exit = input()
    if exit.lower() == "y":
        sys.exit()
    elif exit.lower() == "n":
        welcome()
    else:
        print("Invalid response, exiting...")
        sys.exit()


def main():
    welcome()
    
    takeAQuiz = False
    chapterNumber = tableOfContents()
    if chapterNumber == 7:
        takeAQuiz = True
    
    while not takeAQuiz:
        #open selected chapter
        chapter = Chapter(chapterNumber)
        subchapter = chapter.subContents()
        lastviewed = chapter.viewChapter(subchapter)
        
        if chapter.chapterComplete(lastviewed):
            print(f"You last viewed {chapter_names[chapterNumber]}: {chapter_contents[chapterNumber][lastviewed]}")
            print(f"You have completed the chapter {chapter_names[chapterNumber]}, would you like to take a quiz? Y/N")
            quiz = input()
            if quiz.lower == "y":
                takeAQuiz = True
            else:
                quit()
        else:
            quit()

    while takeAQuiz:
        printChapters()
        q = Quiz()
        quiz = q.createQuiz()
        score = q.takeQuiz(quiz)
        total = q.score(score, quiz)
        print("Would you like to take another quiz? Y/N")
        again = input()
        if again.lower() == "n":
            takeAQuiz = False

        #print("This part is under construction and no quizzes are available at this time")
    quit()


main()
