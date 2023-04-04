import scrapy
from ..items import chatbotEntry

class communitySpider(scrapy.Spider):
	name = "community"

	custom_settings = {
        'FEEDS': { 'Community.csv': { 'format': 'csv', 'overwrite': 'True', 'item_export_kwargs': {'include_headers_line': False,}}},
        }

	def start_requests(self):
		allowed_domains = ['https://research.georgiasouthern.edu']
		start_urls = ['https://research.georgiasouthern.edu/empowering-and-enriching-communities/']
		for url in start_urls:
			yield scrapy.Request(url = url, callback = self.parse)


	def parse(self, response):
		for community in response.css('#main'):
			
			q1 = chatbotEntry()
			q1['Question'] = '"What does the Community Enrichment team research?"',
			q1['Answer'] = community.css('p:nth-child(6)::text').get(),
			yield q1
			
			q2 = chatbotEntry()
			q2['Question'] = '"What does the Community Enrichment team specialize in?"',
			q2['Answer'] = community.css('h6:nth-child(8)::text').get() + ', ' + community.css('h6:nth-child(10)::text').get() + ', ' + community.css('h6 strong::text').get(),
			yield q2

			q3 = chatbotEntry()
			q3['Question'] = '"What is Civic Infrastructures and Public Services?"',
			q3['Answer'] = community.css('p:nth-child(9)::text').get(),
			yield q3

			q4 = chatbotEntry()
			q4['Question'] = '"What is Community Health and Wellbeing?"',
			q4['Answer'] = community.css('p:nth-child(11)::text').get(),
			yield q4

			q5 = chatbotEntry()
			q5['Question'] = '"What do they mean by Quality of Life?"', 
			q5['Answer'] = community.css('p:nth-child(13)::text').get(), 
			yield q5
