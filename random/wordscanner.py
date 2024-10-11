word = input("enter a word.")
while True:
    sentence = input("enter a sentence.")
    if sentence.lower() == 'exit':
        break
    count = sentence.lower().split().count(word.lower())
print(f"The word {word} apeears {count} times.")