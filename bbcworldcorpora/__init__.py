import feedparser

#return feed object
def get_feed(lang):
	return feedparser.parse('http://www.bbc.co.uk/'+lang+'/index.xml')


#return list of articles
def get_articles(lang):
	feed=get_feed(lang)
	for entry in feed.entries:
		print entry['title']
		
if __name__ == '__main__':
	get_articles('russian')