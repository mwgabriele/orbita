import feedparser

feed_url = "https://www.revistaastrokids.com/rss/category/astronautica"

blog_feed = feedparser.parse(feed_url)

print(len(blog_feed.entries))
for noticia in blog_feed.entries:
    print(noticia.title)
