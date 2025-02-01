#! python3
# regSearch.py - A program that opens all .txt files in a folder 
#                and searches for any line that matches a user-supplied 
#                regular expression. The results are then printed to the screen.


from pathlib import Path
import glob as gb

#Asking user to input the regex to search for
regex = input("Enter the regex to search for: ")

#Asking the user to input the directory path where .txt files are stored
dirPath =Path(input("Enter the directory path where .txt files are stored: "))

#Get all .txt file in the specified dir
txtfiles = gb.glob(f"{dirPath}/*.txt")

#For each .txt file in the folder
for textfile in txtfiles:
    
    #Open the file for reading
    with open(textfile) as file:
        
        #Read the file line by line
        lineInFile = file.readlines()
    #For each line in the file
        for line in lineInFile:
            #Search for the supplied regex in the line
            if re.search(regex, line):
                #If the regex is found'
                #Print the line that contains the regex
                print(line)
                 #Print the file name
                print(textfile)

