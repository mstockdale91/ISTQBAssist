import sys
from chapter import Chapter
from chaptercontents import *


#Welcome
def welcome():
    print("Welcome to the ISTQB Foundation Learning Assistant")
    print("This assistant was created as a practise project and may be incomplete!")

def tableOfContents() -> int:
    print("Please select one of the following chapters")
    for chapter in chapter_names:
        chapterName = chapter_names[chapter]
        print(f"{chapter}: {chapterName}")
    chapterNumber = int(input())
    print(f"you have selected {chapter_names[chapterNumber]}")
    return chapterNumber

def quit():
    print("Would you like to exit? Y/N")
    exit = input()
    if exit.lower() == "y":
        sys.exit()


def main():
    welcome()
    
    takeAQuiz = False
    while not takeAQuiz:
        chapterNumber = tableOfContents()
        #open selected chapter
        chapter = Chapter(chapterNumber)
        subchapter = chapter.subContents()
        lastviewed = chapter.viewChapter(subchapter)
        
        if chapter.chapterComplete(lastviewed):
            print(f"You last viewed {chapter_names[chapterNumber]}: Section {lastviewed}")
            print("You have completed the chapter, would you like to take a quiz? Y/N")
            quiz = input()
            if quiz.lower == "y":
                takeAQuiz = True
            else:
                quit()
        else:
            quit()

    #take a quiz


main()
