
def matchingWords(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    # print(words1)
    # print(words2)
    score = 0
    for w1 in words1:
        for w2 in words2:
            # print(f"{w1} is matching with {w2}")
            if w1.lower() == w2.lower():
                score += 1
    return score
    


# matchingWords("python is good", "this is good")
sentences = ["this is good","python is good", "python is great", "life long learner"]
query = input("Search Here: ")
score = [matchingWords(sentence, query) for sentence in sentences]
sortedSentScore = [sentScore for sentScore in sorted(zip(score, sentences), reverse =True) if sentScore[0]!=0]
print(f"{len(sortedSentScore)} results found!")
for sc, resultquery in sortedSentScore:
    print(f"{resultquery} : with the score of {sc}")
