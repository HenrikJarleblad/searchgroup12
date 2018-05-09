from elasticsearch import Elasticsearch
import json

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

query = "sjukpenning"

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
           "vart", "dina", "vars", "vårt", "våra", "ert", "era", "vilkas","hej","hallå","tja","tjena","tjenare"]

result = es.search(index="familjeliv", body={"query": {"match": {'question':query}}})


interest = result['hits']['hits']
newquery = query
for i in range(len(interest) if len(interest) < 5 else 5):
    print()
    newquery = newquery + ' '+interest[i]['_source']['question']

newquery = newquery.lower().split(' ')
finalresult = [word for word in newquery if word not in stupidwords]
print(finalresult)