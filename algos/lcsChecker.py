import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def convert(lst): 
    return ' '.join(lst).split()

def cleanSentence(sentence):
    okPOS = ['NN', 'DT', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS', 'SYM', 'TO', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WRB']
    sentenceTk = nltk.word_tokenize(sentence)
    sentencePOS = nltk.pos_tag(sentenceTk)
    print(sentencePOS)
    # keeping nouns, adjectives, verbs and cleaning the rest
    cleaned = []
    for i in range(len(sentenceTk)):
        if sentencePOS[i][1] in okPOS:
            cleaned.append(sentencePOS[i][0])
    return cleaned


def lcsChecker(modelans, kidans):
    modelAns = cleanSentence(modelans)
    kidAns = cleanSentence(kidans)
    print(modelAns)
    print(kidAns)
    n, m = len(modelAns), len(kidAns)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if modelAns[i-1] == kidAns[j-1]:
                dp[i][j] = 1 + dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
    commonSubsequencesCnt = dp[n][m]
    return commonSubsequencesCnt / (2**min(n, m) - 1)

print(lcsChecker("my name is groot", "groot is my name"))


