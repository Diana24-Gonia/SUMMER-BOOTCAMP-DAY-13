text = ["beautiful", "unhappy", "unwanted", "unaware"]
subwords = []
for word in text:
            if word == "beautiful ":
             subwords.append (word [:6] + '#' * 3)
             subwords.append(word [-3:])
            elif len (word)> 3:
                 subwords.append (word [:2])
                 subwords.append('##' + word [2:]) 
            else:
                subwords.append(word)

print("Subword Tokenization: ", subwords)

