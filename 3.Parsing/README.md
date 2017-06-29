## Natural Language Processing CSCI-UA 480-009
### Assignment 3: Parsing and Phrase Structure


1. Manual parsing of following sentence :
	
	**_Scientists think that any habitable areas on the planet are in the border region._**

	- Following POS tags are assumed:
		
		- Scientists = NNS
		- think = VBP
		- that = IN
		- any = DT
		- habitable = JJ
		- areas = NNS
		- on = IN
		- the = DT
		- planet = NN
		- are = VPB
		- in = IN
		- the = DT
		- border = NN
		- region = NN


	- Rules of English taken from Jurafsky and Martin section 12.4, figure 12.10 and the example NP rules listed under (12.5) are assumed, in addition to the following:

		- NP --> NP PP
		- VP --> VBP PP
		- NP --> NNS
		- VP --> VBP SBAR
		- SBAR --> IN S


	- Output file: Manual.txt



2. Parsing with CFG parser called ‘Chart Parser’, described in NLTK.chapter 8

	- Program file: parse.py

	- To run parser program, run the following code on a UNIX command line: 

	``` 
	python parse.py

	or

	python parse.py > output.txt
	```



3. CKY chart for the following sentence: **_Any habitable areas are in the border region._**
 
	- Following rules are assumed:

		- S--> NP VP
		- NP --> DT NG
		- NP --> NNS
		- NG --> JJ NG
		- NG --> NN
		- NG --> NNS 
		- NG --> NN NN
		- VP --> VBP PP
		- PP --> IN NP
		- DT --> Any
		- DT --> the
		- JJ --> habitable
		- NNS --> areas
		- NN --> border
		- NN --> region
		- IN --> in
		- VBP --> are


	- Output file: Parse_table.txt