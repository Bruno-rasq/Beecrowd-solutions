n_words = int(input())
words = input().split()

correct_words = []
for word in words:
    if len(word) == 3:
        if word[:2] == 'OB':
            correct_words.append("OBI")
        elif word[:2] == 'UR':
            correct_words.append("URI")
        else:
            correct_words.append(word)
    else:
        correct_words.append(word)

print(" ".join(correct_words).strip())