#This program was written by Duc Nguyen on Oct 24, 2019.
#This program generates a BINGO card with 5 rows and 5 columns. In the first
#column, (the “B” column) will be numbers in the range of 1 to 15. Numbers may
#not be repeated. In the second column, (the “I” column) will be numbers in the
#range of 16 to 30. Once again, no duplicates are permitted. In the final
#column, (the “O” column) the numbers will be in the range of 61 to 75. Once the
#BINGO card has successfully been printed, a letter/number combination will be
#drawn (i.e. B7, I23 or N38). The program will then determine if the
#letter/number combination drawn is on the BINGO card.

#Variable Dictionary:
#gamename - the list for the letters in the word BINGO
#bingocard - the list storing all the numbers in the BINGO card
#onerow - the list storing each row of the BINGO card
#randrow - the random row number for the BINGO card
#randcolumn - the random column number for the letter/number combination
#onbingocard - the flag to determine if the letter/number combination in on the card or not

import random
MAXCOLS = 5   #The number of columns in the list for all the numbers from 1 
              #to 75 and in the BINGO card
MAXNUM = 75   #The number of numbers in the list for all the numbers from 1
              #to 75.
MAXROWS = 15  #The number of rows in the list for all the numbers from 1 to 75
                            
GAMENAME = ["B","I","N","G","O"]  #GAMENAME - the list for the letters in the word BINGO


def List():
    """Returns the list for all the numbers from 1 to 75"""
    #minnum - the minimum number in the list of numbers from 1 to 75
    #allnums - the list for all the numbers from 1 to 75
    #eachrow - the list storing each row of the allnums list
    minnum = 1 
    allnums = []     
    for x in range(MAXROWS):
        eachrow = [] 
        for y in range(MAXCOLS):
            eachrow.append(minnum + y*15)
        allnums.append(eachrow)
        minnum = minnum + 1
    return allnums


def BingoCard(allnums):
    """Returns  the list storing all the numbers in the BINGO card
       Simulate generating a BINGO card."""
    #bingocard - the list storing all the numbers in the BINGO card
    #onerow - the list storing each row of the BINGO card
    #randrow - the random row number for the BINGO card
    #allnums - the list for all the numbers from 1 to 75
    bingocard = []  
    for x in range(MAXCOLS):
        onerow = [] 
        for y in range(MAXCOLS):
            randrow = random.randrange(MAXROWS)
            while allnums[randrow][y] == 0:
                randrow = random.randrange(MAXROWS) 
            onerow.append(allnums[randrow][y])
            allnums[randrow][y] = 0
        bingocard.append(onerow)
    return bingocard


def DisplayList(allnums):
    """Display the list after the BINGO card has been created"""
    #allnums - the list for all the numbers from 1 to 75
    print("List   after   filling   the   card")  
    for x in range(MAXROWS):
        for y in range(MAXCOLS):
            print(allnums[x][y],end = "\t")
        print()
    print()
    
def DisplayBingo(bingocard):
    """Display the BINGO card"""
    #bingocard - the list storing all the numbers in the BINGO card
    print("The BINGO card")
    print("B"+"\tI"+"\tN"+"\tG"+"\tO")
    for x in range(MAXCOLS):
        for y in range(MAXCOLS):
            print(bingocard[x][y], end = "\t")
        print()
        
def GenerateRandomSlot():
    """Returns the random row and column numbers"""
    #randrow1 - the random row number for the letter/number combination
    #randcolumn - the random column number for the letter/number combination
    #slot - the list storing the random row and column numbers
    randrow1 = random.randrange(MAXROWS)
    randcolumn = random.randrange(MAXCOLS)
    slot = [randrow1, randcolumn]
    return slot

def DisplayRandomSlot(allnums,slot):
    """Display the random slot number"""
    #slot - the list storing the random row and column numbers
    print(gamename[slot[1]],end = "")
    print(allnums[slot[0]][slot[1]])

def CheckTheSlot(bingocard,allnums,slot):
    "Returns a value of True or False"""
    #onbingocard - the flag to determine if the letter/number combination in on the card or not
    onbingocard = False 
    for x in range(MAXCOLS):
        if allnums[slot[0]][slot[1]] == bingocard[x][slot[1]]:
            onbingocard = True
    return onbingocard

def FinalMessage(onbingocard):
    """Display the final message for the user"""
    #onbingocard - the flag to determine if the letter/number combination in on the card or not
    if onbingocard:
        print("On the card")
    else:
        print("Not on the card")
        
def main():
    """The mainline for the program"""
    #allnums - the list for all the numbers from 1 to 75
    #bingocard - the list storing all the numbers in the BINGO card
    #onbingocard - the flag to determine if the letter/number combination in on the card or not
    #slot - the list storing the random row and column numbers
    
    allnums = List()
    bingocard = BingoCard(allnums)
    DisplayList(allnums)
    DisplayBingo(bingocard)
    slot = GenerateRandomSlot()
    allnums = List()
    DisplayRandomSlot(allnums,slot)
    onbingocard = CheckTheSlot(bingocard,allnums,slot)
    
    FinalMessage(onbingocard)
    
main()

    
        
        
        
        
        
            
