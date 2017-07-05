## Natural Language Processing CSCI-UA 480-009
### Assignment 6: Sequence Labeling

- To score the system, run the following code on a UNIX command line: 
		
	```
	javac FeatureSet.java
	javac SeqLabel.java 
	java SeqLabel WSJ_02-21.pos-chunk WSJ_24.pos

	javac -cp maxent-3.0.0.jar:trove.jar *.java
	java -cp .:maxent-3.0.0.jar:trove.jar MEtrain training.chunk model.chunk
	java -cp .:maxent-3.0.0.jar:trove.jar MEtag test.chunk model.chunk response.chunk
	python score.chunk.py WSJ_24.pos-chunk response.chunk
	python cranfield_score.py cranqrel output.txt
	```
    
    
- Understanding the scoring:

	- Accuracy = (correct BIO tags)/Total BIO Tags
	- Precision, Recall and F-measure measure Noun Group performance: A noun group is correct if it in both the system output and the answer key.
	- Precision = Correct/System_Output
	- Recall = Correct/Answer_key
	- F-measure = Harmonic mean of Precision and Recall


-----------------------------------------------------------------------------------------

- Below is a list of features I used to test the corpus with initially:

	- String previousWord

	- String previousPOS

	- String twoWordsBack

	- String followingWord

	- String followingPOS

	- String twoWordsForward


- These are the features I tried adding at the same time, but couldn't due to OutOfMemoryError:

	- boolean isCapital: whether all the letters of the word are upper case

	- boolean capitalized: whether the first letter is capitalized

	- boolean isAlpha: Whether the word contains alphabets only

	- boolean hasSpecial: Whether the word contains any special characters


So among the above, I tested for the feature that yielded the best score, which turned out to be the isAlpha feature, although with a very slight difference.
