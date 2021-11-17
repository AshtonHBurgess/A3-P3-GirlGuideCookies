import sys
#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     w0465511
#Student Name:  Ashton Burgess


##Lets make this program offer the user to start again
def solidLine():
    print("_____________________________________")

def nextLine():
    print("\n")

def girlGuideProgram():
        # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #need a 2 demiensional list that matches position and prize

    #input listsize
    listSize=int(input("Enter the number of guides selling cookies: "))
    
    guideList=[]
    totalBoxes=0
    #input guides names
    #input boxes sold
    #assign guide names and boxes sold in to my list
    for count in range(0, listSize):
        guide=input("Enter the name of guide #{0}: ".format(count +1 ))
        boxes=int(input("Enter number of boxes sold by {0}: ".format(guide)))
        nextLine()
        totalBoxes= totalBoxes + boxes
        guideList.append([guide])
        guideList[count].append(boxes)
    
    #print(guideList)

    #average boxes sold
    averageBoxes=totalBoxes/listSize

    #Prizes list
    print("The average number of boxes sold by each guide was {0}.".format(averageBoxes))
    nextLine()
    prizes=["         --Trip to Girl Guide Jamboree in Aruba","         --Super Seller Badge","         --Left Over Cookies", "         --Didn't Sell Any"]
    print("Guide                Prizes Won:")
    solidLine()
    nextLine()
    
    #have to get the highest boxexes sold and sort who gets what prize
    boxeList=[]
    for i in range(len(guideList)):    
        boxeList.append(guideList[i][1])

    #print(boxeList)
    maxBoxes=max(boxeList)
    for j in range(len(guideList)):
        if guideList[j][1]==maxBoxes:
            print(guideList[j][0], prizes[0])
        elif guideList[j][1]!=maxBoxes and guideList[j][1] >=10:
            print(guideList[j][0], prizes[1])
        elif guideList[j][1]!=maxBoxes and guideList[j][1] <10 and guideList[j][1] >0:
            print(guideList[j][0], prizes[2])
        elif guideList[j][1]!=maxBoxes and guideList[j][1] ==0:
            print(guideList[j][0], prizes[3])
        else:
            print("something went wrong... are you a girl guide?")
    ##End Of Girl Guides##

def manyGirlGuidePrograms():
    nextLine()
    solidLine()
    print("END OF PROGRAM")
    print("Would you like to run the program agian?")
    solidLine()
    quit=(input("Enter 'no' to quit")).lower()
    while quit != "quit":
        girlGuideProgram()
    exit()

def main():
    #this command will run the method once 
    girlGuideProgram()
    #this command will run the program till the user quits/ or an error occurs...(like if they type a "0" in for number of guides)
    manyGirlGuidePrograms()

main()