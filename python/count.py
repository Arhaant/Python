sentence = input("Write a sentence: ")
letterCount = 0
wordCount = 1
for i in sentence:
    letterCount = letterCount + 1
    if i == " ":
        letterCount = letterCount - 1
        wordCount = wordCount + 1
print(letterCount)
print(wordCount)