import feedparser
import urllib

from lxml.html import parse

#return feed object
def get_feed(lang):
	return feedparser.parse('http://www.bbc.co.uk/'+lang+'/index.xml')


#return list of articles
def get_articles(lang):
	feed=get_feed(lang)
	links=[]
	for entry in feed.entries:
		#print entry['title']
		#print entry['link']
		links.append(entry['link'])

	return links

def get_article(url):
	print "-----------------------------------"
	print url
	doc = parse(url).getroot()
	try:
		body=doc.cssselect('div.story-body')[0]
		print body.text_content()
	except:
		print 'no story-body'

			
if __name__ == '__main__':
	links = get_articles('russian')
	links = get_articles('urdu')
	links = get_articles('tamil')
	for link in links:
		#link=links[0]
		get_article(link)