#class to create a chapter
from chaptercontents import *

class Chapter():
    def __init__(self, chapter_number:int):
        self.chapter_number = chapter_number

    def subContents(self) -> int:
        print("Where would you like to begin?")
        chapterList = chapter_contents[self.chapter_number]
        #print(f"{chapterList}")
        for chapter in chapterList:
            print(f"{chapter}: {chapterList[chapter]}")
        chapterNumber = int(input())
        print(f"you have selected {chapterList[chapterNumber]}")
        return chapterNumber
    
    def viewChapter(self, subchapter: int) -> int:
        
        self.printChapter(subchapter)             
        while self.continueStudying(subchapter):
            subchapter += 1
            self.printChapter(subchapter)
        
        print("Returning to home screen")
        return subchapter

    def continueStudying(self, subchapter: int):
        #get chapter length
        chapterLen = len(chapter_contents[self.chapter_number])
        if subchapter < chapterLen:
            printstring = (f"You have finished {chapter_names[self.chapter_number]}:" \
                            f"{chapter_contents[self.chapter_number][subchapter]}\n" \
                            "Would you like to continue learning Y/N?")
            print(printstring)
            usercont = input()
            if usercont.lower() == "y":
                return True
            else:
                return False
        return False


    def chapterComplete(self, subchapter: int) -> bool:
        chapterLen = len(chapter_contents[self.chapter_number])
        if subchapter == chapterLen:
            return True
        return False
    
    def printChapter(self, subchapter: int):
        #print file between fstring "Chapter {self.chapter_number}: Subsection {subchapter}"
        #and fstring "Chapter {self.chapter_number}: Subsection {subchapter++}" or "End Chapter"
        start_string = f"Chapter {self.chapter_number}: Subsection {subchapter}"
        end_string1 = f"Chapter {self.chapter_number}: Subsection {subchapter+1}"
        end_string2 = "End Chapter"
        
        with open("ISTQBcontent.txt", 'r')  as file:
            printing = False
            counter = 0
            for _, current_line in enumerate(file):
                if start_string in current_line:
                    printing = True
                    continue
                if end_string1 in current_line:
                    printing = False
                    input("End of section: Press any key to continue")
                    break
                if end_string2 in current_line:
                    printing = False
                    input("End of Chapter: Press any key to continue")
                    break
                if printing:
                    print(current_line)
                    counter += 1
                    if counter == 3:
                        input("Readability break: Press any key to continue")
                







