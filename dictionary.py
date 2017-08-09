import json

data = json.load(open("data.json"))

def definition(word):
    if word in data:
        return data[word]
    else:
        return "The word entered doesnt exist, try again!"

word = input("Enter the word : ")

print(definition(word))
