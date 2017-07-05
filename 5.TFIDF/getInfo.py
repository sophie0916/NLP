#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sophie YeonSoo Kim
"""

#import nltk
import re
from classes import Query
from classes import Abstract
from classes import CosineSimilarityItem
import math
import numpy as np
#from decimal import *
#import collections
from stop_list import closed_class_stop_words

#from collections import defaultdict

stopList = closed_class_stop_words

def parseQuery(filename):
    #initialize list of Query objects
    queryList = []
    
    #Correctly store each query into the dictionary
    #{key:value} = {Query ID : Query text}
    ID = 0;
    identifier = ""

    with open(filename, "r") as text:
        index = -1
        for line in text:
            if line[:2] == ".I" :
                identifier = ".I"
                ID = int(line.strip(identifier).strip())
                curr = Query(ID)
                queryList.append(curr)
                index += 1        
            elif line[:2] == ".W":
                identifier = line[:2]
            elif identifier == ".W":
                queryList[index].query += re.split("[., /\-!?:\n()]+", line)
                
            else:
                continue              


    #Remove numbers and stop words from the queries
    for item in queryList:
        item.query = list(filter(None, item.query))
        toRemove = []
        for eachWord in item.query:
            if eachWord.isnumeric():
                toRemove.append(eachWord)
            else: 
                if eachWord in stopList:
                    toRemove.append(eachWord)
        toRemove = list(set(toRemove))
        for removeWord in toRemove: 
            while removeWord in item.query:
                item.query.remove(removeWord)
            
    return queryList


        
def parseAbstract(filename):
    
    #initialize list of Abstract objects
    abstractList = []
    
    ID = 0;
    identifier = ""

    with open(filename, "r") as text:
        index = -1
        for line in text:
            if line[:2] == ".I" :
                identifier = ".I"
                ID = int(line.strip(identifier).strip())
                curr = Abstract(ID)
                abstractList.append(curr)
                index += 1        
            elif line[:2] == ".W":
                identifier = line[:2]
            elif identifier == ".W":
                abstractList[index].abstract += re.split("[., /\-!?:\n()]+", line)
                
            else:
                continue                         
            
    #Remove numbers and stop words from the abstracts
    for item in abstractList:
        item.abstract = list(filter(None, item.abstract))
        toRemove = []        
        for eachWord in item.abstract:
            if eachWord.isnumeric():
                toRemove.append(eachWord)
            else:
                if eachWord in stopList:
                    toRemove.append(eachWord)                    
        toRemove = list(set(toRemove))
        for removeWord in toRemove:
            while (removeWord in item.abstract):
                item.abstract.remove(removeWord)
                    
    return abstractList



def queryTFIDF(queryList):
    #Contains number of queries containing that word; {word : # of queries}
    compList = dict()

    #Count occurrence of each word in query(TF)
    for item in queryList:
        qList = dict()
        for eachWord in item.query:
            if eachWord not in item.TF:
                qList[eachWord] = 1
            else:
                qList[eachWord] += 1
            if eachWord not in compList:
                compList[eachWord] = 1
            else:
                compList[eachWord] += 1   
        item.TF = qList


    #Compute IDF scores for each query vector
    for item in queryList:
        for word in item.query:
            item.IDF[word] = float(len(queryList)) / float(compList[word])
            item.TFIDF[word] = float(float(item.TF[word]) * float(math.log(item.IDF[word])))

    return queryList



def abstractTFIDF(abstractList):

    #Contains number of abstracts containing that word; {word : # of abstracts}
    compList = dict()
    
    #Count occurrence of each word in abstract(TF)
    for item in abstractList:
        aList = dict()
        for eachWord in item.abstract:
            if eachWord not in item.TF:
                aList[eachWord] = 1
            else:
                aList[eachWord] += 1
            if eachWord not in compList:
                compList[eachWord] = 1
            else:
                compList[eachWord] += 1
        item.TF = aList
                    

    #Compute IDF scores for each abstract vector
    for item in abstractList:
        for word in item.abstract:
            item.IDF[word] = float(len(abstractList)) / float(compList[word])
            if (float(len(abstractList) < 0)):
                print("WARNING: ABSTRACTLIST LENGTH NEGATIVE!")
            elif (float(compList[word] < 0)):
                print("WARNING NEG COMPLISTWORDCOUNT")
            elif(item.IDF[word] <0):
                print("NEG AFTER COMPUTATIN")
            item.IDF[word] = np.log(item.IDF[word])
            if(item.IDF[word] <0):
                print("NEG AFTER LOG")
            item.TFIDF[word] = float(float(item.TF[word]) * item.IDF[word])
                   



    return abstractList


def cosineSimilarity(vec1, vec2):
    numerator = 0.0
    ss1, ss2 = 0.0, 0.0
    result = 0.0
    for i in range(0, len(vec1)):
#        print(i)
        numerator = numerator + vec1[i] * vec2[i]
        ss1 = ss1 + float(math.pow(vec1[i],2))
        ss2 = ss2 + float(math.pow(vec2[i],2))
        
    try:    
        result = float(numerator / math.sqrt(ss1 * ss2))
    except:
        result = 0
    return result



def score(queryList, abstractList):
    #scoreList is a dictionary of cosine similarity scores {queryID: [CosineSimilarityItem]}
    scoreList = dict()
    for qItem in queryList:
        key = qItem.ID
        unsortedScores = []
        for aItem in abstractList:
            qryTFIDF = []
            absTFIDF = []
            for qWord in qItem.query:
                qryTFIDF.append(qItem.TFIDF[qWord])
                if (qWord in aItem.abstract):
                    absTFIDF.append(aItem.TFIDF[qWord])
                else:
                    absTFIDF.append(0)
            cosSimScore = cosineSimilarity(qryTFIDF, absTFIDF)
            unsortedScores.append(CosineSimilarityItem(qItem.ID, aItem.ID, cosSimScore))
        unsortedScores.sort(key=lambda x:x.cosSim, reverse=True)
        scoreList[key] = unsortedScores
    
    return scoreList
    
    

def output(scoreList):
    result = open("output.txt", "w")
    temp = ""
    for key in scoreList:
        for scoreItem in scoreList[key]:
            temp += str(scoreItem.queryID) + " " + str(scoreItem.abstractID) + " " + str(scoreItem.cosSim)
            temp += "\n"        
    result.write(temp)
    result.close()



def writeParsedQuery(listName):
    result = open("parsedQuery.txt", "w")
    temp = ""
    for qItem in listName:
        temp += str(qItem.ID) + "\n"
        for eachQuery in qItem.query:
            temp+= eachQuery + ", "
        temp+= "\n"            
        temp+= "\n"
    result.write(temp)
    result.close()



def writeParsedQuery2(listName):
    result = open("parsedQueryWithTFIDF.txt", "w")
    temp = ""
    for qItem in listName:
        temp += str(qItem.ID) + "\n"
        for key in qItem.TFIDF:
            temp+= "key: " + key + " TFIDF: " + str(qItem.TFIDF[key]) + "\n"
        temp+= "\n"            
    result.write(temp)
    result.close()
    
def writeParsedAbstract(listName):
    result = open("parsedAbstract.txt", "w")
    temp = ""
    for qItem in listName:
        temp += "CURRENTQUERYID: " + str(qItem.ID) + "\n"
        for eachQuery in qItem.abstract:
            temp+= eachQuery + ", "
        temp+= "\n"            
        temp+= "\n"
    result.write(temp)
    result.close()    
    
def writeParsedAbstract2(listName):
    result = open("parsedAbstractWithTFIDF.txt", "w")
    temp = ""
    for qItem in listName:
        temp += str(qItem.ID) + "\n"
        for key in qItem.TFIDF:
            temp+= "key: " + key + " TFIDF: " + str(qItem.TFIDF[key]) + "\n"
        temp+= "\n"
    result.write(temp)
    result.close()    


if __name__ == "__main__":
    queryList = parseQuery("Cranfield_collection_HW/cran.qry")
    print("QUERY PARSED")
#    writeParsedQuery(queryList)
    
    queryList = queryTFIDF(queryList)
    writeParsedQuery2(queryList)
    print("QUERYLIST UPDATED WITH TFIDF")
    

    abstractList = parseAbstract("Cranfield_collection_HW/cran.all.1400")
#    writeParsedAbstract(abstractList)
    print("ABSTRACTLIST PARSED")
    
#    print("Number of abstracts: " + str(len(abstractList)))
    
    abstractList = abstractTFIDF(abstractList)
    writeParsedAbstract2(abstractList)
    print("ABSTRACTLIST UPDATED WITH TFIDF")
    
    scoreList = score(queryList, abstractList)
#    scoreList.sort(key=lambda x:x.cosSim, reverse=True)
    output(scoreList)
#    print(scoreList)
    
#ut.sort(key=lambda x: x.count, reverse=True)
    print("success!")
    
#    queryList = queryAbstractVector(queryList, abstractList)
#    print("VECTOR")
#    output(queryList)
#    
#    print("success!")
#


