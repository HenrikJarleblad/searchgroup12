from elasticsearch import Elasticsearch
import json
import string

def strip_punctuation(s):
    sub1 = ''.join(c for c in s if c not in string.punctuation )
    return ''.join(c for c in sub1 if not c.isdigit())

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

query = input()

def getAnswers(query):
    stupidwords = ["och", "det", "att", "i", "en",
            "jag", "hon", "som", "han", "på", "den", "med", "var", "sig",
            "för", "så", "till", "är", "men", "ett", "om", "hade", "de", "av",
            "icke", "mig", "du", "henne", "då", "sin", "nu", "har", "inte",
            "hans", "honom", "skulle", "hennes", "där", "min", "man", "ej",
            "vid", "kunde", "något", "från", "ut", "när", "efter", "upp", "vi",
            "dem", "vara", "vad", "över", "än", "dig", "kan", "sina", "här",
            "ha", "mot", "alla", "under", "någon", "eller", "allt", "mycket",
            "sedan", "ju", "denna", "själv", "detta", "åt", "utan", "varit",
            "hur", "ingen", "mitt", "ni", "bli", "blev", "oss", "din", "dessa",
            "några", "deras", "blir", "mina", "samma", "vilken", "er", "sådan",
            "vår", "blivit", "dess", "inom", "mellan", "sådant", "varför",
            "varje", "vilka", "ditt", "vem", "vilket", "sitta", "sådana",
            "vart", "dina", "vars", "vårt", "våra", "ert", "era", "vilkas",
            "hej","hallå","tja","tjena","tjenare","dvs","osv","etc","","inkl","få","komma",
            "kommer"]

    query = strip_punctuation(query)
    query = query.lower().split(" ")
    query = [word for word in query if word not in stupidwords]
    query = ' '.join(query)
    print(query)
    result = es.search(index="familjeliv", body={"query": {"match": {'question':query}}})


    interest = result['hits']['hits']
    newquery = query
    for i in range(len(interest) if len(interest) < 5 else 5):
        score = interest[i]['_score']
        if(score > 1):
            newquery = newquery + ' '+interest[i]['_source']['question']


    newquery = strip_punctuation(newquery)
    newquery = newquery.lower().split(' ')
    finalresult = [word for word in newquery if word not in stupidwords]
    finalresult = ' '.join(finalresult)

    result1 = es.search(index="familjeliv", body={"query": {"match": {'question': finalresult}}})

    interest = result1['hits']['hits']
    newquery = query
    final_answers = interest[0]['_source']['answers']

    finalresultarray = finalresult.split(" ")

    minHaspmap = {}
    for word in finalresultarray:
        if word in minHaspmap:
            minHaspmap[word] = minHaspmap[word] +1
        else:
            minHaspmap[word] = 1
    
    for word in query.lower().split(' '):
        if word not in stupidwords:
            minHaspmap[word] = minHaspmap[word] + 1000
    score = -1
    ans = ""
    for answer in final_answers:
        answerlist = answer.lower().split(' ')
        tempscore = 0
        relevantwords = 0
        for word in answerlist:
            if word in minHaspmap:
                tempscore = tempscore + minHaspmap[word]
                relevantwords = relevantwords + 1
            if "?" in word:
                tempscore = -999999
        tempscore = tempscore/len(answerlist)
        if score < tempscore:
            ans = answer
            score = tempscore
    finalans = {"answer":ans,"confidence":1 if score>=1 else 0}
    return finalans
out = getAnswers(query)
print(out)