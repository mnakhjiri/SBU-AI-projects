import math
import os
import codecs
import pickle

lang_text = {}
lang_words = {}
unique_words = set()
number_of_words = 0


def lang_process(text, lang):
    text_words = text.split()
    p_lang = math.log(len(lang_words[lang]) / number_of_words)
    for word in text_words:
        p_lang += math.log((lang_words[lang].count(word) + 1) / (len(lang_words[lang]) + len(unique_words)))
    return p_lang


def language_learning(text , lang_title):
    global lang_text, lang_words, unique_words, number_of_words
    words = text.split()
    lang_text[lang_title] += " " + text
    lang_words[lang_title] += words
    number_of_words += len(words)
    for word in words:
        unique_words.add(word)
    with open("database/lang_text.p", "wb") as f:
        pickle.dump(lang_text, f)
    with open("database/lang_words.p", "wb") as f:
        pickle.dump(lang_words, f)
    with open("database/unique_words.p", "wb") as f:
        pickle.dump(unique_words, f)
    with open("database/number_of_words.p", "wb") as f:
        pickle.dump(number_of_words, f)


def get_obj_from_files():
    global lang_text, lang_words, unique_words, number_of_words
    for lang in os.listdir('langs/'):
        file = codecs.open('langs/' + lang, mode='r', encoding='utf-8')
        lang_text[lang[:-4]] = file.read()
        file.close()
    for lang_title, text in lang_text.items():
        words = text.split(" ")
        word_result = []
        for word in words:
            try:
                word = word.split("|")[0]
            except:
                pass
            unique_words.add(word)
            word_result.append(word)
        number_of_words += len(word_result)
        lang_words[lang_title] = word_result
    with open("database/lang_text.p", "wb") as f:
        open("database/lang_text.p", "w").close()
        pickle.dump(lang_text, f)
    with open("database/lang_words.p", "wb") as f:
        open("database/lang_words.p", "w").close()
        pickle.dump(lang_words, f)
    with open("database/unique_words.p", "wb") as f:
        open("database/unique_words.p", "w").close()
        pickle.dump(unique_words, f)
    with open("database/number_of_words.p", "wb") as f:
        open("database/number_of_words.p", "w").close()
        pickle.dump(number_of_words, f)


with codecs.open("input.txt", mode="r", encoding='utf-8') as f:
    if not os.path.exists("database/lang_text.p"):
        get_obj_from_files()
    else:
        lang_text = pickle.load(open("database/lang_text.p", "rb"))
        lang_words = pickle.load(open("database/lang_words.p", "rb"))
        unique_words = pickle.load(open("database/unique_words.p", "rb"))
        number_of_words = pickle.load(open("database/number_of_words.p", "rb"))
    text = f.read()
    words = text.split()
    lang_probility = {}
    for lang_title in lang_text.keys():
        lang_probility[lang_title] = lang_process(text, lang_title)
    max_prob = max(lang_probility.values())
    for lang_title, probility in lang_probility.items():
        if probility == max_prob:
            print("Language is " + lang_title + " ?(y or n) ")
            response = input()
            if response == "y":
                language_learning(text, lang_title)
                break
            else:
                print("Enter language title: ")
                lang_title_input = input()
                language_learning(text , lang_title_input)
                break
