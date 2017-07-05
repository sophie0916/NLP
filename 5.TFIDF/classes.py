#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sophie
"""

class Query:
    
    def __init__(self, ID):
        self.ID = ID
        self.query = []                     #actual list of queries
        self.TF = dict()                    #number of instances of each query word {word : TF}
        self.IDF = dict()                   #{word : IDF}
        self.TFIDF = dict()                 #{word : TFIDF}
        #self.absList = dict()              #{query word : {abstract ID : abstract TFIDF}}
        
        
        self.queryV = dict()                #contains scores of each query word, index corresponds to query list
                                            #{abstractID : vector[]}
        
                      
                      
                      
                      
        ##############################
        self.cosSim = dict()                #{abstract ID : cosine similarity score}
        #############################
        self.finalList = []                 #Final list containing Score namedTuple objects
                                            #in the format [Score(AbstractID = ID, score = xx)]
    def toString(self):
        print("The ID of this query is: ", self.ID)
        print("query: ", self.query)
        
        
        
class Abstract:
    
    def __init__(self, ID):
        self.ID = ID
        self.abstract = []
        #self.queryVector = dict()
        self.TF = dict()
        self.IDF = dict()
        self.TFIDF = dict()
        
#    
#    def __init__(self, ID, title, author, biblio, abstract):
#        self.ID = ID
#        self.title = title
#        self.author = author
#        self.biblio = biblio
#        self.abstract = abstract
#        #self.queryVector = dict()
#        self.TF = dict()
#        self.IDF = dict()
#        self.TFIDF = dict()        
        
        
        
        
class CosineSimilarityItem:
    def __init__(self, queryID, abstractID, cosSim):
        self.queryID = queryID
        self.abstractID = abstractID
        self.cosSim = cosSim
        
    #sort the cosineSimilarityList by cosSim, then when displaying access these info        
        
    #Remove stop words, punctuation and numbers
    #No don't do it here def processAbstract(self):
        