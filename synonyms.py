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

    print(ls_vec1)

    for value in vec2.values():
        ls_vec2.append(value)

    print(ls_vec2)

    abs_vec1 = 0
    abs_vec2 = 0
    for i in range(len(ls_vec1)):
        abs_vec1 += ls_vec1[i]**2
    abs_vec1 = math.sqrt(abs_vec1)

    print(abs_vec1)

    for i in range(len(ls_vec2)):
        abs_vec2 += ls_vec2[i]**2
    abs_vec2 = math.sqrt(abs_vec2)

    print(abs_vec2)

    dot_prod = 0
    for key1 in vec1.keys():
        if key1 in vec2.keys():
            dot_prod += vec1[key1]*vec2[key1]

    cos_sim = dot_prod/(abs_vec1 * abs_vec2)
    return cos_sim


def build_semantic_descriptors(sentences):
    for sentence in sentences:







def build_semantic_descriptors_from_files(filenames):
    pass

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass


if __name__ == "__main__":
    print(cosine_similarity({"a": 1, "b": 2, "c": 3},
{"b": 4, "c": 5, "d": 6}))