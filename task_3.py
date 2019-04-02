def generate_n_grams(size, words_list):
    word_list_by_size = []

    for word in words_list:
        if size:
            word_list_by_size.append(word)
            size = size -1
        else:
            yield word_list_by_size
            word_list_by_size.pop(0)
            word_list_by_size.append(word)

    if len(word_list_by_size):
        yield word_list_by_size

# sentence = "the quick red fox jumps over the lazy brown dog"
# for x in generate_n_grams(3, sentence.split()): print(x)

def generate_sentence(subjects, verbs, objects):
    for i in range(len(subjects)):
        yield ' '.join([subjects[i],verbs[i], objects[i]])

# subjects=["I", "You"]
# verbs=["play", "love"]
# objects=["Basketball","Football"]
# for setence in generate_sentence(subjects, verbs, objects): print(setence)
def generate_permutations(s):
   if len(s) == 1:
     yield s
   else:
       for a in s:
         remaining_elements = [x for x in s if x != a]
         yield from generate_permutations(remaining_elements) # permutations of sublist

some_list = [1,'a',True]
for perm in generate_permutations(some_list): print(perm)
