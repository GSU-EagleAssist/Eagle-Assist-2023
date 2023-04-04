import scrapy
from ..items import chatbotEntry

class supplySpider(scrapy.Spider):
	name = "supply"
	
	custom_settings = {
        'FEEDS': { 'Supply-Chain.csv': { 'format': 'csv', 'overwrite': 'True', 'item_export_kwargs': {'include_headers_line': False,}}},
        }

	def start_requests(self):
		allowed_domains = ['https://research.georgiasouthern.edu/']
		start_urls = ['https://research.georgiasouthern.edu/logistics-and-supply-chain-innovations/']
		for url in start_urls:
			yield scrapy.Request(url = url, callback = self.parse)


	def parse(self, response):
		for supply in response.css('#main'):

			q1 = chatbotEntry()
			q1['Question'] = '"What does the Logistics and Supply Chain Innovations team do?"',
			q1['Answer'] = supply.css('p:nth-child(7)::text').get(),
			yield q1
			
			q2 = chatbotEntry()
			q2['Question'] = '"What does the Logistics and Supply team specialize in?"',
			q2['Answer'] = supply.css('h6::text').getall(),
			yield q2

			q3 = chatbotEntry()
			q3['Question'] = '"What are Logistics, Operations, and Supply Chains?"',
			q3['Answer'] = supply.css('p:nth-child(10)::text').get(),
			yield q3

			q4 = chatbotEntry()
			q4['Question'] = '"What is Automation and Machine Learning?"',
			q4['Answer'] = supply.css('p:nth-child(12)::text').get(),
			yield q4
