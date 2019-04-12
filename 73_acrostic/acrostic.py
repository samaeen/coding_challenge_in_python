#this code does not work at this moment for lack of an api key..But trust me it works..
#there is a working version

import json
#import urllib.request


#url='https://wordsapiv1.p.mashape.com/words/'

randomApi={"b":'berillium',"u":'uranium',"l":'lithium'}
inputWord=input()

for query in inputWord:
	#search=url+query
	#print(search.word)
	print(randomApi[query])



