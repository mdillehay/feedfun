import feedparser

f = feedparser.parse('https://talkpython.fm/episodes/rss')

#print(f.entries[0]['link'])

for i in range(0,9):
    print(f.entries[i]['title'] + ": " + f.entries[i]['link'])
    
    
