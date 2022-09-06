import codecs
import random

words = set()
ordered_words = []
words_dict = {}
first_words = set()

with codecs.open("speech.txt", mode="r", encoding='utf-8') as f:
    for word in f.read().split():
        words.add(word)
        ordered_words.append(word)
    i = 0
    for sample_word in ordered_words:
        # finding first words (can get better)
        if i > 0 and len(ordered_words[i - 1]) > 0:
            if ordered_words[i - 1].strip()[-1] in (".", "!", "?", ",", ";", ":", "?"):
                if len(sample_word.strip()) > 0 and sample_word.strip()[0].isupper():
                    first_words.add(sample_word.strip())

        if sample_word not in words_dict:
            words_dict[sample_word] = {}
        if i + 1 != len(ordered_words):
            next_word = ordered_words[i + 1]
            if next_word not in words_dict[sample_word]:
                words_dict[sample_word][next_word] = 1
            else:
                words_dict[sample_word][next_word] += 1
        i += 1


def get_next_word(word):
    if word in words_dict.keys() and len(list(words_dict[word].keys())) > 5:
        return random.choice(list(words_dict[word].keys()))
    else:
        return random.choice(list(words))


def get_next_word_random(word):
    return random.choice(list(words))


  def get_sentence():
    first_word = random.choice(list(first_words))
    sentence = first_word.strip() + " "
    next_word = get_next_word(first_word)
    i = 0
    while True:
        # if some words in a sentence are repeated, u can uncomment the code below

        # if next_word in sentence.split(" "):
        #     if sentence.split(" ").count(next_word) > 5:
        #         next_word = get_next_word_random(next_word)
        #         continue

        sentence += next_word.strip() + " "
        if len(sentence.strip()) > 0:
            if sentence.strip()[-1] == "." or sentence.strip()[-1] == "!" or sentence.strip()[-1] == "?":
                break
        i += 1
        if i > 20:
            sentence += "."
            break
        next_word = get_next_word(first_word)

    return sentence.strip()


# generating 50 random sentences in a file
with open("out.txt", "w") as f:
    result = ""
    for i in range(50):
        result += get_sentence() + "\n"
    f.write(result)
