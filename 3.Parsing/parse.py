import nltk

grammar1 = nltk.CFG.fromstring("""
S -> NP VP
NP -> DT NG
NP -> NNS
NG -> JJ NG
NG -> NN
NG -> NNS
NG ->NN NN
VP -> VBP PP
PP -> IN NP
DT -> "Any"
DT -> "the"
JJ -> "habitable"
NNS -> "areas"
NN -> "border"
NN -> "region"
IN -> "in"
VBP -> "are"
""")

sent = "Any habitable areas are in the border region.".strip(".").split()

parser = nltk.ChartParser(grammar1)

for tree in parser.parse(sent):
	print(tree)
