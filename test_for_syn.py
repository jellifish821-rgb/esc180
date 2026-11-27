full_text = "I am an apple. I am a star. i like to eat clouds. I can build a bridge! hurray."

L = []
#clean up text where sentences are seperated by . and the punctuation is removed on last sentence
full_text = full_text.lower().replace("?", ".").replace("!", ".")
full_text = full_text[:-1]
print(full_text)

sentences = full_text.split(".")
print(sentences)

for sentence in sentences:
    #remove leading whitespace
    if sentence[0] == " ":
        sentence = sentence.replace(" ", "", 1)

    #remove punctuation
    for character in sentence:
        if character.isalpha() == False and character.isnumeric() == False:
            sentence.replace(character, "")


    L.append(sentence.split(" "))


print(L)