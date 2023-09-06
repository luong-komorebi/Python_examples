def vowel_remover(text):
    return "".join(l for l in text if l.lower() not in "aeiou")
print(vowel_remover("hello world!"))
