text = input("Enter Sentence: ")
sentence_delimiters = '.!?'
sentences = []
current_sentence = []

for char in text:
    current_sentence.append(char)
    if char in sentence_delimiters:
        sentences.append(''.join(current_sentence).strip())
        current_sentence = []

if current_sentence:
    sentences.append(''.join(current_sentence).strip())

print("Tokenized Sentences:")
print(sentences)