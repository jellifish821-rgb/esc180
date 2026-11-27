'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2):
    ls_vec1 = []
    ls_vec2 = []
    for value in vec1.values():
        ls_vec1.append(value)

    for value in vec2.values():
        ls_vec2.append(value)

    abs_vec1 = 0
    abs_vec2 = 0
    for i in range(len(ls_vec1)):
        abs_vec1 += ls_vec1[i]**2
    abs_vec1 = math.sqrt(abs_vec1)

    for i in range(len(ls_vec2)):
        abs_vec2 += ls_vec2[i]**2
    abs_vec2 = math.sqrt(abs_vec2)

    dot_prod = 0
    for key1 in vec1.keys():
        if key1 in vec2.keys():
            dot_prod += vec1[key1]*vec2[key1]

    cos_sim = dot_prod/(abs_vec1 * abs_vec2)
    return cos_sim


def build_semantic_descriptors(sentences):
    d = {}
    for sentence in sentences:
        for word in sentence:
            if word not in d.keys():
                d[word] = {} # create new key, word; and assign it an empty dictionary

            #update semantic sim for word; by updating it with the other words(w) in the sentence
            for w in sentence:
                if w != word:
                    if w in d[word].keys():
                        d[word][w] += 1
                    else:
                        d[word][w] = 1

    return d



def build_semantic_descriptors_from_files(filenames):
    #create 1 file for all text
    text = "" #I was having trouble opening files before, so I added this code
    for file in filenames:
        with open(file, 'r', encoding='latin1') as file:
            text += file.read()
    '''
    with open('complied_file', 'w', encoding ='latin1') as complied_file:
        for file in filenames:
            with open(file, 'r', encoding='latin1') as file:
                text = file.read()
            complied_file.write(text)
        full_text = complied_file.read()
    '''


    return build_semantic_descriptors(convert_txt_to_ls(text))

#helper function
def convert_txt_to_ls(full_text):
    L = [] #append to this list

    #clean up text where sentences are seperated by .
    new_text = full_text.lower().replace("?", ".").replace("!", ".")

    #punctuation is removed on last sentence
    new_text = new_text[:-1]

    sentences = new_text.split(".")

    for sentence in sentences:

        #remove leading whitespace ##The functions sometimes gives lists of len0, so the indexing causes errors ### as in sentence could be len 0? then adding a conditional should catch it right? like below?
        if len(sentence) != 0:
            if sentence[0] == " ":
                sentence = sentence.replace(" ", "", 1)

        #remove punctuation
        for character in sentence:
            if character != " " and character.isalpha() == False and character.isnumeric() == False and character != "'":
                sentence = sentence.replace(character, "") # should remove punctuation now, it didn;t work as replace() doesn't modify the string in place and I forgot reassign the altered senetence to a variable

        word_list = sentence.split(" ")
        L.append(word_list)

    return L


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pick = None
    max_close = -1
    if word in semantic_descriptors.keys(): # added conditional
        word_vec = semantic_descriptors[word]

    for option in choices: #add similar conditional here?
        option_vec = semantic_descriptors[option]
        closeness = similarity_fn(word_vec, option_vec)
        if closeness > max_close:
            max_close = closeness
            pick = option

    return pick

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    #File name gives words, were the first is what we compare to and the second in correct
    game = seperate_by_line(filename)
    points = 0
    guesses = 0
    for round in range(len(game)):
        given = game[round][0]
        correct = game[round][1]
        possibles = game[round][2:] # changed [1:] to [2:] because slicing index is inclusve on the start
        if most_similar_word(given, possibles, semantic_descriptors, similarity_fn) == correct:
            points += 1
        guesses += 1

    return (points/guesses)*100

def seperate_by_line(filename):
    text = "" #I was having trouble opening files before, so I added this code
    with open(filename, 'r', encoding='latin1') as file:
        text += file.read()
    L = [] #append to this list

    sentences = text.split("\n")

    for sentence in sentences:
        word = sentence.split(" ")
        L.append(word)
    return L


if __name__ == "__main__":
    text2 = "I am an apple. I am a star; i like to eat clouds-I can, build a bridge! hurray."
    most_similar_word("cloud",[hurray, am, I, star], build_semantic_descriptors(convert_txt_to_ls(text2)), cosine_similarity)

    '''

    (cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
    sentences1 = [["i", "am", "a", "sick", "man"],
["i", "am", "a", "spiteful", "man"],
["i", "am", "an", "unattractive", "man"],
["i", "believe", "my", "liver", "is", "diseased"],
["however", "i", "know", "nothing", "at", "all", "about", "my",
"disease", "and", "do", "not", "know", "for", "certain",
"what", "ails", "me"]]
    print(build_semantic_descriptors(sentences1))



    print(convert_txt_to_ls(text2))
    print(build_semantic_descriptors(convert_txt_to_ls(text2)))
    alice = build_semantic_descriptors_from_files(["Alice.txt"])
    print(alice["cheshirecat"])

    word = "mad"

    choices = ["rabbit", "queen", "hatter", "hare", "march"]
    print(most_similar_word(word, choices, alice, cosine_similarity))
    print(run_similarity_test("test_sim.txt", alice, cosine_similarity))
    '''


