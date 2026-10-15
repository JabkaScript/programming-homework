import re

sentence = input("Введите предложение: ")

words = re.findall(r"[а-яёa-z]+", sentence.lower())
result = []

for word in words:
    if word not in result:
        result.append(word)
print(result)
