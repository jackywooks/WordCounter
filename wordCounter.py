import os
import string

#Load file by user input
inputFile = input("Please input file name: ")
inputFileName = inputFile +".txt"

#check if the input file exist
while os.path.exists(inputFileName) != True:
    print("Invalid File Name\n","Please input the file name of a file in the directories, without .txt\n","i.e. 'a' for 'a.txt'")
    inputFileName = input("Please input file name: ")
    inputFileName = inputFileName +".txt"
else:
    print("Your file is",inputFileName)

#Start Reading the file
inputFileReader = open(inputFileName,'r')
wordString = inputFileReader.read()
inputFileReader.close()

#data massage on the string
abbreString = {
"'ll": " will",
"'d":" would",
"'ve":" have",
"'s":" is",
"'m":" am",
"'re":" are",
"n't":" not",
"--":" "
}

def dataMassage(strInput):
    # Handle abbreviation
    for key in abbreString:
        strInput = strInput.replace(key,abbreString[key])
    #remove punctuation
    strInputv2 = ""
    for char in strInput:
        if char not in string.punctuation:
            strInputv2 += char
    #convert all character to lowercase
    strInput = strInputv2.lower()
    #remove extra space
    strInput = " ".join(strInput.split())
    return strInput

cleanString = dataMassage(wordString)

# convert the clean string to a list
wordList = cleanString.split()

#count the word in the list
wordCount = {}
for word in wordList:
    if word in wordCount:
        wordCount[word] +=1
    else:
        wordCount[word] =1

#sort the dictionary by value
countList = list(wordCount.items())
sortedCountList = sorted(countList,key=lambda x:x[1],reverse=True)
wordCountFinal = dict(sortedCountList)


#write the word count result in the report
reportWriter = open(inputFile+"-WordCountReport.txt",'w')
reportWriter.writelines(["Word\t\t\t\t","Frequency\n"])
for key in wordCountFinal:
    if(len(key) < 4):
        reportWriter.writelines([key,"\t\t\t\t|\t",str(wordCountFinal[key]),"\n"])
    elif(len(key) >= 4 and len(key) < 8):
        reportWriter.writelines([key,"\t\t\t|\t",str(wordCountFinal[key]),"\n"])
    elif(len(key) >= 8 and len(key) < 12):
        reportWriter.writelines([key,"\t\t|\t",str(wordCountFinal[key]),"\n"])
    else:
        reportWriter.writelines([key,"\t|\t",str(wordCountFinal[key]),"\n"])
    
print("Your report is exported, please check",inputFile,"-WordCountReport.txt")

reportWriter.close()