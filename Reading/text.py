import nltk
import sys
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentence = """I went to see star wars yesterday. It was bad, bad bad very bad. I almost cried tears of joy"""
'''
tokens = nltk.word_tokenize(sentence)
tokens
tagged = nltk.pos_tag(tokens)
tagged[0:6]
'''


def findpolar(test_data):
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(test_data)["compound"];
    '''if(polarity >= 0.1):    
     foundpolar = 1
    if(polarity <= -0.1):
     foundpolar = -1 
    if(polarity>= -0.1 and polarity<= 0.1):
     foundpolar = 0
     '''
    return(polarity)
def getValues(file):
    text_file = open(file, "r")
    lines = text_file.readlines()
    text_file.close()
    #print(lines[1])
    #print(findpolar(sentence))
    tweets = []
    followers = []
    for x in range(len(lines)):
        #print(lines[x])
        #print(len(lines))
        start = lines[x].index("\"text\"")
        start = start + 7
        end = lines[x].index("source")
        end  = end - 3
        foldStart = lines[x].index("followers_count")+17
        foldEnd = lines[x][foldStart:].index(",")
        #foldStart = lines[x][folStart:].index(":")
        #print(foldStart)
        #print(foldEnd)
        num = lines[x][foldStart:foldStart+foldEnd]
        followers.append(num)
        string = lines[x][start:end]
        tweets.append(list((string,num)))

    #print("Length of tweets  before removing dups: " + str(len(tweets)))
    #tweets = list(set(tweets))
    #print("Length of tweets after removing dups:" + str(len(tweets)))
    #print(followers)
    polars = []
    for y in range(len(tweets)):
        polars.append((int(followers[y]),findpolar(tweets[y][0])))
    numPos = 0
    numNeg = 0
    numNeut = 0
    #target = sys.argv[2]
    for z in range(len(polars)):
        if polars[z][1] == 0:
            numNeut = numNeut + 1
        elif polars[z][1] > 0 :
            numPos = numPos + 1
        else:
            numNeg = numNeg + 1
    #print("FinalPolarity of our tweets, averages is " + str(sum(polars)/len(polars)))
    #print(polars)
    subj = (numPos+numNeg)/numNeut
    pol = numPos/numNeg
    #print("Subjectivity is " + str(subj))
    #print("Polarity is: " + str(pol))
    #print(numPos)
    #print(numNeg)
    #print(numNeut)
    #data = (polars,target)
    #In [10]: df = pd.DataFrame(data, index=index, columns=columns)
    #df = pd.DataFrame({'col':polars})
    #df['target'] = target
    #print(df)
    return([subj,pol])

subjList = []
polList = []

file = open(sys.argv[1], "r")
lines = file.readlines()
file.close()
for x in lines:
    results = getValues(x.split("\n")[0])
    subjList.append(results[0])
    polList.append(results[1])
print(subjList)
print(polList)