import scrapy

class MyCrawler(scrapy.Spider):
    name = 'my_crawler'
    
    def __init__(self, seed_url, max_pages, max_depth, *args, **kwargs):
        super(MyCrawler, self).__init__(*args, **kwargs)
        self.start_urls = [seed_url]
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.visited_urls = set()
        
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'depth': 0})

    def parse(self, response):
        # Save the HTML content to a file
        filename = f'page_{response.meta["depth"]}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        
        # Extract relevant content from the HTML document
        # You can further process or save the content as needed
        
        # Follow links to next pages if not reached max pages or max depth
        if response.meta.get('depth', 0) < self.max_depth and len(self.visited_urls) < self.max_pages:
            for link in response.css('a::attr(href)').getall():
                absolute_url = response.urljoin(link)
                if absolute_url not in self.visited_urls:
                    self.visited_urls.add(absolute_url)
                    yield scrapy.Request(url=absolute_url, callback=self.parse, meta={'depth': response.meta.get('depth', 0) + 1})
