import wikipediaapi
import re

wiki_wiki = wikipediaapi.Wikipedia('en')
search='Bangladesh'
page = wiki_wiki.page(search)


if page.exists()==True:
	print(page.title)
	summary=page.summary[0:2000]
	words=re.split(r'[.,?\s]+', summary)
	wordCounter={}
	for i in words:
		if i not in wordCounter:
			wordCounter[i]=1
		else:
			wordCounter[i]+=1
	print(wordCounter)