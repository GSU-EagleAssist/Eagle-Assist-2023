import scrapy


class ResearchSpider(scrapy.Spider):
    name = 'research'
    
    def start_requests(self):
     allowed_domains = ['https://research.georgiasouthern.edu']
     start_urls = [
        'https://research.georgiasouthern.edu/impact-areas/'
        
        ]

     for url in start_urls:
        yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        for research in response.css('#main'):
            areas = response.css('div.wp-block-cover__inner-container')
            yield {
                'Title': research.css('h1.title::text').get(),
                'About' : research.css('p:nth-child(3)::text').get() + '\n\n' + response.css('#main > p:nth-child(4)::text').get(), 
                'Impact Areas' : areas.css('a::text \n').getall()
            }