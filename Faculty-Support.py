import scrapy
from ..items import chatbotEntry

class supportSpider(scrapy.Spider):
	name = "support"
	
	custom_settings = {
        'FEEDS': { 'Faculty-Support.csv': { 'format': 'csv', 'overwrite': 'True', 'item_export_kwargs': {'include_headers_line': False,}}},
        }

	def start_requests(self):
		allowed_domains = ['https://research.georgiasouthern.edu/']
		start_urls = ['https://research.georgiasouthern.edu/faculty-support/']
		for url in start_urls:
			yield scrapy.Request(url = url, callback = self.parse)


	def parse(self, response):
		for support in response.css('#main'):

			q0 = chatbotEntry()
			q0['Question'] = '"What does the Reasearch Faculty Support do?"',
			q0['Answer'] = support.css('p:nth-child(2)::text').get(),
			yield q0
			
			q1 = chatbotEntry()
			q1['Question'] = '"What support does the school give research teams?"',
			q1['Answer'] = support.css('p:nth-child(3)::text').get(),
			yield q1
			
			q2 = chatbotEntry()
			q2['Question'] = '"What areas are being supported?"',
			q2['Answer'] = support.css('div:nth-child(5) h3 a strong::text').get() + support.css('div:nth-child(5) h3 a::text').get() +', '+ support.css('div:nth-child(7) h3 a::text').get() +', '+ support.css('div:nth-child(9) h3 strong a::text').get() +', '+ support.css('div:nth-child(11) h3 a::text').get() +', '+ support.css('div:nth-child(13) h3 strong a::text ').get(),
			yield q2
