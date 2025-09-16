import feedparser

feed_url = "https://sci.esa.int/newssyndication/rss/sciweb.xml"

blog_feed = feedparser.parse(feed_url)

print(len(blog_feed.entries))
for noticia in blog_feed.entries:
    print(noticia.title)
