import scrapy
from ..items import chatbotEntry

class coastalSpider(scrapy.Spider):
	name = "coastal"

	custom_settings = {
        'FEEDS': { 'Coastal.csv': { 'format': 'csv', 'overwrite': 'True', 'item_export_kwargs': {'include_headers_line': False,}}},
        }

	def start_requests(self):
		allowed_domains = ['https://research.georgiasouthern.edu']
		start_urls = ['https://research.georgiasouthern.edu/coastal-sustainability-and-resilience/']
		for url in start_urls:
			yield scrapy.Request(url = url, callback = self.parse)


	def parse(self, response):
		for coastal in response.css('#main'):
			
			q1 = chatbotEntry()
			q1['Question'] = '"What does the Coastal Sustainability and Resilience team research?"',
			q1['Answer'] = coastal.css('p:nth-child(7)::text').get() + ' ' + coastal.css('p:nth-child(8)::text').get(), 
			yield q1
			
			q2 = chatbotEntry()
			q2['Question'] = '"What does Costal Sustainability team specialize in?"',
			q2['Answer'] = coastal.css('h6::text').getall(),
			yield q2

			q3 = chatbotEntry()
			q3['Question'] = '"What is Conservation Biology and Shoreline Ecology?"',
			q3['Answer'] = coastal.css('p:nth-child(12)::text').get(),
			yield q3

			q4 = chatbotEntry()
			q4['Question'] = '"What is Water Quality?"',
			q4['Answer'] = coastal.css('p:nth-child(14)::text').get(),
			yield q4

			q5 = chatbotEntry()
			q5['Question'] = '"What are Water Resources?"', 
			q5['Answer'] = coastal.css('p:nth-child(16)::text').get()
			yield q5
