import nltk
import tensorflow as tf
import tensorflow_hub as hub


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def tfLCSChecker(modelans, kidans):
    embed = hub.load("https://tfhub.dev/google/tf2-preview/nnlm-en-dim128/1")
    embeddings = embed([modelans, kidans])
    return tf.keras.losses.cosine_similarity(embeddings[0], embeddings[1], axis=-1)


def cleanSentence(sentence):
    okPOS = ['NN', 'DT', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS', 'SYM', 'TO', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WRB']
    sentenceTk = nltk.word_tokenize(sentence)
    sentencePOS = nltk.pos_tag(sentenceTk)
    # keeping nouns, adjectives, verbs and cleaning the rest
    cleaned = []
    for i in range(len(sentenceTk)):
        if sentencePOS[i][1] in okPOS:
            cleaned.append(sentencePOS[i][0])
    return cleaned


def lcsChecker(modelans, kidans):
    modelAns = cleanSentence(modelans)
    kidAns = cleanSentence(kidans)
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


def keywordsChecker(modelans, kidans):
    modelAns = cleanSentence(modelans)
    kidAns = cleanSentence(kidans)
    n, m = len(modelAns), len(kidAns)
    modelAns = set(modelAns)
    intersection = modelAns.intersection(kidAns)
    return len(list(intersection))/len(modelAns)


def lengthChecker(modelans, kidans):
    return float(min(1, len(kidans)/len(modelans)))
    
print(lcsChecker("my name is groot", "groot is my name"))
print(keywordsChecker("my name is groot", "groot is my name"))
print(lengthChecker("my name is groot", "groot is my name"))
print(tfLCSChecker("continuing forever", "continuing forever in the same way"))


