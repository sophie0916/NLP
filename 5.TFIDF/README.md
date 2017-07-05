## Natural Language Processing CSCI-UA 480-009
### Assignment 5: Information Retrieval


##### Ad Hoc Information Retrieval task using TF-IDF weights and cosine similarity scores. 



1. Sorting abstracts for each query, based on cosine similarity scores

	\* Vectors are based on all the words in the query, after removing the members of a list of stop words.

	- Cranfield Collection

       	- cran.qry: contains a set of queries numbered 1~225

			\- query ID: line following .I 
            
            \- query: lines following .W

		- cran.all.1400: contains 1400 abstracts of aerodynamics journal articles

			\- abstract ID: line following .I
            
            \- title: lines following .T
            
            \- author: lines following .A
            
            \- bibliographic notation: lines following .B
            
            \- abstract: lines following .W
            
		- cranqrel: answer key

			\- each line consists of three numbers separated by a space
            
            \- 1st number: query id (1 through 225)
            
            \- 2nd number: abstract id (1 through 1400)
            
            \- 3rd number: represents how related the query is to the given abstract (-1, 1, 2, 3, or 4)

	- list of words to eliminate from query: stop_list.py 


2. Scoring the system

	- Program file: classes.py , getInfo.py
	
	- Output file: output.txt

	- scoring script: cranfield_score.py

	- To score the system, run the following code on a UNIX command line: 

		``` 
		python cranfield_score.py cranqrel output.txt
		```

