import scrapy
from ..items import chatbotEntry

class fitnessSpider(scrapy.Spider):
	name = "fitness"
	
	custom_settings = {
        'FEEDS': { 'Holistic-Fitness.csv': { 'format': 'csv', 'overwrite': 'True', 'item_export_kwargs': {'include_headers_line': False,}}},
        }

	def start_requests(self):
		allowed_domains = ['https://research.georgiasouthern.edu']
		start_urls = ['https://research.georgiasouthern.edu/holistic-fitness-and-wellness/']
		for url in start_urls:
			yield scrapy.Request(url = url, callback = self.parse)


	def parse(self, response):
		for fitness in response.css('#main'):

			q1 = chatbotEntry()
			q1['Question'] = '"What does the Holistic Fitness and Wellness team research?"',
			q1['Answer'] = fitness.css('p:nth-child(6)::text').get(),
			yield q1
			
			q2 = chatbotEntry()
			q2['Question'] = '"What does the Holistic Fitness team specialize in?"',
			q2['Answer'] = fitness.css('h6 strong::text').getall(),
			yield q2

			q3 = chatbotEntry()
			q3['Question'] = '"What is Performance Enhancement?"',
			q3['Answer'] = fitness.css('p:nth-child(9)::text').get(),
			yield q3

			q4 = chatbotEntry()
			q4['Question'] = '"What is Innovation in Health and Wellness Treatment?"',
			q4['Answer'] = fitness.css('p:nth-child(11)::text').get(),
			yield q4

			q5 = chatbotEntry()
			q5['Question'] = '"What is Health Informatics?"', 
			q5['Answer'] = fitness.css('p:nth-child(13)::text').get(), 
			yield q5