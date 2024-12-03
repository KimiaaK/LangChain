"""Given a dictionary consisting of many roots and a sentence, stem all the words in the sentence with the root forming it."""

roots = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"


def replace_root(roots, sentence):
    words = sentence.split(" ")
    for index, word in enumerate(words):
        for root in roots:
            if word.startswith(root):
                words[index] = root
    return " ".join(words)


a = replace_root(roots, sentence)
print(a)
