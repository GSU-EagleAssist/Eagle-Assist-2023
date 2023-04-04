import scrapy
from ..items import chatbotEntry

class advanceSpider(scrapy.Spider):
	name = "advance"

	custom_settings = {
        'FEEDS': { 'Advanced-Materials.csv': { 'format': 'csv', 'overwrite': 'True', 'item_export_kwargs': {'include_headers_line': False,}}},
        }

	def start_requests(self):
		allowed_domains = ['https://research.georgiasouthern.edu']
		start_urls = ['https://research.georgiasouthern.edu/impact-areas/advanced-materials-and-manufacturing/']
		for url in start_urls:
			yield scrapy.Request(url = url, callback = self.parse)


	def parse(self, response):
		for advance in response.css('#main'):
			
			q1 = chatbotEntry()
			q1['Question'] = '"What does the Advanced Materials and Manufacturing team research?"',
			q1['Answer'] = advance.css('p:nth-child(6)::text').get(),
			yield q1
			
			q2 = chatbotEntry()
			q2['Question'] = '"What does the Advanced Materials team specialize in?"',
			q2['Answer'] = advance.css('p strong::text '+ '\n\n').getall(),
			yield q2

			q3 = chatbotEntry()
			q3['Question'] = '"What is Materials Engineering, Processing, and Characterization?"',
			q3['Answer'] = advance.css('p:nth-child(9)::text').get(),
			yield q3

			q4 = chatbotEntry()
			q4['Question'] = '"What is Additive Manufacturing?"',
			q4['Answer'] = advance.css('p:nth-child(11)::text').get(),
			yield q4

			q5 = chatbotEntry()
			q5['Question'] = '"What is Plant Operations including Robotics and Automation?"', 
			q5['Answer'] = advance.css('p:nth-child(13)::text').get()
			yield q5
