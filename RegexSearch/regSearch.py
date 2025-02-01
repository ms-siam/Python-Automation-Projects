#! python3
# regSearch.py - A program that opens all .txt files in a folder 
#                and searches for any line that matches a user-supplied 
#                regular expression. The results are then printed to the screen.


from pathlib import Path
import re

#Asking user to input the regex to search for
regex = input("Enter the regex to search for: ")

#Asking the user to input the directory path where .txt files are stored
dirPath =Path(input("Enter the directory path where .txt files are stored: "))

#Get all .txt file in the specified dir
txtfiles = dirPath.glob("*.txt")

#For each .txt file in the folder
for textfile in txtfiles:
    found_match = False
    matchedLines = []
    #Open the file for reading
    with open(textfile) as file:
        
        #Read the file line by line
        lineInFile = file.readlines()
    #For each line in the file
        for line in lineInFile:
            #Search for the supplied regex in the line
            if re.search(regex, line):
                #If the regex is found'
                #Assign the line that contains the regex
                matchedLines.append(line)
                found_match = True
        if found_match:
            #Print the name of the file that contains the regex
            print(textfile)
            #Print the line that contains the regex
            for L in matchedLines:
                print(L)
            print("\n")
                

