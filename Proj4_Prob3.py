# Joseph Do
# Project 4 Word Frequency
# This program read the content of a text file and show how many times it appears

def main():

    # Open file, lowercase all, split all spaces
    infile = open('random.txt','r')
    file_content = infile.read().lower().split(" ")

    # Empty dictionary
    wordList = {}

    # Go through each word in file and add appearance to them, remove punctuations
    for i in file_content:
        i = i.strip(".").strip(",").strip("?").strip("!")
        count = wordList.get(i,0)
        wordList[i] = count + 1
        
    word_list = wordList.keys()

    # Display results
    for key in word_list:
        print("Word:",key,"#:", wordList[key])

# Start program   
main()
