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
    found_match = False      #Flag to check if the regex is found in the file
    matchedLines = []        #List to store the lines that contain the regex
    
    #Open the file for reading
    with open(textfile) as file:
        
        #Read the file line by line
        lineInFile = file.readlines()
    #For each line in the file
        for line in lineInFile:
            #Search for the supplied regex in the line
            if re.search(regex, line):
                #If the regex is found'
                #Append the line that contains the regex into the list
                matchedLines.append(line.strip())
                
                found_match = True    #Set the flag to True
                
        if found_match:
            #Print the name of the file that contains the regex
            print(f"The file that contains below matches- {textfile}")
            #Print the line that contains the regex
            for i,L in enumerate(matchedLines):
                n = i+1
                print(f"{n}. {L}")
            print("\n")
                

