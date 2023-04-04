import scrapy
from ..items import chatbotEntry

class ResearchSpider(scrapy.Spider):
    name = 'research'

    custom_settings = {
        'FEEDS': { 'Research-Teams.csv': { 'format': 'csv', 'overwrite': 'True', 'item_export_kwargs': {'include_headers_line': False,}}},
        }
    
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
            
            q1 = chatbotEntry()
            q1['Question'] = '"What research teams does the school have?"',
            q1['Answer'] = areas.css('a::text \n').getall(),
            yield q1
