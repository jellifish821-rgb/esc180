#automated readabiliuty index
# number of words
def num_words(text):
    return len(text.split())

def num_sentences(text):
    text = text.replace("!", ".")
    text = text.replace("?", ".")
    ret = len(text.split(".")) #will be +1 actual because last line will split as empty space
    return ret

def num_letters(text):
    num_letters = 0

    for char in text:
        if char.isalpha():
            total_letters += 1

    return num_letters

f = open("file", encoding="latin-1")
text = f.read

tot_letters = num_letters(text)
tot_sent = num_sentences(text)
tot_words = num_words(text)

ARI = 4.71*(tot_letters/tot_words) + 0.5*(tot_words/tot_sent) - 21.43


