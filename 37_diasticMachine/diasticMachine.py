'''This is diastic machine challenge implementation 
by dan shiffman (coding challenge 37).I just modified the code of 
coding challenge 40(word counter) so that it takes the first 
words[100:105] and finds the words associated with them from 
[105 to 4000]
'''
import wikipediaapi
import re

wiki_wiki = wikipediaapi.Wikipedia('en')
search='Bangladesh'
page = wiki_wiki.page(search)


if page.exists()==True:
	print(page.title)
	summary1=page.summary[100:130]
	summary2=page.summary[201:4000]
	blankarray=[]
	words=re.split(r'[.,?\s]+', summary2)
	for i in summary1:
		if i==' ':
			pass
		else:
			for j in words:
				if i in j:
					print(j)
#need to modify for Django implementation