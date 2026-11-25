##1 word frequency
#word_ls = open("wizard_of_oz.txt").read.split()
word_ls = "I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased. However, I know nothing at all about my disease, and do not know for certain what ails me.".split()



word_counts = {}
for word in word_ls:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1



#B
def top10(L):
    for k in range(len(L)-1, 0, -1):
            cur_max = L[k]
            loc_max = k
            # iteratre through unsorted portion
            for i in range(k):
                if L[i] > cur_max:
                    cur_max = L[i]
                    loc_max = i
            #perform swap
            L[k], L[loc_max] = L[loc_max], L[k]
    print(L)
    return L[-10:]
    # O(n^2)


# C
inv_word_counts = {}
for value in word_counts.values():
    inv_word_counts[value] = []
print(inv_word_counts)
for key, value in word_counts.items():
    inv_word_counts[value].append(key)

print(inv_word_counts.items())

##2
'''
h = open("hello.html","w", encoding="latin-1")
h.write("hello")
h.close()
'''

with open("Hello, World.html", "a") as h:
    h.write("<b>Vinci</b>\n")
    h.write('<a href = "https://en.wikipedia.org/?title=Engineering_science&redirect=no">engineering science</a>')

##3

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def num_results(term):
    term = term.replace(" ", "%")
    link = f"https://en.wikipedia.org/w/index.php?title=Special:Search&fulltext=1&search={term}"
    req = urllib.request.Request(link, headers={"User-Agent":
    "ESC180-Lab7/1.0 (University of Toronto course lab)"})
    f = urllib.request.urlopen(req)
    page = f.read().decode("utf-8")
    f.close()

    if "data-mw-num-results-total=" in page:
        ind = page.find('data-mw-num-results-total="')
        start_ind = ind + 27
        i = start_ind
        num = []
        while page[i] != '"':
            num.append(page[i])
            i += 1
        num = "".join(num)
        return num


print(num_results("engineering science"))


def choose_variants(L):
    result = {}
    for variant in L:
        variant = variant.replace(" ", "%")
        result[variant] = int(num_results(variant))


    inv_res = {}
    for value in result.values():
        inv_res[value] = ""
    for key, value in result.items():
        inv_res[value] = key

    sorted(inv_res)

    ls = []
    for value in inv_res.values():
        ls.append(value)

    return ls[-1].replace("%", " ")

L = (['"five-year anniversary"', '"fifth anniversary"'])
print(choose_variants(L))







































